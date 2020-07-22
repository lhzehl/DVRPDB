<template>
  <div class="container">
    <div class="row">
      <p class="form-error mx-auto">{{ errors[0] }}</p>
    </div>
    <div class="row mx-auto">
      <div class="col-6">
        <p class="mt-2">Title:</p>
        <p class="mt-2">descriptions:</p>
        <p class="mt-2">category:</p>
        <p class="mt-2">image:</p>
      </div>
      <div class="col-6">
        <input
          v-model="form.title"
          type="text"
          name="title"
          id="post-title"
          class="mt-2"
        />
        <br />
        <input
          v-model="form.descriptions"
          type="text"
          name="descriptions"
          id="post-descriptions"
          class="mt-2"
        /><br />
        <select class="mt-2" v-model="form.category">
            <option>Chose category</option>
            <option   :value="category.id"  v-for="category in categoryList" :key="category.title" >{{category.title}}</option>
        </select>
        <img class="post-image mt-2" :src="imagePreview" />
        <input
          type="file"
          ref="file"
          id="photo"
          class="mt-2"
          accept="image/*"
          v-on:change="handleFileUpload()"
        />
      </div>
      <div class="mx-auto mt-2">
        <a class="btn-post " @click="onSubmit">Post</a>
        <router-link class="btn-post" to="/">Cancel</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "PostCreate",
  data: () => ({
    form: {
      title: "",
      descriptions: "",
      image: null,
      category: null,
    },
    errors: [],
    imagePreview: "",
  }),
  computed: {
    ...mapGetters("category", ["categoryList"]),
  },
  methods: {
    ...mapActions("posts", ["fetchNewPost"]),
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
    checkForm() {
      this.errors = [];
      if (this.form.title && this.form.descriptions) {
        return true;
      } else {
        if (!this.form.title) {
          this.errors.push("title is requered");
        }
        if (!this.form.descriptions) {
          this.errors.push("description is required");
        }
        console.log(this.errors);
        return false;
      }
    },
    onSubmit() {
      if (this.checkForm()) {
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
        // console.log(this.form.category)
        // console.log(formFiltered)
        this.fetchNewPost(formFiltered);
      }
    },
  },
};
</script>

<style scoped>
.form-error {
  font-size: x-large;
  font-weight: bold;
  color: rgb(0, 0, 0);
}
.btn-post{
  border-radius: 15px;
  font-size: x-large;
  border: 4px solid black;
  font-family: Arial, Helvetica, sans-serif;
  color: black;
  /* height: 12px */
}
.btn-post:hover{
  color: black;
  font-size: xx-large;
  font-weight: bold;
}
.post-image{
  max-width: 300px;
  max-height: 300px;
  border: 3px black solid;
  filter: grayscale(100%);

}
</style>
