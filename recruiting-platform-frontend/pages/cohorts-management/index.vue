<template>
<div class="cohort-management container">
    <div class="title-2">
        Welcome to your cohorts dashboard
    </div>
    <div class="description-2">
        Here you can add new cohorts and add users to them
    </div>
</div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";

@Component({})
export default class CohortManagement extends Vue {
}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/base/_variables";

.cohort-management {
    margin-top: 80px;
    max-width: 1200px;
    box-shadow: $basic-box-shadow;
    padding: 2rem;

    .title-2 {
        text-align: center;
    }

    .description-2 {
        color: $primary-yellow;
        margin-top: 1rem;
        text-align: center
    }
}
</style>
