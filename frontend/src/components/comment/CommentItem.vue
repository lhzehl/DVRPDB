<template>
  <div>
    <div class="row mt-2 mb-2">
      <div class="col-4 comment-author">

                  <router-link class="mr-5 route-text" :to="routeToAuthor">{{
            comment.author.username
          }}</router-link>
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
  computed: {
        routeToAuthor(){
      return `/users/profile/${this.comment.author.id}`
    },
  },
};
</script>

<style scoped>
.comment-author {
  border: solid 2px rgb(0, 0, 0);
}
.comment-author-image {
  max-width: 100%;
  max-height: 100%;
  border-radius: 1rem;
  position: relative;
}
.comment-body {
  border: solid 2px rgb(0, 0, 0);
}
.route-text {
  color: black;
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
