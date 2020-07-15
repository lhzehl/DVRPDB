<template>
  <div>
    <div class="row">
      <div class="col-6 p-left">
        <p v-if="profile.name">Name:</p>
        <p class="mt-2 p-left">Username:</p>
        <p class="mt-2 p-left">DOB:</p>
        <p class="mt-2 p-left">Photo:</p>
        <button v-if="isLogin&&!isOwn"
          class="mess mx-auto"
          @click="startDialog = true"
        >
          Send Message
        </button>
      </div>
      <div class="col-6 p-right">
        <p v-if="profile.name" class="mt-2">{{ profile.name }}</p>
        <p class="mt-2 p-right">{{ profile.username || "" }}</p>
        <p class="mt-2 p-right">{{ localeDate }}</p>
        <img class="mt-2 profile-image" :src="profile.image" />
      </div>
    </div>

    <div class="dialog mt-5 mx-auto" v-if="startDialog">
      <p class="form-error mx-auto">{{ errors[0] }}</p> <br>
      <input v-model="message" class="mx-auto" type="text" /><br />
      <button class="mess" @click="SendMessage">Send Message</button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "UsersProfile",
  props: {
    profile: {
      type: Object,
      required: true,
    },
  },
  data: () => ({
    errors: [],
    startDialog: false,
    message: "",
  }),
  computed: {
    ...mapGetters('auth', ['isLogin']),
    ...mapGetters('profile',['ownProfile']),
    localeDate() {
      return new Date(this.profile.dob).toLocaleDateString();
    },
    isOwn(){
      return this.ownProfile.id === this.profile.id
    }
  },
  methods: {
    ...mapActions("dialog", ["fetchStartDialog"]),
    checkMessageField() {
      this.errors = [];
      if (this.message) {
        return true;
      } else {
        this.errors.push("This field may not be blank");
        return false;
      }
    },
    SendMessage() {
      if (this.checkMessageField()) {
        const data = {
          message: this.message,
          recipient: this.profile.id,
        };
        this.startDialog = false
        // console.log(this.isOwn, data)
        this.fetchStartDialog(data)
      }

      // console.log(data);
    },
  },
};
</script>

<style scoped>
.profile-image {
  border-radius: 5rem;
  max-width: 200px;
}
.p-left {
  border: solid 2px steelblue;
}
.p-right {
  border: solid 2px steelblue;
}
.mess {
  color: rgba(34, 21, 2, 0.877);
  font-size: large;
  font-weight: bold;
  font-family: "Times New Roman", Times, serif;
  border: solid 3px rgba(158, 70, 180, 0.788);
  max-width: 100%;
  background: rgba(222, 184, 135, 0.555);
  /* bottom: 0px; */
  /* right: 185px; */
  /* position: absolute; */
  border-radius: 5px;
}
.mess:hover {
  background: rgba(196, 83, 7, 0.829);
  color: aliceblue;
  border: solid 4px rgb(104, 43, 3);
}
.dialog {
  position: relative;
  border: solid 2px steelblue;
  max-width: 80%;
  max-height: 500px;
  min-height: 100px;
}
.form-error {
  font-size: x-large;
  font-weight: bold;
  color: tomato;
}
</style>
