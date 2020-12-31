<template>
  <div class="login">
    <div class="header">
      <div class="description-4">
        Welcome to the cohort manager of the recruiting analytics platform
      </div>
    </div>

    <div class="login-form-wrapper">
      <div class="description-2">To continue, sign in:</div>
      <b-form @submit.prevent="onSubmit()" class="login-form">
        <b-input
          v-model="selectedInfo.email"
          placeholder="Type your email address*"
          type="email"
        >
        </b-input>
        <b-input
          v-model="selectedInfo.password"
          placeholder="Type your password*"
          type="password"
        >
        </b-input>
        <div style="display: flex; width: 100%">
          <div style="margin-left: auto">
            <b-button
              type="submit"
              :disabled="
                !selectedInfo.email.length || !selectedInfo.password.length
              "
              class="torre-button"
            >
              CONTINUE
            </b-button>
          </div>
        </div>
      </b-form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";

@Component({})
export default class Login extends Vue {
  selectedInfo = {
    email: "",
    password: ""
  };

  onSubmit() {}
}
</script>

<style lang="scss" scoped>
@import "../../assets/scss/base/_variables";

.login {
  background: black;
  min-height: 100vh;

  .header {
    background-color: $primary-background;
    height: 46px;
    position: fixed;
    top: 46px;
    left: 0;
    right: 0;
    z-index: 4;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2), 0 1px 1px rgba(0, 0, 0, 0.14),
      0 2px 1px -1px rgba(0, 0, 0, 0.12);
    display: flex;
    align-content: baseline;
    border-top: 1px solid rgba(255, 255, 255, 0.12);

    > .description-4 {
      text-shadow: $basic-text-shadow;
      height: max-content;
      margin-top: auto;
      margin-bottom: auto;
      margin-left: 1rem;
    }
  }

  .login-form-wrapper {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    height: auto;
    max-width: 440px;
    margin: auto;
    margin-top: 92px;
    background-color: $primary-background;

    .torre-button {
      right: 0;
    }
  }
}
</style>
