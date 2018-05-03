import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import router from './router'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';


Vue.use(ElementUI);
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
