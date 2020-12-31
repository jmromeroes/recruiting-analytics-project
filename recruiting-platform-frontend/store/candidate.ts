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
    errorMessage: string = "";
    private candidatesService = new CandidatesService();

    @Action
    fetchCandidates() {
        cohortStore.currentCohort.fold(
            () => this.setCandidates([]),
            cohort =>
                this.candidatesService.fetchCandidatesInCohort(cohort.id).then(candidates => {
                    this.setCandidates(candidates)
                })
        )
    }

    @Action
    addCandidate(publicId: string){
        cohortStore.currentCohort.fold(
            () => {},
            cohort =>
                this.candidatesService.addCandidate(cohort.id, publicId).then(candidates => {
                    this.fetchCandidates()
                })
        )
    }

    @Mutation
    setCandidates(candidates: Candidate[]) {
        this.candidates = candidates;
    }
}
