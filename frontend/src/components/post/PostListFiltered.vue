<template>
  <div class="post-list">

    <p>{{localedate}}</p>
    <router-link class="route-text" :to="detail">{{ post.title }} </router-link>
    <p>{{ shortDetail }}</p>
    
  </div>
</template>

<script>
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "PostListFiltered",
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  computed: {
    localedate() {
      return new Date(this.post.date_create).toLocaleDateString();
    },
    detail() {
      // console.log(this.post.id)
      return `/post/${this.post.id}`;
    },
    shortDetail() {
      if (this.post.descriptions.length > 250) {
        return `${this.post.descriptions.slice(0, 250)} .....`;
      } else {
        return this.post.descriptions;
      }
    },
  },
};
</script>

<style scoped>
.post-list{
  border: 2px solid rgba(41, 44, 43, 0.822);
}
.route-text {
  color: black;
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
