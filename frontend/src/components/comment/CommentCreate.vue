<template>
  <div class="mx-auto">
    <p>Comment:</p>
    <p class="form-error mx-auto">{{ errors[0] }}</p>
    <input v-model="text" type="text" />
    <button class="btn btn-comment" @click="onSubmit">Comment</button>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "CommentCreate",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data: () => ({
    errors: [],
    text: "",
  }),
  methods: {
    ...mapActions("posts", ["fetchNewComment"]),
    checkCommentField() {
      this.errors = [];
      if (this.text) {
        return true;
      } else {
        this.errors.push("This field may not be blank");
        return false;
      }
    },
    onSubmit() {
      if (this.checkCommentField()) {
        const data = {
          post: this.id,
          text: this.text,
        };
        
        this.fetchNewComment(data);
      }
    },
  },
};
</script>

<style scoped>
.btn-comment {
  margin-left: 2px;
  border: rgba(7, 70, 63, 0.719) solid 3px;
}
.btn-comment:hover {
  border: rgba(18, 12, 109, 0.719) solid 3px;
  /* font-size: x-large; */
  background: rgba(0, 0, 255, 0.459);
  font-weight: bold;
  color: rgba(252, 252, 252, 0.829);
}
.form-error {
  font-size: x-large;
  font-weight: bold;
  color: tomato;
}
</style>
