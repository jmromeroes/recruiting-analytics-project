import { Store } from "vuex";
import { getModule, config } from "vuex-module-decorators";
import authentication from "~/store/authentication";

// Set rawError to true by default on all @Action decorators, in this way we can avoid ERR_ACTION_ACCESS_UNDEFINED
// to identify which are the errors in @Action functions
config.rawError = true;

let authenticationStore: authentication;

function initialiseStores(store: Store<any>): void {
  authenticationStore = getModule(authentication, store);
}

export { initialiseStores, authenticationStore };
