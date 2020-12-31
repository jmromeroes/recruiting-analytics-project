import {
  cohortStore
} from "~/store";

export default function ({
  redirect,
  route
}) {
  cohortStore.fetchCohorts()
}
