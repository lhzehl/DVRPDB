<template>
  <div>
    <div class="row">
      <div class="col-6 p-left">
        <p v-if="profile.name">Name:</p>
        <p class="mt-2 p-left">Username:</p>
        <p class="mt-2 p-left">DOB:</p>
        <p class="mt-2 p-left">Photo:</p>

        <div v-if="isLogin && !isOwn">
          <button class="mess mx-auto mt-2" @click="startDialog = true">
            Send Message
          </button>
          <button class="mess mx-auto mt-2" @click="Subscribe">
            Subscribe
          </button>
        </div>
      </div>
      <div class="col-6 p-right">
        <p v-if="profile.name" class="mt-2">{{ profile.name }}</p>
        <p class="mt-2 p-right">{{ profile.username || "" }}</p>
        <p class="mt-2 p-right">{{ localeDate }}</p>
        <img class="mt-2 profile-image" :src="profile.image" />
      </div>
    </div>

    <div class="dialog mt-5 mx-auto" v-if="startDialog">
      <p class="form-error mx-auto">{{ errors[0] }}</p>
      <br />
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
    ...mapGetters("auth", ["isLogin"]),
    ...mapGetters("profile", ["ownProfile"]),
    localeDate() {
      return new Date(this.profile.dob).toLocaleDateString();
    },
    isOwn() {
      return this.ownProfile.id === this.profile.id;
    },
  },
  methods: {
    ...mapActions("dialog", ["fetchStartDialog"]),
    ...mapActions("notifications", ["fetchSubscribeForUser"]),

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
        this.startDialog = false;

        this.fetchStartDialog(data);
      }
    },
    Subscribe() {
      this.fetchSubscribeForUser(this.profile.id);
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
  border: solid 2px rgb(2, 2, 2);
}
.p-right {
  border: solid 2px rgb(0, 0, 0);
}
.mess {
  color: rgba(34, 21, 2, 0.877);
  font-size: large;
  font-weight: bold;
  font-family: "Times New Roman", Times, serif;
  border: solid 3px rgba(37, 37, 37, 0.788);
  max-width: 100%;
  background: rgba(212, 212, 212, 0.555);

  border-radius: 5px;
}
.mess:hover {
  background: rgba(255, 255, 255, 0.829);
  color: rgb(0, 0, 0);
  border: solid 4px rgb(0, 0, 0);
}
.dialog {
  position: relative;
  border: solid 2px rgb(0, 0, 0);
  max-width: 80%;
  max-height: 500px;
  min-height: 100px;
}
.form-error {
  font-size: x-large;
  font-weight: bold;
  color: rgb(0, 0, 0);
}
</style>
