import jwt_decode from "jwt-decode";
import { Module, VuexModule, Action, Mutation } from "vuex-module-decorators";
import { Option, None, Some } from "space-lift";
import {
  AuthenticationLoginInformation,
  AuthenticationGeneralInformation,
  TokenWrapper,
  AuthenticationStates
} from "~/platform/models/authentication/Authentication";
import { AuthenticationService } from "~/platform/services/AuthenticationService";
import { userTypeStore, learningTrackStore } from "~/store";

@Module({
  name: "authentication",
  namespaced: true,
  stateFactory: true
})
export default class authentication extends VuexModule {
  _username: string = <string>localStorage.getItem("username");
  localStorageToken = localStorage.getItem(`token-manager-${this._username}`);

  token: Option<TokenWrapper> = this.localStorageToken
    ? Some(JSON.parse(this.localStorageToken))
    : None;

  _authenticationService: AuthenticationService = new AuthenticationService();

  _authenticationState = this.token.fold(
    () => {
      return AuthenticationStates.LOGGED_OUT;
    },
    _ => {
      return AuthenticationStates.LOGGED_IN;
    }
  );

  @Action
  async obtainToken(authData: AuthenticationLoginInformation) {
    this._authenticationService
      .obtainToken({ username: authData.username, password: authData.password })
      .then(tokenInfo => {
        tokenInfo.fold(
          () => {},
          _tokenInfo => {
            localStorage.setItem("username", authData.username);

            this.obtainTokenSuccess({
              token: _tokenInfo.token,
              nextRoute: authData.nextRoute,
              params: authData.params
            });
          }
        );
      })
      .catch(err => this.obtainTokenFailure());
  }

  @Action
  async refreshToken(token: TokenWrapper) {
    this._authenticationService.refreshToken(token).then(tokenInfo => {
      tokenInfo.fold(
        () => {},
        _tokenInfo => {
          this.obtainTokenSuccess({
            token: _tokenInfo.token,
            nextRoute: "",
            params: None
          });
        }
      );
    });
  }

  @Action
  async removeToken() {
    this._removeToken();
  }

  @Action
  async inspectToken() {
    this.token.fold(
      () => {},
      _token => {
        const decoded = jwt_decode(_token);
        const exp = decoded.exp;
        const orig_iat = decoded.orig_iat;
        if (
          exp - Date.now() / 1000 < 1800 &&
          Date.now() / 1000 - orig_iat < 628200
        ) {
          this.refreshToken(_token);
        } else if (exp - Date.now() / 1000 < 0) {
          this.removeToken();
        }
      }
    );
  }

  @Action
  obtainTokenFailure() {
    this._obtainTokenFailure();
  }

  @Action
  obtainTokenSuccess(authInfo: AuthenticationGeneralInformation) {
    this._obtainTokenSuccess({ authInfo, router: this.store.$router });
  }

  get authenticationState() {
    return this._authenticationState;
  }

  @Mutation
  _obtainTokenSuccess(payload: {
    authInfo: AuthenticationGeneralInformation;
    router: Object;
  }) {
    this._authenticationState = AuthenticationStates.LOGGED_IN;

    localStorage.setItem(
      `token-manager-${localStorage.getItem("username")}`,
      `"${payload.authInfo.token}"`.replace('""', '"')
    );

    return payload.router.push("/cohorts-management");
  }

  @Mutation
  _obtainTokenFailure() {
    this._authenticationState = AuthenticationStates.AUTHENTICATION_ERROR;
  }

  @Mutation
  _removeToken() {
    this._authenticationState = AuthenticationStates.LOGGED_OUT;
    this.token = None;
    const token = localStorage.removeItem(
      `token-manager-${localStorage.getItem("username")}`
    );
    localStorage.removeItem("username");
    location.reload();
  }
}
