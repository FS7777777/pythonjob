<template>
    <div>
        <el-container>
            <el-header class="selfhead" style="height:100px;">
                <el-steps :active="step" finish-status="success" align-center>
                    <el-step title="登录" description="选择登录客户"></el-step>
                    <el-step title="类型" description="选择上报类型，并上传对应文件"></el-step>
                    <el-step title="上报" description="确认上报"></el-step>
                    <el-step title="确认" description="完成确认"></el-step>
                    <el-step title="完成" description="恭喜上报完成"></el-step>
                </el-steps>
            </el-header>
            <el-main>
                <el-row :gutter="20">
                    <el-col :span="4">
                        <el-button type="success" size="small" @click="previous" :disabled="step<=0?true:false" v-show="step>=0?true:false">上一步</el-button>
                        <el-button type="success" size="small" @click="next" :disabled="step>=5?true:false" v-show="step>=0?true:false">下一步</el-button>
                    </el-col>
                    <el-col :span="20">
                        <transition name="el-zoom-in-center">
                            <el-card class="box-card" shadow="always" v-show="step==0?true:false">
                                <div slot="header">
                                    <span>登录</span>
                                </div>
                                <div v-for="o in 4" :key="o">
                                    {{'列表内容 ' + o }}
                                </div>
                                <el-button type="success" size="small" style="float: right; margin: 20px;" @click="login">确认</el-button>
                            </el-card>
                        </transition>
                        <transition name="el-zoom-in-center">
                            <el-card class="box-card" shadow="always" v-show="step==1?true:false">
                                <div slot="header">
                                    <span>文件上传</span>
                                </div>
                                <el-upload
                                class="upload-demo"
                                ref="upload"
                                action="https://jsonplaceholder.typicode.com/posts/"
                                :on-preview="handlePreview"
                                :on-remove="handleRemove"
                                :file-list="fileList"
                                :auto-upload="false">
                                <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                                <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
                                <div slot="tip" class="el-upload__tip">上传说明</div>
                                </el-upload>
                                <el-button type="success" size="small" style="float: right; margin: 20px;">确认</el-button>
                            </el-card>
                        </transition>
                        <transition name="el-zoom-in-center">
                            <el-card class="box-card" shadow="always" v-show="step==2?true:false">
                                <div slot="header">
                                    <span>开始上报</span>
                                </div>
                                <div>
                                    客户信息：XXX客户
                                </div>
                                <el-button type="success" size="small" style="float: right; margin: 20px;">确认</el-button>
                            </el-card>
                        </transition>
                        <transition name="el-zoom-in-center">
                            <el-card class="box-card" shadow="always" v-show="step==3?true:false">
                                <div slot="header">
                                    <span>确认完成</span>
                                </div>
                                <div>
                                    是否确认完成
                                </div>
                                <el-button type="success" size="small" style="float: right; margin: 20px;">确认</el-button>
                            </el-card>
                        </transition>
                        <transition name="el-zoom-in-center">
                            <el-card class="box-card" shadow="always" v-show="(step==4 || step==5)?true:false">
                                <div slot="header">
                                    <span>完成</span>
                                </div>
                                <div class="parent">
                                    <el-progress type="circle" :percentage="100" status="success"></el-progress>
                                </div>
                                <el-button type="success" size="small" style="float: right; margin: 20px;">确认</el-button>
                            </el-card>
                        </transition>
                    </el-col>
                </el-row>
            </el-main>
        </el-container>
   </div> 
</template>
<script>
import {loginPage} from '../../service/service';
export default {
  data () {
    return {
        step:0,
        fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}, {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}]
    }
    },
    methods: {
        async login(){
           let res = await loginPage.login({username:'yang',pwd:'123456'});
        },
        next(){
            if(this.step==5){
                return;
            }
            this.step++;
        },
        previous(){
            if(this.step==0){
                return;
            }
            this.step--;
        },
        submitUpload() {
            this.$refs.upload.submit();
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file) {
            console.log(file);
        }
    }
}
</script>
<style>
.selfhead{
    background:#eee;
    margin: 20px;
}
.box-card {
    width: 480px;
}
.parent {
    display: flex;
    justify-content:center;
    align-items: center;
}
</style>