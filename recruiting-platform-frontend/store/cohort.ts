import { Module, VuexModule, Action, Mutation } from "vuex-module-decorators";
import { Option, None, Some } from "space-lift";
import { Cohort } from "~/platform/models/cohort/Cohort"
import { CohortsService } from "~/platform/services/CohortsServices"

@Module({
  name: "cohort",
  namespaced: true,
  stateFactory: true
})
export default class cohort extends VuexModule {
  _cohorts: Cohort[] = [];
  _currentCohort: Option<Cohort> = None;

  private cohortService = new CohortsService()

  get currentCohort() {
    return this._currentCohort;
  }

  get cohorts() {
    return this._cohorts;
  }

  @Action
  fetchCohorts(){
    this.cohortService.fetchCohorts().then(cohorts => this.setCohorts(cohorts))
  }

  @Mutation
  setCohorts(cohorts: Cohort[]) {
    this._cohorts = cohorts;
  }

  @Mutation
  setCurrentCohort(cohortId: number) {
    this._currentCohort = Option(this.cohorts.find(cohort => cohort.id === cohortId))
  }
}
