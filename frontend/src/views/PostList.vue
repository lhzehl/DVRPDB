<template>
  <div class="home">
    <div class="container">
      <div class="row">
        <div class="col-9">
          <template v-if="isExist">
            <div v-for="post in postList" :key="post.date_create">
              <PostListItem :post="post" />
            </div>
          </template>
        </div>
        <div class="col-3">
          <CategoryWidget />
        </div>
        
      </div>
      <template v-if="isExist">
        <Pagination
          :count="countPost"
          :current-page="currentPage"
          :per-page="perPage"
          @pageChanged="onPageChange"
        />
      </template>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapActions, mapGetters } from "vuex";
import Pagination from "@/components/Pagination";
import PostListItem from "@/components/post/PostListItem";
import CategoryWidget from "@/components/CategoryWidget";
export default {
  name: "Home",
  components: {
    PostListItem,
    Pagination,
    CategoryWidget,
  },
  computed: {
    ...mapGetters("posts", ["postList", "countPost", "currentPage", "perPage"]),
    isExist() {
      return Boolean(this.postList.length);
    },
  },
  // watch: {
  //   "$route.params": {
  //     handler: "onPageChange",
  //     immediate: true,
  //     depp: true,
  //   },
  // },
  mounted() {
    this.fetchPosts(1);
    // page = 1 =>0
  },
  methods: {
    ...mapActions("posts", ["fetchPosts"]),
    onPageChange(page) {
      console.log(this.$route);
      this.fetchPosts(page);
    },
  },
};
</script>
