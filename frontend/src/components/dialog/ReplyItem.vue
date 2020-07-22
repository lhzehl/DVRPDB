<template>
  <div>
    <div class="row  mt-4">
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
    <div class="row">
      <!-- <div class="col-8"></div>
      <div class="col-4"> -->
      <!-- <router-link :to="detail">View</router-link> -->
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "ReplyItem",
  props: {
    dialog: {
      type: Object,
      required: true,
    },
  },
  computed: {
    routeToSender() {
      return `/users/profile/${this.dialog.sender.id}`;
    },
  },
};
</script>

<style scoped>
.item {
  border: rgba(0, 0, 0, 0.671) 2px solid;
  border-radius: 10px;
}
.profile-pic {
  width: 150px;
  height: 150px;
  border-radius: 35px;
  border: rgba(0, 0, 0, 0.671) 2px solid;
}
.route-text {
  color: black;
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
