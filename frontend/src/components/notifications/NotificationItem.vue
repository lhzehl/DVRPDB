<template>
  <div class="row mt-2 notify-item">
    <!-- {{notification}} -->
    <div class="col-4">
      <router-link class="user-link" :to="userLink">{{
        notification.actions.by_user.username
      }}</router-link>
    </div>
    <div class="col-4">
      <router-link class="post-link" :to="postLink">{{
        notification.actions.action
      }}</router-link>
    </div>
    <div class="col-4">
      <p>{{ dateAdd }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotificationItem",
  props: {
    notification: {
      type: Object,
      required: true,
    },
  },
  computed: {
    dateAdd() {
      return new Date(this.notification.actions.date_add);
    },
    userLink() {
      return `/users/profile/${this.notification.actions.by_user.id}`;
    },
    postLink() {
      return `/post/${this.notification.actions.post_id}`;
    },
  },
  methods: {
    //   showAction(){
    //       console.log(this.notification)
    //   }
  },
};
</script>

<style scoped>
.notify-item {
  border: rgb(3, 3, 3) 2px solid;
}
.user-link {
  color: rgb(0, 0, 0);
  font-size: large;
  font-weight: bolder;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.post-link {
  color: rgba(0, 0, 0, 0.774);
  font-size: medium;
  font-weight: bolder;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
</style>
