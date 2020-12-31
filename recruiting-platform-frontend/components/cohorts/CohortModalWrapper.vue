<template>
  <div class="cohort-modal-wrapper">
    <div class="cohort-creator-header" v-if="currentStep === 0">
      <div class="description-2">CREATE YOUR COHORT</div>
      <div class="description-3 yellow-text">STARTING UP</div>
    </div>
    <div class="cohort-creator-header" v-else>
      <div class="description-2">CREATE YOUR COHORT</div>
      <div class="description-3 yellow-text">STEP {{ currentStep }}</div>
    </div>

    <div class="cohort-creator-content" v-if="currentStep === 0">
      <div class="description-2">
        <b>Welcome to the cohort creator.</b>
      </div>
      <div class="description-3">
        Please follow the next steps so you can create your cohort from a Torre
        opportunity
      </div>
      <div class="action-buttons">
        <b-button @click="prevStep()" class="torre-button">
          Close
        </b-button>
        <b-button @click="nextStep()" class="torre-button"> Next </b-button>
      </div>
    </div>

    <div class="cohort-creator-content" v-else-if="currentStep === 1">
      <div class="cohort-form">
        <div class="description-2">
          <b>Add your opportunity id</b>
        </div>
        <div style="text-align: left" class="description-3">
          Go to the Torre platform an look for the public id of the opportunity
          you want to reference as base for your cohort
        </div>
        <div
          style="text-align: left; margin-top: 1rem"
          class="description-3 yellow-text"
        >
          Some example ids for you to test with are: awK0LDdn, mwALR7WJ,
          Yd6vGjdp, VWM2PAwZ, Yd6vLgdp, Prlg9Ldk, EW7k67Wy
        </div>

        <b-input v-model="opportunityId" placeholder="Assing the opportunity to the cohort"> </b-input>
        <div class="action-buttons">
          <b-button @click="prevStep()" class="torre-button">
            Back
          </b-button>
          <b-button @click="nextStep()" :disabled="!opportunityId.length" class="torre-button"> Next </b-button>
        </div>
      </div>
    </div>
    <div class="cohort-creator-content" v-else-if="currentStep === 2">
      <div class="cohort-form">
        <div class="description-2">
          <span class="yellow-text" v-if="currentCohort">
              <b>ID: {{currentCohort.id}}</b>
          </span>
          <b>Add your candidates</b>
        </div>
        <div style="text-align: left" class="description-3">
          Go to the Torre platform an look for the public id of the candidate
          you want to add to the cohort
        </div>
        <div
          style="text-align: left; margin-top: 1rem"
          class="description-3 yellow-text"
        >
          Some example ids for you to test with are: jmromeroe, torrenegra,
          rolfveldman, danielabotero, taniazapata, nataliagkioka, kunlaoye
        </div>
        <b-input v-model="userId" placeholder="Assing the opportunity to the cohort"> </b-input>

        <div class="candidates-wrapper">
            <div>

            </div>
        </div>
        <div class="action-buttons">
          <b-button @click="prevStep()" class="torre-button">
            Back
          </b-button>
          <b-button @click="nextStep()" :disabled="!userId.length || isLoading" class="torre-button"> Next </b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";
import { cohortStore } from "~/store";
import { candidateStore } from "~/store";
import { CohortStates } from "~/platform/models/cohort/Cohort"
import { Candidate } from "~/platform/models/candidate/Candidate"

@Component({})
export default class CohortModalWrapper extends Vue {
  @Prop() hideFunction: Function;

  currentStep: number = 0;
  opportunityId: string = "";
  userId: string = "";

  get currentCohortState() {
    return cohortStore.currentCohortState
  }

  get currentCohort() {
    return cohortStore.currentCohort.fold(
        () => undefined,
        v => v
    )
  }

  get isLoading() {
    return cohortStore.currentCohortState === CohortStates.LOADING
  }

  get candidates() {
    return candidateStore.candidates
  }

  @Watch("currentCohortState")
  onStateUpdated(newVal: CohortStates, oldVal: CohortStates){
      if(newVal === CohortStates.CREATED){
          this.currentStep += 1
      }
  }

  nextStep() {
    if(this.currentStep === 1){
        cohortStore.addCohort(this.opportunityId)
    } else if(this.currentStep === 2){
        candidateStore.addCandidate(this.userId)
    } else {
        this.currentStep += 1
    }
  }
    
  prevStep() {
    if (this.currentStep == 0) {
      this.hideFunction();
      return;
    }

    this.currentStep = this.currentStep - 1;
  }

}
</script>

<style lang="scss">
.cohort-modal-wrapper {
  display: flex;
  flex-direction: column;

  .cohort-creator-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .action-buttons {
    margin: auto;
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  .cohort-creator-content {
    text-align: center;
    padding: 1rem;
  }
}
</style>