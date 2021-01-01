<template>
  <div class="cohort-management container">
    <div class="title-2">Welcome to your cohorts dashboard</div>
    <div class="description-2">
      Here you can add new cohorts and add users to them
    </div>

    <div class="cohorts-wrapper">
      <CohortCard v-for="(cohort, index) in cohorts" :key="index" :cohort="cohort"/>
      <AddCohortCard />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";
import { cohortStore } from "~/store";
import CohortCard from "~/components/cohorts/CohortCard";
import AddCohortCard from "~/components/cohorts/AddCohortCard";

@Component({
  middleware: ["authenticated", "loadGeneralData"],
  components: {
      CohortCard,
      AddCohortCard
  }
})
export default class CohortManagement extends Vue {
    
    get cohorts(){
        return cohortStore.cohorts;
    }
}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/base/_variables";

.cohort-management {
  margin-top: 80px;
  max-width: 900px;
  padding: 2rem;

  .title-2 {
    text-align: center;
  }

  .description-2 {
    color: $primary-yellow;
    text-align: center;
  }

  .cohorts-wrapper {
    margin-top: 2rem;
    display: flex;
    flex-wrap: wrap;
  }
}
</style>
