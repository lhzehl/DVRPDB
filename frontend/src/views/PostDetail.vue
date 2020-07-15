<template>
  <div>
    <PostDetailItem v-if="isExist" :post="postDetail" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import PostDetailItem from "@/components/post/PostDetailItem";
export default {
  name: "PostDetail",
  components: {
    PostDetailItem,
  },
  props: {
    id: {
      type: Number,
    },
  },
  watch: {
    "$route.params": {
      handler: "onPostParamsChange",
      immediate: true,
      depp: true,
    },
  },

  methods: {
    ...mapActions("posts", ["fetchPostDetail"]),
    onPostParamsChange({ id = this.id } = {}) {
      this.fetchPostDetail(Number(id));
    },
  },
  computed: {
    ...mapGetters("posts", ["postDetail"]),
    isExist() {
      return Boolean(this.postDetail.author);
    },
  },
};
</script>

<style scoped></style>
