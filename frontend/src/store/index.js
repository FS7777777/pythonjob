import Vue from 'vue'
import Vuex from 'vuex'

import state from './common/state'
import mutations from './common/mutations'
import actions from './common/actions'
import getters from './common/getters'

Vue.use(Vuex)

export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})