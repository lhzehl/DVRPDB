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
            <router-link
              class="mr-5 post-author route-text"
              :to="routeToAuthor"
              >{{ post.author.username }}</router-link
            >
            <a class="mr-5 route-text" href="#">{{ localedate }}</a>
            <router-link class="route-text" v-if="isPostCategoryExist" :to="params">{{
              post.category.title
            }}</router-link>
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
    params() {
      return `/posts/${this.post.category.title}`;
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
  border: rgb(45, 48, 48) 2px solid;
}
.body-part {
  border: rgb(0, 0, 0) 2px solid;
}
.upd-btn {
  color: rgba(34, 21, 2, 0.877);
  font-size: large;
  font-weight: bold;
  font-family: "Times New Roman", Times, serif;
  border: solid 3px rgba(23, 23, 24, 0.788);
  max-width: 100%;
  background: rgba(255, 255, 255, 0.555);
  /* bottom: 0px; */
  /* right: 185px; */
  /* position: absolute; */
  border-radius: 5px;
}
.upd-btn:hover {
  background: rgba(255, 255, 255, 0.425);
  color: rgba(24, 24, 24, 0.897);
  font-size: x-large;
  border: solid 2px rgb(0, 0, 0);
}
.route-text {
  color: black;
  font-size: large;
  font-weight: bold;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>
