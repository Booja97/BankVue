<template>
    <div class="hello">
      <h1>{{ msg }}</h1>
    <router-link to="/accounts/loans">
        <button  type="submit"  class="btn-loan" >  Add Loan</button>
      </router-link>
    <router-link to="/">
        <button class="btn-logout">  logout</button>
      </router-link>
        <table v-if="IsLoanAvailable" border=1 class="center">
            <thead>
                <tr>
                <th>UserName</th>
                <th>LoanType</th>
                <th>LoanAmount (INR)</th>
                <th>Date</th>
                <th>Rate of Interest</th>
                <th>Duration Of Loan</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(loan,i) in Loan" :key="i">
                <td>{{loan.username}}</td>
                <td>{{loan.loan_type}}</td>
                <td>INR:{{loan.loan_Amount}}</td>
                <td>{{loan.date}}</td>
                <td>{{loan.rate_of_interest}}</td>
                <td>{{loan.duration_of_loan}}year</td>
                </tr>
            </tbody>
    </table>
     <div v-if="!IsLoanAvailable" style="text-align:left;margin-left:235px;">
        <h3 style="color:red;">No active loans at this moment to show!!!</h3>
      </div>
    </div>
</template>

<script>
/*eslint-disable*/
import axios from "axios";
import router from '../router';
export default {
  name: 'ViewLoans',
  data: function () {
    return {
      msg: 'Loan Details',
      username: this.$route.params.username,
      IsLoanAvailable:true,
      Loan: []
    }
  },
  methods: {
    getLoan (username) {
     // axios.get('http://127.0.0.1:5000/accounts/login/' + this.username + '/loans')
     axios.get(' https://4fiu4yvg7j.execute-api.us-east-2.amazonaws.com/Development/loan/' + this.username )
        .then(res => {
          if (res.data.length) {
            this.Loan = res.data
            console.log(this.Loan)
            router.push({
            params:{username:this.username}
          })
          }
          else{
              this.IsLoanAvailable = false
            }
         }, err => {
          console.log(err)
        })
    }
  },
  created: function(){
      this.getLoan()
    }
}
</script>
<style scoped>
.btn-logout{
  width: 100px;
  margin-right: 40px;
  float: right;
}​​
.btn-loan{
  width: 100px;
  margin-left: 800px;
  float: left;
}
.center {
  width: 500px;
  height: 150px;
  margin-right: 250px;
  margin-top: 70px;
  float: right;
  box-sizing: border-box;
}
</style>
