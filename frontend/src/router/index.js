import Vue from 'vue'
import VueRouer from 'vue-router'
//router path
import column from 'components/column/column'
import funnel from 'components/funnel/funnel'
import heat from 'components/heat/heat'
import point from 'components/point/point'
import line from 'components/line/line'
import dashboard from 'components/dashboard/dashboard'
import multipleColumn from 'components/multipleColumn/multipleColumn'

import home from 'src/views/home/home'

Vue.use(VueRouer)
export default new VueRouer({
    routes: [{
      path: '/column',
      component: column
    }, {
      path: '/funnel',
      component: funnel
    }, {
      path: '/heat',
      component: heat
    }, {
      path: '/point',
      component: point
    }, {
      path: '/dashboard',
      component: dashboard
    }, {
      path: '/multipleColumn',
      component: multipleColumn
    }, {
      path: '/line',
      component: line
    },{
        path: '/home',
        component: home,
        children:[ 
          { path: 'line', component: line}
        ]
    }
],
    linkActiveClass: 'active'
})