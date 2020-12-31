<template>
  <div class="header">
    <div class="header-logo">
      cohorts
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";

@Component({})
export default class Header extends Vue {}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/base/_variables";

.header {
  background-color: $primary-background;
  height: 46px;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 4;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2), 0 1px 1px rgba(0, 0, 0, 0.14),
    0 2px 1px -1px rgba(0, 0, 0, 0.12);
  display: flex;
  align-content: baseline;

  .header-logo {
    text-shadow: $basic-text-shadow;
    height: max-content;
    font-weight: 600;
    font-size: 20px;
    color: $primary-color;
    margin-top: auto;
    margin-bottom: auto;
    margin-left: 1rem;
    letter-spacing: 0.8px;
  }
}
</style>
