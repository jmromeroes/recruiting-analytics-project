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

    <div class="cohort-creator-content">
      <div class="description-2">
        <b>Welcome to the cohort creator.</b>
      </div>
      <div class="description-3">
        Please follow the next steps so you can create your cohort from a Torre
        opportunity
      </div>
    </div>

    <div class="action-buttons">
      <b-button @click="prevStep()" class="torre-button"> Back </b-button>
      <b-button class="torre-button"> Next </b-button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";

@Component({})
export default class CohortModalWrapper extends Vue {
  @Prop() hideFunction: Function;

  currentStep: number = 0;

  nextStep() {
    this.currentStep = this.currentStep + 1;
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