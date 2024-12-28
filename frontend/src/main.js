import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import DeviceList from './views/DeviceList.vue'
import axios from 'axios'

// API基础URL配置
axios.defaults.baseURL = 'http://localhost:8000/api/v1'

// 路由配置
const routes = [
    {
        path: '/',
        name: 'DeviceList',
        component: DeviceList
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

// 创建Vue应用
const app = createApp(App)

// 使用路由
app.use(router)

// 全局配置axios
app.config.globalProperties.$axios = axios

// 挂载应用
app.mount('#app')
