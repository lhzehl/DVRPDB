<template>
  <div>
    <button
      v-if="!edited && isOwn"
      class="upd-btn mt-2  mx-auto"
      @click="edited = !edited"
    >
      Edit
    </button>

    <div class="container mt-2">
      <template v-if="!edited">
        <div class="row">
          <div class="col-12 top-part">
            <router-link class="mr-5 post-author" :to="routeToAuthor">{{
              post.author.username
            }}</router-link>
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
      </template>
      <template v-if="edited">
        <PostUpdate :post="post" @cancel="edited = !edited" />
      </template>

      <CommentCreate :id="post.id" />
      <template v-if="isPostCommentsExist">
        <CommentsList :comments="post.comments" />
      </template>
    </div>
  </div>
</template>

<script>
import CommentsList from "@/components/comment/CommentsList";
import CommentCreate from "@/components/comment/CommentCreate";
import PostUpdate from "@/components/post/PostUpdate";
import { mapGetters } from "vuex";
export default {
  name: "PostDetailItem",
  data: () => ({
    edited: false,
  }),
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  components: {
    CommentsList,
    CommentCreate,
    PostUpdate,
  },
  computed: {
    ...mapGetters("profile", ["ownProfile"]),
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
    routeToAuthor() {
      return `/users/profile/${this.post.author.id}`;
    },
    isOwn() {
      if (localStorage.getItem("ownProfile")) {
        return this.ownProfile.id === this.post.author.id;
      } else {
        return false;
      }
    },
  },
  methods: {
    // ...mapActions('post', ['fetchUpdatePost'])
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
.upd-btn {
  color: rgba(34, 21, 2, 0.877);
  font-size: large;
  font-weight: bold;
  font-family: "Times New Roman", Times, serif;
  border: solid 3px rgba(70, 99, 180, 0.788);
  max-width: 100%;
  background: rgba(255, 255, 255, 0.555);
  /* bottom: 0px; */
  /* right: 185px; */
  /* position: absolute; */
  border-radius: 5px;
}
.upd-btn:hover {
  background: rgba(7, 10, 196, 0.829);
  color: rgb(255, 255, 255);
  border: solid 1px rgb(0, 0, 0);
}
</style>
