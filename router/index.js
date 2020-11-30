import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import Register from '@/components/register'
import Loan from '@/components/loan'
import ViewLoans from '@/components/ViewLoans'
import Accounts from '@/components/accountdetails'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/accounts/signup',
      component: Register
    },
    {
      path: '/accounts/loans',
      name: 'Loan',
      component: Loan
    },
    {
      path: '/accounts/showloans/:username',
      name: 'ViewLoans',
      component: ViewLoans
    },
    {
      path: '/accounts/login',
      name: 'accountdetails',
      component: Accounts
    }
  ]
})
