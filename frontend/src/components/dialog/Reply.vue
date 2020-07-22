<template>
  <div class="mx-auto">
    <p>Reply:</p>
    <p class="form-error mx-auto">{{ errors[0] }}</p>
    <input v-model="message" type="text" />
    <button class="btn btn-reply" @click="onSubmit">Reply</button>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Reply",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data: () => ({
    errors: [],
    message: "",
  }),
  methods: {
    ...mapActions("dialog", ["fetchReplyDialog"]),
    checkReplyField() {
      this.errors = [];
      if (this.message) {
        return true;
      } else {
        this.errors.push("This field may not be blank");
        return false;
      }
    },
    onSubmit() {
      if (this.checkReplyField()) {
        const data = {
          dialog: this.id,
          message: this.message,
        };
        // console.log(data)
        this.fetchReplyDialog(data);
        this.message = "";
      }
    },
  },
};
</script>

<style scoped>
.btn-reply {
  margin-left: 2px;
  border: rgba(32, 32, 32, 0.719) solid 3px;
}
.btn-reply:hover {
  border: rgba(0, 0, 0, 0.719) solid 3px;
  /* font-size: x-large; */
  background: rgba(102, 102, 102, 0.459);
  font-weight: bold;
  color: rgba(252, 252, 252, 0.829);
}
.form-error {
  font-size: x-large;
  font-weight: bold;
  color: rgb(2, 2, 2);
}
</style>
