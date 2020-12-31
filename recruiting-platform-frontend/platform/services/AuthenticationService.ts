import axios from "axios";

import { TypedService } from "./TypedService";
import { AuthenticationRequest } from "~/platform/models/authentication/api/AuthenticationRequest";

import { Some, None, Option } from "space-lift";
import {
  TokenWrapper,
  ObtainTokenResponse
} from "../models/authentication/Authentication";

export class AuthenticationService extends TypedService {
  readonly obtainJWT = "/auth/obtain_token";
  readonly refreshJWT = "/auth/refresh_token";

  async obtainToken(
    authInformation: AuthenticationRequest
  ): Promise<Option<ObtainTokenResponse>> {
    return this.post(this.obtainJWT, authInformation).then(response => {
      if (response.data.token) {
        return Some({
          token: response.data.token,
          userType: response.data.user_type,
          email: response.data.email,
          learningTrack: response.data.learning_track
        });
      }

      return None;
    });
  }

  async refreshToken(token: TokenWrapper): Promise<Option<TokenWrapper>> {
    return this.post(this.refreshJWT, { token }).then(response => {
      if (response.data.token) {
        return Some({
          token: response.data.token
        });
      }

      return None;
    });
  }
}
