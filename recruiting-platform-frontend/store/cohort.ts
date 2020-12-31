import { Module, VuexModule, Action, Mutation } from "vuex-module-decorators";
import { Option, None, Some } from "space-lift";
import { Cohort, CohortStates } from "~/platform/models/cohort/Cohort"
import { CohortsService } from "~/platform/services/CohortsServices"

@Module({
    name: "cohort",
    namespaced: true,
    stateFactory: true
})
export default class cohort extends VuexModule {
    _cohorts: Cohort[] = [];
    _currentCohort: Option<Cohort> = None;
    _currentCohortState: CohortStates = CohortStates.NOT_CREATED;
    _errorMessage: string = ""

    private cohortService = new CohortsService()

    get currentCohort() {
        return this._currentCohort;
    }

    get cohorts() {
        return this._cohorts;
    }

    get currentCohortState() {
        return this._currentCohortState;
    }

    get errorMessage() {
        return this._errorMessage;
    }

    @Action
    fetchCohorts() {
        this.setCurrentCohortState(CohortStates.LOADING)
        this.cohortService.fetchCohorts().then(cohorts => {
            this.setCohorts(cohorts)
            this.setCurrentCohortState(CohortStates.CREATED)
        })
        .catch(error => {
            this.setErrorMessage(error.toString())
        })
    }

    @Action
    addCohort(opportunityId: string) {
        this.setCurrentCohortState(CohortStates.LOADING)
        this.cohortService.addCohort(opportunityId).then(cohort => {
            this.setCurrentCohortState(CohortStates.CREATED)
            this.setCohorts(this._cohorts.concat([cohort]))
            this.setCurrentCohort(cohort.id)
        })
        .catch(error => {
            this.setErrorMessage(error.toString())
        })
    }

    @Mutation
    setCohorts(cohorts: Cohort[]) {
        this._cohorts = cohorts;
    }

    @Mutation
    setCurrentCohort(cohortId: Number) {
        this._currentCohort = Option(this.cohorts.find(cohort => cohort.id === cohortId))
    }

    @Mutation
    setCurrentCohortState(currentCohortState: CohortStates) {
        this._currentCohortState = currentCohortState
    }

    @Mutation
    setErrorMessage(errorMessage: string) {
        this._errorMessage = errorMessage;
    }
}
