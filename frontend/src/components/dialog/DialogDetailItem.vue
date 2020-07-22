<template>
  <div>

    <div class="container mt-2">
      <div class="row">
        <div class="col-4 item">
          <router-link class="mx-auto mb-2 route-text" :to="routeToSender">{{
            dialog.sender.username
          }}</router-link>
          <br />
          <img :src="dialog.sender.image" class="profile-pic" />
        </div>
        <div class="col-8 item">
          <p>{{ dialog.message }}</p>
        </div>
      </div>
      <template v-if="ifReplysIsExist"> 
          <ReplyList :reply="dialog.reply" />
      </template>

    <Reply :id="dialog.id" />

    </div>
  </div>
</template>

<script>
import Reply from "@/components/dialog/Reply"
import ReplyList from "@/components/dialog/ReplyList";
export default {
  name: "DialogDetailItem",
  props: {
    dialog: {
      type: Object,
      required: true,
    },
  },
  components: {
    ReplyList,
    Reply,
  },
  computed: {
    ifReplysIsExist() {
      return Boolean(this.dialog.reply.length);
    },
    routeToSender() {
      return `/users/profile/${this.dialog.sender.id}`;
    },
  },
};
</script>

<style scoped>
.item {
  border: rgb(8, 8, 8) 2px solid;
}
.profile-pic {
  width: 150px;
  height: 150px;
  border-radius: 35px;
  border: rgb(5, 5, 5) 2px solid;
}
.route-text {
  color: black;
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
