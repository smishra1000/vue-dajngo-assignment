<template>
  <div class="add-participant">
    <section class="hero">
      <div class="hero-body">
        <div class="field">
          <label class="label">First Name</label>
          <div class="control">
            <input
              class="input"
              type="text"
              placeholder="Name"
              v-model="first_name"
            />
          </div>
        </div>
        <div class="field">
          <label class="label">Last Name</label>
          <div class="control">
            <input
              class="input"
              type="text"
              placeholder="Name"
              v-model="last_name"
            />
          </div>
        </div>

        <div class="field">
          <label class="label">Email</label>
          <div class="control">
            <input
              class="input"
              type="text"
              placeholder="Email"
              value=""
              v-model="email"
            />
          </div>
        </div>

        <div class="field">
          <label class="label">Type of Participant</label>
          <div class="control">
            <div class="select">
              <select v-model="participant_type" on:change="changeType(participant_type)">
                <option value="1">Band</option>
                <option value="2">Carriage</option>
              </select>
            </div>
          </div>
        </div>

        <div class="field">
          <label class="label">Foundation date</label>
          <div class="control">
            <input
              class="input"
              type="date"
              placeholder="Foundation Date"
              value=""
              v-model="foundation_date"
            />
          </div>
        </div>
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-primary" @click="save()">Submit</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "addparticipant",
  data() {
    return {
      participant_type:1,
      foundation_date:"",
      email:"",
      last_name:"",
      first_name:"",

    };
  },
  methods:{
    changeType(selectedType) {
        this.participant_type = selectedType;
    },
    save() {
      let body = {
        email:this.email,
        last_name:this.last_name,
        first_name:this.first_name,
        foundation_date:new Date(this.foundation_date).toISOString(),
        participant_type:this.participant_type,
      }
      var config = {
        headers: { "Content-Type": "application/json" },
        responseType: "json",
      };
      axios
        .post(
          "http://localhost:8000/api/",
          body,
          config
        )
        .then((response) => {
         console.log("created");
         this.$router.push('/list-participant')
        });
    },
  }
};
</script>

<style lang="sass" scoped>
@import '../mq'

.hero
  background-size: cover

  .title
    +mobile
      font-weight: bold
    +tablet
      font-size: 2.5rem
    +desktop
      font-size: 4rem
      margin-top: 2rem

h2
  margin: 1.5rem 0 2rem 0 !important

.fa-cog
  font-size: 40px

#learn
  +desktop
    margin-bottom: 2rem

.pd
  +tablet
    padding: 2em 0
</style>
