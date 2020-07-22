<template>
  <div>
    <div class="row item mt-4">
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
      <div class="col-8"></div>
      <div class="col-4">
        <router-link class="route-text" :to="detail">View</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DialogListItem",
  props: {
    dialog: {
      type: Object,
      required: true,
    },
  },
  computed: {
    detail() {
      // console.log(this.post.id)
      return `/dialog/${this.dialog.id}`;
    },
    routeToSender() {
      return `/users/profile/${this.dialog.sender.id}`;
    },
  },
};
</script>

<style scoped>
.item {
  border: rgb(5, 5, 5) 2px solid;
}
.profile-pic {
  width: 150px;
  height: 150px;
  border-radius: 35px;
  border: rgb(2, 2, 2) 2px solid;
}
.route-text {
  color: black;
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
