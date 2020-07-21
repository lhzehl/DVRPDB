<template>
  <div>
    <div class="row  mt-5 ">
      <p class="head mx-auto">Add new category:</p>
      <p class="form-error mx-auto">{{ error }}</p>
      <p class="form-success mx-auto">{{ isCreated }}</p>
    </div>
    <div class="row add-block">
      <div class="col-3">
        <p class="mt-1">title</p>
        <p class="mt-1">description</p>
      </div>
      <div class="col-8">
        <input v-model="category.title" class="mr-1 mt-1" type="text" /><br />
        <input
          v-model="category.description"
          class="mr-1 mt-1"
          type="text"
        /><br />
      </div>
    </div>
    <div class="row">
      <button class="ml-auto" @click="Cancel">Cancel</button>
      <button class="mr-auto" @click="addCategory">ADD</button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "CategoryCreate",
  data: () => ({
    category: {
      title: "",
      description: "",
    },
    error: "",
  }),
  computed: {
    ...mapGetters("category", ["isCreated"]),
  },
  methods: {
    ...mapActions("category", ["fetchNewCategory"]),
    addCategory(e) {
      e.preventDefault();
      this.error = "";
      if (!this.category.title) {
        this.error = "title is required";
      } else {
        this.fetchNewCategory(this.category);
      }
    },
    Cancel() {
      this.$emit("cancel");
    },
  },
};
</script>
<style scoped>
.form-error {
  font-size: x-large;
  font-weight: bold;
  color: tomato;
}
.form-success {
  font-size: x-large;
  font-weight: bold;
  color: rgba(33, 3, 202, 0.815);
}
.head {
  font-family: "Times New Roman", Times, serif;
  font-size: x-large;
  font-weight: bold;
}
</style>
