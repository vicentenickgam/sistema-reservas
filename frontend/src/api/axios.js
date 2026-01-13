import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/",
});

// Variable para evitar múltiples refresh al mismo tiempo
let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });
  failedQueue = [];
};

// INTERCEPTOR
api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    if (
      error.response?.status === 401 &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;

      const refresh = localStorage.getItem("refresh");
      if (!refresh) return Promise.reject(error);

      if (isRefreshing) {
        return new Promise(function (resolve, reject) {
          failedQueue.push({ resolve, reject });
        }).then(token => {
          originalRequest.headers["Authorization"] = "Bearer " + token;
          return api(originalRequest);
        });
      }

      isRefreshing = true;

      try {
        const res = await axios.post(
          "http://localhost:8000/api/token/refresh/",
          { refresh }
        );

        const newAccess = res.data.access;

        processQueue(null, newAccess);
        isRefreshing = false;

        originalRequest.headers["Authorization"] =
          "Bearer " + newAccess;

        return api(originalRequest);
      } catch (err) {
        processQueue(err, null);
        isRefreshing = false;
        localStorage.removeItem("refresh");
        return Promise.reject(err);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
