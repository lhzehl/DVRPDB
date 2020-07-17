<template>
  <div>
    <template v-if="userProfile.username">
      <UsersProfile :profile="userProfile" />
    </template>
    <div v-if="isExist" class="mt-5">
      <p class="u-posts">USER POSTS</p>
      <div v-for="post in paramsPosts" :key="post.date_create">
        <PostListFiltered :post="post" />
      </div>
      <div v-if="paramsCountPost">
        <Pagination
          :count="paramsCountPost"
          :current-page="paramsCurrentPage"
          :per-page="perPage"
          @pageChanged="onPageChange"
        />
      </div>
    </div>
  </div>
</template>

<script>
import UsersProfile from "@/components/profile/UsersProfile";
import PostListFiltered from "@/components/post/PostListFiltered";
import Pagination from "@/components/Pagination";

import { mapActions, mapGetters } from "vuex";
export default {
  name: "UserProfile",
  components: {
    UsersProfile,
    PostListFiltered,
    Pagination,
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      postAuthor: {
        author: "",
      },
    };
  },
  watch: {
    "$route.params": {
      handler: "onProfileParamsChange",
      immediate: true,
      depp: true,
    },
  },
  computed: {
    ...mapGetters("profile", ["userProfile"]),
    ...mapGetters("posts", [
      "paramsPosts",
      "paramsCountPost",
      "paramsCurrentPage",
      "perPage",
    ]),
    isExist() {
      return Boolean(this.paramsPosts.length);
    },
  },
  methods: {
    ...mapActions("profile", ["fetchUserProfile"]),
    ...mapActions("posts", ["fetchPostsByParams"]),
    onProfileParamsChange({ id = this.id } = {}) {
      this.fetchUserProfile(Number(id));
      // console.log(this.id, this.userProfile.username);
      // console.log(id) /page , page: page
      // this.postAuthor.author = this.userProfile.username;
      this.fetchPostsByParams({ author: id });
    },
    onPageChange(page){
      this.fetchPostsByParams({ author: this.id, page: page });
    }
  },
};
</script>

<style scoped>
.u-posts{
  font-weight: bold;
  font-size: large;
  font-family: 'Times New Roman', Times, serif;
  box-shadow: 0px 5px 30px rgba(5, 30, 110, 0.7);
}

</style>
