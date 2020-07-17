<template>
  <div>
    <b-card bg-variant="light" class="auth-form mx-auto">
      <!-- <b-form-group
        label-cols-lg="3"
        label="Registration"
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mx-auto"
      > -->
      <p class="reg">Registration</p>
      <p class="err-reg">{{ errRegMail }}</p>
      <p class="is-created">{{ isCreated }}</p>
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
      <p class="err-reg">{{ errRegPass }}</p>
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
      <router-link to="/authorization" class="btn btn-submit mr-3"
        >SingIn</router-link
      >
      <button class="btn btn-submit" v-on:click="logInFormSubmit">
        Submit
      </button>
    </b-card>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Authorization",
  data: () => ({
    email: "",
    password: "",
  }),
  mounted() {
    var self = this;
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
    ...mapActions("auth", ["fetchNewUser"]),
    logInFormSubmit() {
      console.log(this.email, this.password);
      let data = {
        email: this.email,
        password: this.password,
      };
      this.fetchNewUser(data);
    },
  },
  computed: {
    ...mapGetters("auth", ["errRegMail", "errRegPass", "isCreated"]),
  },
};
</script>

<style scoped>
.auth-form {
  min-width: 50%;

  margin-top: 5rem;
  /* margin-left: 10rem; */
  /* margin-right: 10rem; */
}
.btn-submit {
  border: solid rgba(70, 131, 180, 0.322);
}
.btn-submit:hover {
  border: solid 4px slateblue !important;
  color: rgb(15, 23, 31);
  font-weight: bold;
}
.err-reg {
  color: red;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: bold;
  font-size: large;
}
.is-created {
  color: royalblue;
  font-family: "Times New Roman", Times, serif;
  font-weight: bold;
  font-size: x-large;
}
.reg {
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
