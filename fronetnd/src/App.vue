<template>
  <div id="app">
    <div class="nav">
      <div class="container">
        <div class="nav-left">
          <a class="nav-item">Assignment</a>
        </div>

        <span class="nav-toggle" v-on:click="toggleNav" v-bind:class="{ 'is-active': isActive }">
          <span></span>
          <span></span>
          <span></span>
        </span>

        <div class="nav-right nav-menu" v-bind:class="{ 'is-active': isActive }">

          <router-link to="list-participant" class="nav-item r-item">View Participant</router-link>
          <router-link to="add-participant" class="nav-item r-item">Join As Participant</router-link>

        </div>
      </div>
    </div>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data: function() {
    return {
      isActive: false
    }
  },
  methods: {
    toggleNav: function() {
      this.isActive = !this.isActive;
    }
  }
}
</script>

<style lang="sass">
@import '../node_modules/bulma/bulma.sass'
@import 'mq'

.nav
  background-color: #383838
  

a.nav-item:not(.button)
  color:#ffffff
a.nav-item:not(.button):hover
  color:#FFFFFF
.nav-left a 
  color: #fff
  font-weight: bold

a.r-item
  color:#FFFFFF
  padding: 0.5rem 1.75rem
  +mobile
    color: gray


.nav-toggle span
  background-color: #C1C1C1

footer
  background-color: $primary !important
  color: #fff

  .icon
    color: #fff
    margin-left: 20px

</style>