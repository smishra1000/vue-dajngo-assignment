<template>
  <div class="faq">
    <div class="container">
    <h1 style="font-size:22px;">Participants List</h1>
      <section class="section">
        <table class="table">
          <thead>
            <tr>
              <th v-for="(column, index) in view_columns">
                {{ column }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in participants">
              <td>
                {{ row.first_name }}
              </td>
              <td>
                {{ row.first_name }}
              </td>
              <td>
                {{ row.email }}
              </td>
              <td>
                {{ row.participant_type==1 ? 'Band' : 'Carriage' }}
              </td>
              <td>
                {{ row.ranking }}
              </td>
              <td>
                {{ formatDate(new Date(row.foundation_date)) }}
              </td>
            </tr>

            <tr v-if="participants.length == 0">
              <td :colspan="view_columns.length" class="has-text-centered">
                No data found.
              </td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "listparticipant",
  data: () => ({
    participants: [],
    errors: [],
    view_columns: [
      "First Name",
      "Last Name",
      "Email",
      "Participant Type",
      "Rank",
      "Foundation Date",
    ],
  }),
  methods: {
    formatDate(date) {
      var hours = date.getHours();
      var minutes = date.getMinutes();
      var ampm = hours >= 12 ? "pm" : "am";
      hours = hours % 12;
      hours = hours ? hours : 12; // the hour '0' should be '12'
      minutes = minutes < 10 ? "0" + minutes : minutes;
      var strTime = hours + ":" + minutes + " " + ampm;
      return (
        date.getMonth() +
        1 +
        "/" +
        date.getDate() +
        "/" +
        date.getFullYear() +
        "  " +
        strTime
      );
    },
  },

  created() {
    axios
      .get("http://localhost:8000/api/")
      .then((response) => {
        console.log(response);
        this.participants = response.data;
      })
      .catch((e) => {});
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="sass" scoped>
@import '../mq'

.pd
  padding: 2.5em 0 1.5em 0

.answer
  margin-top: 10px !important
  color: gray

.columns
  flex-wrap: wrap
</style>
