<template>
  <div class="post-list">

    <p>{{localedate}}</p>
    <router-link :to="detail">{{ post.title }} </router-link>
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
  border: 2px solid rgba(2, 54, 37, 0.822);
}

</style>
