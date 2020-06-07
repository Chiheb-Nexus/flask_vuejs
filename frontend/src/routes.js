
import Home from './components/Home.vue'
import FirstExample from './components/FirstExample.vue'
import SecondExample from './components/SecondExample.vue'
import ThirdExample from './components/ThirdExample.vue'


const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/first-example',
        name: 'first-example',
        component: FirstExample
    },
    {
        path: '/second-example',
        name: 'second-example',
        component: SecondExample
    },
    {
        path: '/third-example',
        name: 'third-example',
        component: ThirdExample
    }
]
export default routes;