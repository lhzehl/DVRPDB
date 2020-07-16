<template>
  <div>
    {{ posts }}
  </div>
</template>

<script>
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "PostListFiltered",
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },
  // computed: {
  //   ...mapGetters("posts", [
  //     "paramsPosts",
  //     "paramsCountPost",
  //     "paramsCurrentPage",
  //     "perPage",
  //   ]),
  // isExist() {
  //   return Boolean(this.posts.length);
  // },

  // watch: {
  //   "$route.params": {
  //     handler: "onProfileParamsChange",
  //     immediate: true,
  //     depp: true,
  //   },
  // },
  // methods: {
  //   ...mapActions("posts", ["fetchPostsByParams"]),
  //   onProfileParamsChange({ params = this.params } = {}) {
  //     console.log(this.params);
  //     this.fetchPostsByParams(params);
  //   },
  // },
};
</script>

<style scoped></style>
