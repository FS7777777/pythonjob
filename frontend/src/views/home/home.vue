<template>
    <div style="height: 100px;">
        <Row>
            <Col span="2"></Col>
            <Col span="11">
                <Progress :percent="25"></Progress>
                <i-switch v-model="islove"></i-switch>
                <Button type="success"  @click="bchange(!islove)">Success</Button>
            </Col>
        </Row>
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
export default {
    computed: {
        ...mapGetters({
        islove: 'islove',
        })
    },
    methods: {
    ...mapActions({
     change : 'setinitlove'// 将 `this.setinitlove()` 映射为 `this.$store.dispatch('setinitlove')`
    }),
    bchange(love){
        this.change(love)
    }
  }
}
</script>
<style scoped>

</style>