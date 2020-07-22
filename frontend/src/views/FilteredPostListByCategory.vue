<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-9">
          <template v-if="isExist">
            <div v-for="post in paramsPosts" :key="post.date_create">
              <PostListItem :post="post" />
            </div>
          </template>
        </div>
        <div class="col-3">
          <CategoryWidget :list="categoryList" />
        </div>
      </div>
      <template v-if="isExist">
        <Pagination
          :count="paramsCountPost"
          :current-page="paramsCurrentPage"
          :per-page="perPage"
          @pageChanged="onPageChange"
        />
      </template>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Pagination from "@/components/Pagination";
import PostListItem from "@/components/post/PostListItem";
import CategoryWidget from "@/components/category/CategoryWidget";

export default {
  name: "FilteredPostListByCategory",

  props: {
    category: {
      type: String,
    },
  },
  data: () => ({
    params: {},
  }),

  components: {
    PostListItem,
    Pagination,
    CategoryWidget,
  },

  computed: {
    ...mapGetters("posts", [
      "paramsPosts",
      "perPage",
      "paramsCountPost",
      "paramsCurrentPage",
    ]),
    ...mapGetters("category", ["categoryList"]),
    isExist() {
      return Boolean(this.paramsPosts.length);
    },
  },
  watch: {
    "$route.params": {
      handler: "onCategoryChange",
      immediate: true,
      depp: true,
    },
  },
  methods: {
    ...mapActions("posts", ["fetchPostsByParams"]),
    onPageChange(page) {
      const params = this.params;
      params.page = page;
      this.fetchPostsByParams(params);
    },
    onCategoryChange({ category = this.category }) {
      const params = this.params;
      params.category = category;
      this.fetchPostsByParams(params);
    },
  },
};
</script>

<style scoped></style>
