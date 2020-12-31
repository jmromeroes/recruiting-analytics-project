export default (context, inject) => {
    const token = localStorage.getItem(
      `token-manager-${localStorage.getItem("username")}`
    );
    if (token) {
      context.$axios.setToken(token.replace('"', ""), "JWT");
    }
  
    context.$axios.setHeader("Content-Type", "application/json");
    context.$axios.setHeader("Accept", "application/json");
  
    context.$axios.onError(error => {
      const code = parseInt(error.response && error.response.status);
      if (code === 404) {
        alert("Backend service '" + error.config.url + "' not found");
      }
      if (code === 401) {
        localStorage.removeItem(
          `token-manager-${localStorage.getItem("username")}`
        );
        location.reload(true);
      }
    });
    inject("axios", context.$axios);
  };