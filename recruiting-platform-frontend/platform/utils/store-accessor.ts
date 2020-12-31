import { Store } from "vuex";
import { getModule, config } from "vuex-module-decorators";
import authentication from "~/store/authentication";
import candidate from "~/store/candidate";
import cohort from "~/store/cohort";

// Set rawError to true by default on all @Action decorators, in this way we can avoid ERR_ACTION_ACCESS_UNDEFINED
// to identify which are the errors in @Action functions
config.rawError = true;

let authenticationStore: authentication;
let candidateStore: candidate;
let cohortStore: cohort;

function initialiseStores(store: Store<any>): void {
  authenticationStore = getModule(authentication, store);
  candidateStore = getModule(candidate, store);
  cohortStore = getModule(cohort, store);
}

export { initialiseStores, authenticationStore, cohortStore, candidateStore };
