import { Store } from "vuex";
import { initialiseStores } from "~/platform/utils/store-accessor";

const initializer = (store: Store<any>) => initialiseStores(store);

export const plugins = [initializer];
export * from "~/platform/utils/store-accessor";
