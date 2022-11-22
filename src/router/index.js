//引入vue-router
import VueRouter from "vue-router";
//引入需要路由的组件

import HomePage from "@/pages/HomePage";
import kitchen_main from "@/pages/Kitchen_main";
import login from "@/pages/Login_Page";
import test from "@/pages/test"
import bayLIME_Homepage from "@/pages/BayLIME_Homepage";
import No_suchpage from "@/pages/No_suchpage";
//创建并暴露VueRouter
export default new VueRouter({
    routes:[

        {
            //跳转路由的路径和跳转到的组件
            path:'/',
            component:HomePage,

        },
        {
            //跳转路由的路径和跳转到的组件
            path:'/kitchen',
            component:kitchen_main,

        },
        {
            //跳转路由的路径和跳转到的组件
            path:'/login',
            component:login,

        },
        {
            //跳转路由的路径和跳转到的组件
            path:'/test',
            component:test,

        },
        {
            //跳转路由的路径和跳转到的组件
            path:'/BayLIME',
            component:bayLIME_Homepage,

        },
        {
            //跳转路由的路径和跳转到的组件
            path:'*',
            component:No_suchpage,

        },

    ],

    mode:'history',


})


