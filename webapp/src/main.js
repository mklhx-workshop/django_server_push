import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'
import vuetify from '@/plugins/vuetify' // path to vuetify export

const app = createApp(App).use(router)
app.use(router, vuetify)
app.mount('#app')