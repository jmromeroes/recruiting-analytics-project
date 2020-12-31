<template>
  <div>
    <Header />
    <Nuxt />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Prop } from "vue-property-decorator";
import Header from "~/components/global/Header";

@Component({
  components: {
    Header
  }
})
export default class Default extends Vue {}
</script>

<style lang="scss">
@import "../assets/scss/base/_variables";

html {
  font-family: "Muli", "Helvetica", "Arial", sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  background: $primary-background;
}

body {
  font-family: "Muli", "Helvetica", "Arial", sans-serif;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}

.form-control {
  background-color: $primary-background;
  color: $primary-color;
  margin: 1rem auto;
}

.form-control::-webkit-input-placeholder {
  color: $primary-gray;
  font-size: 13px;
  border-color: $primary-gray;
}

textarea:focus,
input[type="text"]:focus,
input[type="password"]:focus,
input[type="datetime"]:focus,
input[type="datetime-local"]:focus,
input[type="date"]:focus,
input[type="month"]:focus,
input[type="time"]:focus,
input[type="week"]:focus,
input[type="number"]:focus,
input[type="email"]:focus,
input[type="url"]:focus,
input[type="search"]:focus,
input[type="tel"]:focus,
input[type="color"]:focus,
.uneditable-input:focus {
  border-color: $primary-yellow;
  background-color: $primary-background;
  color: $primary-color;
}
</style>
