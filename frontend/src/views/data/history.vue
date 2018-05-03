<<template>
    <div style="background:#eee;padding:20px">
        <el-button type="primary" size="small" :loading="loading" @click="showModal">加载中</el-button>


        <!-- 历史数据条件过滤 -->
       <el-dialog title="提示" :visible.sync="dialogVisible" :close-on-click-modal="false" width="30%">
            <span>这是一段信息</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="cancel">取 消</el-button>
                <el-button type="primary" @click="ok">确 定</el-button>
            </span>
        </el-dialog>
        <children>
            <span>子组件内部元素</span>
        </children>
   </div> 
</template>
<script>
export default {
    components: {
      children: {
        template: '<div><slot><p>默认效果</p></slot>这里是子组件</div>'
      }
    },
  data () {
        return {
            dialogVisible: false,
            loading:false
        }
    },
    methods: {
        showModal(){
            this.loading=true;
            this.dialogVisible=true;
        },
        ok () {
            this.$message({type: 'info',message:'yes'});
            this.loading=false;
            this.dialogVisible=false;
        },
        cancel () {
            this.$message({type: 'info',message:'no'});
            this.loading=false;
            this.dialogVisible=false;
        }
    }
}
</script>
<style>

</style>