<template>
  <div class="container">
    <form>
      <div class="well">
        <h4>Login Page</h4>

        <div class="form-group">
          <label class="pull-left"> Username </label>
          <input
            type="text"
            class="form-control"
            placeholder="Username"
            v-model="User.username"
            required
          />
        </div>
        <div class="form-group">
          <label class="pull-left"> Password </label>
          <input
            type="password"
            class="form-control"
            placeholder="Password "
            v-model="User.password"
            required
          />
        </div>
      </div>
      <button
        type="submit"
        class="btn btn-large btn-block btn-success full-width"
        @click="handleSubmit()"
      >
        Submit
      </button>
      <br />
      <router-link to="/accounts/signup">
        <button
          type="submit"
          class="btn btn-large btn-block btn-primary "
        >
          Signup
        </button>
      </router-link>
    </form>
  </div>
</template>

<script>
/*eslint-disable */
import axios from "axios";
import router from '../router';
export default {
  // name: 'login',
  
  data() {
    return {
      User: {
        // name: "",
        username: "",
        password: "",
       
      },
      submitted: false,
    };
  },
  methods: {
    handleSubmit() {
      this.submitted = true;
    
      // stop here if form is invalid
      let newUser = {
        // name: this.User.name,
        username: this.User.username,
        password: this.User.password
      };
      console.log(newUser);
      axios
        //.post("http://127.0.0.1:5000/accounts/login", newUser)
        .post(" https://4fiu4yvg7j.execute-api.us-east-2.amazonaws.com/Development/login", newUser).catch(()=>{})
        .then((response) => {
          console.log(response);
          router.push({ name: 'accountdetails' ,
          params:{username:newUser.username}
          })
        })
        .catch((error) => {
          console.log(error.response);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h2 {
  font-weight: normal;
}
form{
  width: 800px;
  height: 100px;
  padding-left: 250px;-.
  box-sizing: border-box;
}
</style>