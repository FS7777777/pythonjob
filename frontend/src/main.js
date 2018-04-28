import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import router from './router'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import store from './store'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';


Vue.use(Vuex)
Vue.use(iView);

new Vue({
  router,
  store,
  template: '<App/>',
  components: {App},
  data: {
    eventHub: new Vue(),
    charts: []
  }
}).$mount('#app')

router.beforeEach((to, from, next) => {
  iView.LoadingBar.start();
  next();
});

router.afterEach(route => {
  iView.LoadingBar.finish();
});
//router.push('dashboard')
