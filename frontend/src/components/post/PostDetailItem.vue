<template>
  <div>
    <div class="container mt-2">
      <div class="row">
        <div class="col-12 top-part">
          <a class="mr-5 post-author" href="#">{{ post.author.username }}</a>
          <a class="mr-5" href="#">{{ localedate }}</a>
          <a v-if="isPostCategoryExist" href="#">{{ post.category.title }}</a>
          <img v-if="isPostImageExist" class="post-image" :src="post.image" />
        </div>
      </div>
      <div class="row">
        <div class="col-12 body-part">
          <h3>{{ post.title }}</h3>
          <p>{{ post.descriptions }}</p>
        </div>
      </div>
      <template v-if="isPostCommentsExist">
        <CommentsList :comments="post.comments"/>
      </template>
    </div>
  </div>
</template>

<script>
import CommentsList from "@/components/comment/CommentsList";
export default {
  name: "PostDetailItem",
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  components: {
    CommentsList,
  },
  computed: {
    localedate() {
      return new Date(this.post.date_create).toLocaleDateString();
    },
    isPostImageExist() {
      return Boolean(this.post.image);
    },
    isPostCategoryExist() {
      return Boolean(this.post.category);
    },
    isPostCommentsExist() {
      return Boolean(this.post.comments.length);
    },
  },
};
</script>

<style scoped>
.post-image {
  height: 20rem;
  width: 100%;
}
.top-part {
  border: cadetblue 2px solid;
}
.body-part {
  border: cadetblue 2px solid;
}
</style>
