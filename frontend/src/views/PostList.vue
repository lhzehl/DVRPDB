<template>
  <div class="home">
    <template v-if="isExist">
      <div v-for="post in postList" :key="post.date_create">
        <PostListItem :post="post" />
      </div>
    </template>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapActions, mapGetters } from "vuex";
import PostListItem from "@/components/post/PostListItem";

export default {
  name: "Home",
  components: {
    PostListItem,
  },
  computed: {
    ...mapGetters("posts", ["postList"]),
    isExist() {
      return Boolean(this.postList.length);
    },
  },
  mounted() {
    this.fetchPosts();
  },
  methods: {
    ...mapActions("posts", ["fetchPosts"]),
  },
};
</script>
