<template>
  <div>
    <div class="row mt-2 mb-2">
      <div class="col-4 comment-author">
        <a href="#">{{ comment.author.username }}</a>
        <img
          class="comment-author-image mt-2 mr-2"
          :src="comment.author.image"
        />
      </div>
      <div class="col-8 comment-body">{{ comment.text }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentItem",
  props: {
    comment: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.comment-author {
  border: solid 2px steelblue;
}
.comment-author-image {
  max-width: 100%;
  max-height: 100%;
  border-radius: 1rem;
  position: relative;
}
.comment-body {
  border: solid 2px steelblue;
}
</style>
