<<template>
    <div style="background:#eee;padding:20px">
        <el-button type="primary" size="small" :loading="loading" @click="showModal">加载中</el-button>


        <!-- 历史数据条件过滤 -->
        <Modal v-model="modal1" title="Common Modal dialog box title"
            @on-ok="ok"
            @on-cancel="cancel">
            <p>Content of dialog</p>
            <p>Content of dialog</p>
            <p>Content of dialog</p>
        </Modal>
   </div> 
</template>
<script>
export default {
  data () {
        return {
            modal1: false,
            loading:false
        }
    },
    methods: {
        showModal(){
            this.loading=true;
            this.modal1=true;
        },
        ok () {
            this.$Message.info('Clicked ok');
            this.loading=false;
        },
        cancel () {
            this.$Message.info('Clicked cancel');
            this.loading=false;
        }
    }
}
</script>
<style>

</style>