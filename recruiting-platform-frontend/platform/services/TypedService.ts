import axios, { AxiosInstance } from "axios";
import { Option, None } from "space-lift";

export class TypedService {
  api: AxiosInstance;

  constructor(jwt: Option<string> = None) {
    this.api = this.initAxios(jwt);
  }

  initAxios(jwt: Option<string> = None) {
    const api = axios.create({
      baseURL: process.env.baseUrl
    });

    const jsonWebToken = jwt.fold(
      () => {
        localStorage.getItem(
          `token-manager-${localStorage.getItem("username")}`
        );
        return Option(
          localStorage.getItem(
            `token-manager-${localStorage.getItem("username")}`
          )
        ).fold(() => "", token => token);
      },
      token => token
    );
    api.defaults.headers.common["Authorization"] = `JWT ${jsonWebToken}`;
    api.defaults.headers.post["Content-Type"] = "application/json";
    api.defaults.headers.post["Accept"] = "application/json";

    return api;
  }

  get(url: string) {
    const api = this.initAxios();
    return api.get(url).catch(error => this.onError(error));
  }

  patch(url: string, payload: Object) {
    const api = this.initAxios();
    return api.patch(url, payload).catch(error => this.onError(error));
  }

  post(url: string, payload: Object) {
    const api = this.initAxios();
    return api.post(url, payload).catch(error => this.onError(error));
  }

  postMultipartFormData(url: string, formData: FormData) {
    const api = this.initAxios();
    const config = {
      headers: {
        "content-type": "multipart/form-data"
      }
    };

    return api.post(url, formData, config).catch(error => this.onError(error));
  }

  patchMultipartFormData(url: string, formData: FormData) {
    const api = this.initAxios();
    const config = {
      headers: {
        "content-type": "multipart/form-data"
      }
    };

    return api.patch(url, formData, config);
  }

  onError(error: any) {
    const code = parseInt(error.response && error.response.status);

    switch (code) {
      case 404:
        alert("Backend service '" + error.config.url + "' not found");
        break;
      case 401:
        console.log("Authentication error, session token expired");
        localStorage.removeItem(
          `token-manager-${localStorage.getItem("username")}`
        );
        location.reload(true);
        break;
      case 500:
        console.error("500 error in server");
        break;
      default:
        console.error(code, error.response);
        break;
    }
  }
}
