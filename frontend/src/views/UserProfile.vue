<template>
  <div>
    <template v-if="userProfile.username">
      <UsersProfile :profile="userProfile" />
    </template>
    <template v-if="paramsPosts.length">
      <PostListFiltered :posts="paramsPosts" />
    </template>
  </div>
</template>

<script>
import UsersProfile from "@/components/profile/UsersProfile";
import PostListFiltered from "@/components/post/PostListFiltered";

import { mapActions, mapGetters } from "vuex";
export default {
  name: "UserProfile",
  components: {
    UsersProfile,
    PostListFiltered
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      postAuthor: {
        author: ""
      }
    };
  },
  watch: {
    "$route.params": {
      handler: "onProfileParamsChange",
      immediate: true,
      depp: true
    }
  },
  computed: {
    ...mapGetters("profile", ["userProfile"]),
    ...mapGetters("posts", [
      "paramsPosts",
      "paramsCountPost",
      "paramsCurrentPage",
      "perPage"
    ])
  },
  methods: {
    ...mapActions("profile", ["fetchUserProfile"]),
    ...mapActions("posts", ["fetchPostsByParams"]),
    onProfileParamsChange({ id = this.id } = {}) {
      this.fetchUserProfile(Number(id));
      // console.log(this.id, this.userProfile.username);
      // console.log(id)
      // this.postAuthor.author = this.userProfile.username;
      this.fetchPostsByParams({ author: id});
    }
  }
};
</script>

<style scoped></style>
