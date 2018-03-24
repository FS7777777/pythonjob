<template>
    <div class="layout">
        <Row type="flex">
            <Col span="5" class="layout-menu-left">
                <Menu active-name="1-2" theme="dark" width="auto" :open-names="['1']">
                    <div class="layout-logo-left"></div>
                    <Submenu name="1">
                        <template slot="title">
                            <Icon type="ios-navigate"></Icon>
                            导航一
                        </template>
                        <MenuItem name="1-1">选项 1</MenuItem>
                        <MenuItem name="1-2">选项 2</MenuItem>
                        <MenuItem name="1-3">选项 3</MenuItem>
                    </Submenu>
                    <Submenu name="2">
                        <template slot="title">
                            <Icon type="ios-keypad"></Icon>
                            导航二
                        </template>
                        <MenuItem name="2-1">选项 1</MenuItem>
                        <MenuItem name="2-2">选项 2</MenuItem>
                    </Submenu>
                    <Submenu name="3">
                        <template slot="title">
                            <Icon type="ios-analytics"></Icon>
                            导航三
                        </template>
                        <MenuItem name="3-1">选项 1</MenuItem>
                        <MenuItem name="3-2">选项 2</MenuItem>
                    </Submenu>
                </Menu>
            </Col>
            <Col span="19">
                <div class="layout-header">
                    <Row>
                        <Col span="10">
                            <div class="main-search">
                                <Input  placeholder="请输入...">
                                    <Button  slot="append" icon="ios-search"></Button>
                                </Input>
                            </div>
                        </Col>
                        <Col span="8"><a style="line-height: 60px;">export</a></Col>
                        <Col span="6">                    
                            <div class="demo-avatar-badge">
                                <Badge count="1">
                                    <Avatar shape="square" icon="person" size="large"/>
                                </Badge>
                            </div>
                        </Col>
                    </Row>

                </div>
                <div class="layout-breadcrumb">
                    <Breadcrumb>
                        <BreadcrumbItem href="#">首页</BreadcrumbItem>
                        <BreadcrumbItem href="#">应用中心</BreadcrumbItem>
                        <BreadcrumbItem>某应用</BreadcrumbItem>
                    </Breadcrumb>
                </div>
                <div class="layout-content">
                    <!-- <router-view class="layout-content-main">内容区域</router-view> -->
                    <div class="btn-group" role="group" aria-label="...">  
      <button type="button" class="btn btn-default">Left</button>  
      <button type="button" class="btn btn-default">Middle</button>  
      <button type="button" class="btn btn-default">Right</button>  
    </div>
                </div>
                <div class="layout-copy">
                    2011-2017 &copy; TalkingData
                </div>
            </Col>
        </Row>
    </div>
</template>
<script>
$(function () {  
    alert(123);  
 }); 
    export default {
        
    }
</script>
<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
    }
    .layout-breadcrumb{
        padding: 10px 15px 0;
    }
    .layout-content{
        min-height: 200px;
        margin: 15px;
        overflow: hidden;
        background: #fff;
        border-radius: 4px;
    }
    .layout-content-main{
        padding: 10px;
    }
    .layout-copy{
        text-align: center;
        padding: 10px 0 20px;
        color: #9ea7b4;
    }
    .layout-menu-left{
        background: #464c5b;
    }
    .layout-header{
        height: 60px;
        background: #fff;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
    }
    .layout-logo-left{
        width: 90%;
        height: 40px;
        background: #5b6270;
        border-radius: 3px;
        margin: 15px auto;
        background-image:url(../../../static/img/baron.png);
    }
    .demo-avatar-badge{
        width: 100px;
        height: 60px;
        line-height: 60px;
        float: right;
    }
    .main-search{
        padding: 10px 10px;
        top:50%;
    }
</style>