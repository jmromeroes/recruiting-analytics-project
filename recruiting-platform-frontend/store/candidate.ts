import { Module, VuexModule, Action, Mutation } from "vuex-module-decorators";
import { Option, None, Some } from "space-lift";
import { Candidate } from "~/platform/models/candidate/Candidate"
import { CandidatesService } from "~/platform/services/CandidatesService"
import { candidateStore, cohortStore } from "~/store"

@Module({
    name: "candidate",
    namespaced: true,
    stateFactory: true
})
export default class candidate extends VuexModule {
    candidates: Candidate[] = [];
    _errorMessage: string = "";
    private candidatesService = new CandidatesService();

    get errorMessage() {
        return this._errorMessage;
    }

    @Action
    fetchCandidates() {
        cohortStore.currentCohort.fold(
            () => this.setCandidates([]),
            cohort =>
                this.candidatesService.fetchCandidatesInCohort(cohort.id).then(candidates => {
                    this.setCandidates(candidates)
                })
                .catch(error => {
                    this.setErrorMessage(error.toString())
                })
        )
    }

    @Action
    addCandidate(publicId: string){
        cohortStore.currentCohort.fold(
            () => {},
            cohort =>
                this.candidatesService.addCandidate(cohort.id, publicId).then(candidate => {
                    console.log(candidate)
                    this.fetchCandidates()
                })
                .catch(error => {
                    this.setErrorMessage(error.toString())
                })
        )
    }

    @Mutation
    setCandidates(candidates: Candidate[]) {
        this.candidates = candidates;
    }

    @Mutation
    setErrorMessage(errorMessage: string) {
        this._errorMessage = errorMessage;
    }
}
