<template>
  <div class="container">
    <form>
      <div class="well">
        <h4>Registration</h4>
        <div class="form-group">
          <label class="pull-left"> Username </label>
          <input type="text" class="form-control" placeholder="Username" v-model="User.username" required minlength="6" />
        </div>
        <div class="form-group">
          <label class="pull-left"> Password </label>
          <input type="password" class="form-control" placeholder="Password " v-model="User.password" required minlength="6" />
        </div>
        <div class="form-group">
          <label class="pull-left"> Address </label>
          <input type="text" class="form-control" placeholder="Address " v-model="User.address" required />
        </div>
        <div class="form-group">
          <label class="pull-left"> State </label>
          <input type="text" class="form-control" placeholder="State " v-model="User.state" required />
        </div>
        <div class="form-group">
          <label class="pull-left"> Country </label>
          <input type="text" class="form-control" placeholder="Country " v-model="User.country" required />
        </div>
        <div class="form-group">
          <label class="pull-left"> Email Address </label>
          <input type="email" class="form-control" placeholder="Email " v-model="User.emailAddress" required />
        </div>
        <div class="form-group">
          <label class="pull-left"> PAN </label>
          <input type="text" class="form-control" placeholder="PAN number " v-model="User.pan" required minlength="6" maxlength="10" />
        </div>
        <div class="form-group">
          <label class="pull-left"> Contact Number </label>
          <input type="text" class="form-control" placeholder="Contact " v-model="User.contactNo" required minlength="10" maxlength="12" />
        </div>
        <div class="form-group">
          <label class="pull-left"> Date of birth </label>
          <input type="date" class="form-control" placeholder="Date of birth " v-model="User.dob" required />
        </div>
        <div class="form-group">
          <label class="pull-left"> Account Type </label>
          <input type="text" class="form-control" placeholder="Account type " v-model="User.accountType" required />
        </div>
      </div>
      <button type="submit" class="btn btn-md btn-success" @click="addToAPI">Submit</button>
      <router-link to="/">
        <button class="btn btn-md btn-danger">Cancel</button>
      </router-link>
    </form>
  </div>
</template>
<script>
/*eslint-disable */
import axios from "axios";
import router from '../router';
export default {
  // name: 'Register',
  
  data() {
    return {
      User: {
        // name: "",
        username: "",
        password: "",
        address: "",
        state: "",
        country: "",
        emailAddress: "",
        pan: "",
        contactNo: "",
        dob: "",
        accountType: "",
      },
    };
  },
  methods: {
    addToAPI() {
      let newUser = {
        // name: this.User.name,
        username: this.User.username,
        password: this.User.password,
        address: this.User.address,
        state: this.User.state,
        country: this.User.country,
        email: this.User.emailAddress,
        pan: this.User.pan,
        contact: this.User.contactNo,
        dob: this.User.dob,
        accounttype: this.User.accountType,
      };
      console.log(newUser);
      axios
        //.post("http://127.0.0.1:5000/accounts/signup", newUser)
        .post("https://4fiu4yvg7j.execute-api.us-east-2.amazonaws.com/Development/users", newUser)
        .then((response) => {
          console.log(response);
          router.push({ name: 'Login' })
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
