<template>
  <div class="add-cohort" @click="openModal()">
    <div class="title-2">{{cohort.name}}</div>
    <div class="description-3 descriptions">
        <div style="margin-top: .4rem">
            <b><span class="yellow-text">Objective: </span></b><span>{{cohort.opportunityObjective}}</span>
        </div>
        <div style="margin-top: .4rem">
            <b><span class="yellow-text">Platform: </span></b><span>{{cohort.platformName}}</span>
        </div>
        <div style="margin-top: .4rem" v-if="cohort.organizations && cohort.organizations.length">
            <b><span class="yellow-text">Company name: </span></b><span>{{cohort.organizations[0].name}}</span>
            <div style="margin-top: .4rem">
                <img v-if="cohort.organizations[0].picture && cohort.organizations[0].picture.length" :src="cohort.organizations[0].picture" style="width: 50px; height: 50px" />
            </div>
        </div>
        <div style="margin-top: .4rem">
            <b><span class="yellow-text">Slug: </span></b><span>{{cohort.slug}}</span>
        </div>
    </div>
    <b-modal
      id="add-cohort-modal"
      ref="add-cohort-modal"
      hide-footer
      hide-header
      size="lg"
      centered
    >
        <CandidatesVisualization :cohort="cohort"/>
    </b-modal>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";
import {Cohort} from "~/platform/models/cohort/Cohort";
import CandidatesVisualization from "./CandidatesVisualization";

@Component({
    components: {
        CandidatesVisualization
    }
    
})
export default class CohortCard extends Vue {
    @Prop() cohort: Cohort;

    openModal() {
        this.$refs["add-cohort-modal"].show();
    }
}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/base/_variables";

.add-cohort {
  box-shadow: $basic-box-shadow;
  max-width: 240px;
  cursor: pointer;
  padding: .6rem;
  text-align: center;
  margin: 1rem;

  &:hover {
      border: 1px solid $primary-yellow;
  }

  .circle-icon {
      border-radius: 50%;
      border: 2px solid white;
      width: 50px;
      height: 50px;
      display: flex;
      align-content: center;
      justify-content: center;
      align-items: center;
      margin: 1rem auto;
  }
}
</style>