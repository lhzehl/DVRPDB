<template>
  <div>
    <div class="row mx-auto">
      <div class="col-6">
        <p class="mt-2">Title:</p>
        <p class="mt-2">descriptions:</p>
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
      <div class="mx-auto">
        <button class="btn btn-warning" @click="onSubmit">Update</button>
        <button @click="cancel" class="btn btn-primary">
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "PostUpdate",
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      form: {
        title: this.post.title,
        descriptions: this.post.descriptions,
        image: null,
        id: this.post.id,
      },
      imagePreview: this.post.image,
    };
  },
  computed: {
    routeToPost() {
      return `/post/${this.post.id}`;
    },
  },
  methods: {
    ...mapActions("posts", ["fetchUpdatePost"]),
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

      this.fetchUpdatePost(formFiltered);
      this.$emit("cancel");
    },
    cancel() {
      this.$emit("cancel");
    },
  },
};
</script>

<style scoped>
.post-image {
  max-height: 400px;
  max-width: 400px;
}
</style>
