<template>
  <div class="add-cohort" @click="openModal()">
    <div class="title-2">Add Cohort</div>
    <div class="circle-icon">
        <font-awesome-icon class="description-1" icon="plus" />
    </div>
    <div class="description-3">
        Create a new cohort and manage your candidates for a specific opportunity
    </div>
    <b-modal
      id="add-cohort-modal"
      ref="add-cohort-modal"
      hide-footer
      hide-header
      no-close-on-esc
      no-close-on-backdrop
      size="md"
      centered
    >
        <CohortModalWrapper :hideFunction="hideModal" />
    </b-modal>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";
import CohortModalWrapper from "./CohortModalWrapper";

@Component({
    components: {
        CohortModalWrapper
    }
})
export default class AddCohortCard extends Vue {
    openModal() {
        this.$refs["add-cohort-modal"].show();
    }

    hideModal() {
        this.$refs["add-cohort-modal"].hide();
    }
}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/base/_variables";

.add-cohort {
  box-shadow: $basic-box-shadow;
  max-width: 250px;
  cursor: pointer;
  padding: .6rem;
  text-align: center;
  margin: 1rem;

  &:hover {
      border: 1px solid $primary-yellow;
  }

  .description-3 {
    color: $primary-yellow;
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