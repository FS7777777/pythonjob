import request from '../../requests/request';

export const loginPage = {
    login: param => request.post('/auth/login', param),
};

export const headerMenuPage = {
    //登陆
    getMenuList: () => request.get('/manager/getManagerMenu'),
    //退出登录
    exitSys: () => request.get('/manager/exit'),
    //修改密码
    updatePassword: param => request.post('/manager/updatePassword', param)
};