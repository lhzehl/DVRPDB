<template>
  <div class="container">
      <PostCreate />
  </div>
</template>

<script>
import PostCreate from "@/components/post/PostCreate";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "CreatePost",
  components: {
    PostCreate,
  },
  mounted() {
    if (!this.isLogin) {
      this.redirectToAuth();
    }
  },
  methods: {
    ...mapActions("auth", ["redirectToAuth"]),
  },
  computed: {
    ...mapGetters("auth", ["isLogin"]),
  },
};
</script>

<style scoped></style>
