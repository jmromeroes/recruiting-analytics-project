import { AuthenticationStates } from "~/platform/models/authentication/Authentication";
import { authenticationStore } from "~/store";
export default function({ redirect, route }) {
  authenticationStore.inspectToken();
  switch (authenticationStore.authenticationState) {
    case AuthenticationStates.LOGGED_OUT:
    case AuthenticationStates.AUTHENTICATION_ERROR:
      redirect(
        `/login/`
      );
  }
}
