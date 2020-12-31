import { Option } from "space-lift";

export enum AuthenticationStates {
  LOGGED_IN = "LOGGED_IN",
  LOGGED_OUT = "LOGGED_OUT",
  SESSION_EXPIRED = "SESSION_EXPIRED",
  AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
}

export type TokenWrapper = {
  token: string;
};

export type AuthenticationTokenInformation = {
  token: string;
  nextRoute: string;
  params: Option<Object>;
};

export type AuthenticationLoginInformation = {
  username: string;
  password: string;
  nextRoute: string;
  params: Option<Object>;
};

export type AuthenticationGeneralInformation = {
  token: string;
  nextRoute: string;
  params: Option<Object>;
};

export type ObtainTokenResponse = {
  token: string;
  email: string;
};
