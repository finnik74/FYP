import VueRouter from "vue-router";
import login from "@/pages/Login_Page";
import bayLIME_Homepage from "@/pages/BayLIME_Homepage";
import No_suchpage from "@/pages/No_suchpage";


export default new VueRouter({
    routes:[

        {
            path:'/login',
            component:login,

        },
        {
            path:'/',
            component:bayLIME_Homepage,

        },
        {
            path:'*',
            component:No_suchpage,

        },

    ],
    mode:'history',
})


