import Vue from 'vue';
import Router from 'vue-router';
import ListParticipant from '@/components/ListParticipant';
import AddParticipant from '@/components/AddParticipant';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/list-participant',
      name: 'list-participant',
      component: ListParticipant
    },
    {
      path: '/add-participant',
      name: 'add-articipant',
      component: AddParticipant
    }
  ]
})
