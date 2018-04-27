import Vue from 'vue'
import VueRouer from 'vue-router'
//router path
import column from 'components/column/column'
import point from 'components/point/point'
import line from 'components/line/line'
import dashboard from 'components/dashboard/dashboard'
import multipleColumn from 'components/multipleColumn/multipleColumn'

import home from 'src/views/home/home'
import map from 'src/views/map/map'
import bpmn from 'src/views/bpmn/bpmn'

Vue.use(VueRouer)
export default new VueRouer({
    routes: [{
      path: '/column',
      component: column
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
          { path: 'line', component: line},
          { path: 'map', component: map},
          { path: 'bpmn', component: bpmn}
        ]
    }
],
    linkActiveClass: 'active'
})