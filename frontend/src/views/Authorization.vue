<template>
  <div>
    <b-card bg-variant="light" class="auth-form mx-auto">
      <!-- <b-form-group
        label-cols-lg="3"
        label="Log In"
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0"
      > -->
      <p class="login">Log In</p>
      <p class="err-auth">{{ errLogin }}</p>
      <b-form-group
        label-cols-sm="3"
        label="Email:"
        label-align-sm="right"
        label-for="email-input"
      >
        <b-form-input
          v-model="email"
          type="email"
          id="email-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Password:"
        label-align-sm="right"
        label-for="password-input"
      >
        <b-form-input
          v-model="password"
          type="password"
          id="password-input"
        ></b-form-input>
      </b-form-group>
      <!-- </b-form-group> -->
      <router-link to="/registration" class="btn btn-submit mr-3"
        >Register</router-link
      >
      <button class="btn btn-submit" v-on:click="logInFormSubmit">LogIn</button>
    </b-card>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Registration",
  data: () => ({
    email: "",
    password: "",
  }),
  mounted() {
    var self = this
    const pass = document.querySelector("#password-input");
    const mail = document.querySelector("#email-input");
    function submit(event) {
      // console.log(event)
      if (event.keyCode === 13) {
        self.logInFormSubmit();
      }
    }
    pass.addEventListener("keydown", submit);
    mail.addEventListener("keydown", submit);
  },
  methods: {
    ...mapActions("auth", ["fetchLogin"]),
    logInFormSubmit() {
      let data = {
        email: this.email,
        password: this.password,
      };
      this.fetchLogin(data);
    },
  },
  computed: {
    ...mapGetters("auth", ["errLogin"]),
  },
};
</script>

<style scoped>
.auth-form {
  min-width: 50%;

  margin-top: 5rem;
}
.login {
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
.btn-submit {
  border: solid rgba(70, 131, 180, 0.322);
}
.btn-submit:hover {
  border: solid 4px slateblue !important;
  color: rgb(15, 23, 31);
  font-weight: bold;
}
.err-auth {
  color: red;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: bold;
  font-size: large;
}
</style>
