<template>
    <div style="background:#eee;padding:20px">
        <el-button type="primary" size="small" :loading="loading" @click="showModal">加载中</el-button>
        <el-button type="primary" size="small" @click="add">添加</el-button>
        <el-button type="primary" size="small" @click="changefirst">修改</el-button>
        <div>
            <div v-for="fun in funs" >
                <funmodel v-bind:formInline="fun"></funmodel>
            </div>
        </div>

        <!-- 历史数据条件过滤 -->
       <el-dialog title="模板" :visible.sync="dialogVisible" :close-on-click-modal="false" width="30%">
            <span>这是一段信息</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="cancel">取 消</el-button>
                <el-button type="primary" @click="ok">确 定</el-button>
            </span>
        </el-dialog>
   </div> 
</template>
<script>
import funmodel from 'components/model/model'
export default {
  components: {
    funmodel
  },
  data () {
        return {
            dialogVisible: false,
            loading:false,
            funs:[]
        }
    },
    methods: {
        showModal(){
            this.loading=true;
            this.dialogVisible=true;
            console.log(this.funs);
        },
        ok() {
            this.$message({type: 'info',message:'yes'});
            this.loading=false;
            this.dialogVisible=false;
        },
        cancel () {
            this.$message({type: 'info',message:'no'});
            this.loading=false;
            this.dialogVisible=false;
        },
        add(){
            this.funs.push({user:"是我",region:"beijing"});
        },
        changefirst(){
            if(this.funs.length>0){
                this.funs[0].user="是你"
            }
        }
    }
}
</script>
<style>

</style>