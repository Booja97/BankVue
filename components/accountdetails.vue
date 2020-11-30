<template>
  <div v-if="currentUser"  class="edit-form">
    <h4>Account Details</h4>
    <router-link to="/">
        <button class="btn-logout">
        logout
      </button>
      </router-link>
    <form >
      <router-link :to="{ name: 'ViewLoans', params: { username: this.currentUser.username } }"><button class="btn-loan">{{this.currentUser.username}}-Loan</button></router-link>
      <div class="form-group">
        <label for="username">UserName</label>
        <input type="text" class="form-control" id="username" readonly="readonly"
          v-model="currentUser.username" required
            minlength=6
        />
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <input type="text" class="form-control" id="address"
          v-model="currentUser.address"
        />
      </div>
      <div class="form-group">
        <label for="state">State</label>
        <input type="text" class="form-control" id="state"
          v-model="currentUser.state"
        />
      </div>
      <div class="form-group">
        <label for="country">Country</label>
        <input type="text" class="form-control" id="country"
          v-model="currentUser.country"
        />
      </div>
      <div class="form-group">
        <label for="emailAddress">Email</label>
        <input type="email" class="form-control" id="emailAddress"
          v-model="currentUser.emailAddress"
        />
      </div>
      <div class="form-group">
        <label for="contactno">Contact No</label>
        <input type="number" class="form-control" id="contactno"
          v-model="currentUser.contactNo"
          required
        />
      </div>
    </form>

    <button type="submit" class="badge badge-success"
      @click="updateUser"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>
</template>
<script>
/* eslint-disable */
import axios from 'axios'
import router from '../router';
export default {
  name: 'user',
  data () {
    return {
      username: this.$route.params.username,
      currentUser: null,
      message: ''
    }
  },
  methods: {
    getUser () {
      axios
        //.get('http://127.0.0.1:5000/accounts/login/'+this.username)
        
        .then(response => {
          this.currentUser = response.data
          console.log(response.data)
          router.push({ 
          params:{username:this.username}
          })
        })
        .catch(e => {
          console.log(e)
        })
    },
    updateUser () {
       let User = {
        // name: this.currentUser.name,
        username: this.currentUser.username,
        password: this.currentUser.password,
        address: this.currentUser.address,
        state: this.currentUser.state,
        country: this.currentUser.country,
        emailAddress: this.currentUser.emailAddress,
        pan: this.currentUser.pan,
        contactNo: this.currentUser.contactNo,
        DOB: this.currentUser.dob,
        accountType: this.currentUser.accountType
      }
      console.log(this.currentUser)
      axios
        .put('http://127.0.0.1:5000/accounts/login/' + this.currentUser.username, User).catch(()=>{})
        .then(response => {
          console.log(response.data)
          this.message = 'User Details was updated successfully!'
        })
        .catch(e => {
          console.log(e)
          this.message = 'An error occured. Please read the exception message' +' - '+ e.message
        })
    }
  },
  mounted () {
    this.message = ''
    this.getUser(this.$route.params.username)
    router.push({ 
          params:{username:this.username}
          })
  }
}
</script>
<style scoped>
.btn-logout{
  width: 100px;
  margin-right: 40px;
  float: right;
}
.btn-loan{
  width: 200px;
  margin-right: 40px;
  float: right;
}
.form-group {
  width: 800px;
  height: 60px;
  padding-left: 450px;
  box-sizing: border-box;
}
</style>