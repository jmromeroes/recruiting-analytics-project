<template>
  <div class="cohort-candidates">
    <div class="title-2">This cohort's candidates information</div>

    <div
      class="coh-content"
      v-for="(candidate, index) in candidates"
      :key="index"
    >
      <div class="description-3">
        <b><span class="yellow-text">User: </span></b>
        <span>{{ candidate.publicId }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Country: </span></b>
        <span>{{ candidate.country }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Bio: </span></b>
        <span>{{ candidate.bio }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Jobs: </span></b>
        <span>{{ candidate.jobs }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Links: </span></b>
        <span>{{ candidate.links }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Number of strengths: </span></b>
        <span>{{ candidate.numberOfStrengths }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Number of jobs: </span></b>
        <span>{{ candidate.numberOfJobs }}</span>
      </div>

      <div class="description-3">
        <b><span class="yellow-text">Number of awards: </span></b>
        <span>{{ candidate.numberOfAwards }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Number of projects: </span></b>
        <span>{{ candidate.numberOfProjects }}</span>
      </div>
      <div class="description-3">
        <b><span class="yellow-text">Number of interests: </span></b>
        <span>{{ candidate.numberOfInterests }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";
import { cohortStore } from "~/store";
import { candidateStore } from "~/store";
import { CohortStates, Cohort } from "~/platform/models/cohort/Cohort";
import { Candidate } from "~/platform/models/candidate/Candidate";

@Component({})
export default class CandidatesVisualization extends Vue {
  @Prop() cohort: Cohort;

  mounted() {
    cohortStore.setCurrentCohort(this.cohort.id);
    candidateStore.fetchCandidates();
  }

  get candidates() {
    return candidateStore.candidates;
  }
}
</script>

<style lang="scss">
@import "../../assets/scss/base/_variables";

.cohort-candidates {
  .coh-content {
    border-top: 1px solid white;
    padding: 2rem;
    
    .description-3 {
      margin-top: 0.4rem;
    }
  }
}
</style>