<template>
  <div class="container">
    <button class="btn btn-success" v-if="!edited" @click="edited = !edited">
      Edit
    </button>
    <template v-if="!edited">
      <div class="row">
        <div class="col-6">
          <p class="mt-2">Name:</p>
          <p class="mt-2">Username:</p>
          <p class="mt-2">DOB:</p>
          <p class="mt-2">Photo:</p>
        </div>
        <div class="col-6">
          <p class="mt-2">{{ profile.name || "null" }}</p>
          <p class="mt-2">{{ profile.username || "" }}</p>
          <p class="mt-2">{{ localeDate }}</p>
          <img :src="profile.image" />
        </div>
      </div>
    </template>
    <template v-if="edited">
      <div class="row">
        <div class="col-6">
          <p class="mt-2">Name:</p>
          <p class="mt-2">Username:</p>
          <p class="mt-2">BOD:</p>
          <p class="mt-2">Photo:</p>
        </div>
        <div class="col-6">
          <input class="mt-2" type="text" v-model="form.name" /> <br>
          <input class="mt-2" type="text" v-model="form.username" /> <br>
          <b-form-datepicker class="mt-2"
            id="example-datepicker"
            v-model="form.dob"
          ></b-form-datepicker> <br>
          <img class="profile-image mt-2" :src="imagePreview" /> <br>
          <input
          class="mt-2"
            type="file"
            ref="file"
            id="photo"
            accept="image/*"
            v-on:change="handleFileUpload()"
          /> <br>
        </div>
      </div>
      <button class="btn btn-primary" @click="onSubmit">Save</button>
      <button class="btn" @click="edited = !edited">Cancel</button>
    </template>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "AuthProfile",
  props: {
    profile: {
      type: Object,
      requered: true,
    },
  },
  data() {
    return {
      edited: false,
      form: {
        name: this.profile.name,
        username: this.profile.username,
        dob: this.profile.dob,
        image: null,
        id: this.profile.id,
      },
      imagePreview: "",
    };
  },
  computed: {
    localeDate() {
      return new Date(this.profile.dob).toLocaleDateString();
    },
  },
  methods: {
    ...mapActions("profile", ["fetchUpdateProfile"]),
    handleFileUpload() {
      this.form.image = this.$refs.file.files[0];
      const reader = new FileReader();
      reader.addEventListener(
        "load",
        function() {
          this.imagePreview = reader.result;
        }.bind(this),
        false
      );
      if (this.form.image) {
        if (/\.(jpe?g|png|gif)$/i.test(this.form.image.name)) {
          reader.readAsDataURL(this.form.image);
        }
      }
    },
    onSubmit(e) {
      e.preventDefault();
      Object.filter = function(obj, filtercheck) {
        let result = {};
        Object.keys(obj).forEach((key) => {
          if (filtercheck(obj[key])) result[key] = obj[key];
        });
        return result;
      };
      const filterFunc = function(val) {
        return Boolean(val);
      };
      const formFiltered = Object.filter(this.form, filterFunc);

      this.fetchUpdateProfile(formFiltered);

      this.edited = false;
    },
  },
};
</script>

<style scoped>
.profile-image {
  width: 200px;
  height: 200px;
  border: 2px solid black;
}
</style>
