<template>
  <div>
    <div class="container mt-2">
      <div class="row">
        <div class="col-4 post-left">
          <router-link :to="routeToAuthor">{{ post.author.username }}</router-link
          ><a> {{ localedate }}</a>
        </div>
        <div class="col-8"></div>
      </div>
      <div class="row">
        <div class="col-4 post-left">
          <img class="mx-auto post-image" :src="post.image" />
        </div>
        <div class="col-8 post-short">
          <h3>
            {{ post.title }}
          </h3>
          <p>
            {{ shortDetail }}
          </p>
        </div>
      </div>
      <div class="row">
        <div class="col-4"></div>
        <div class="col-8 post-short">
          <router-link :to="detail">View all </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostListItem",
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  computed: {
    localedate() {
      return new Date(this.post.date_create).toLocaleDateString();
    },
    detail() {
      // console.log(this.post.id)
      return `/post/${this.post.id}`;
    },
    shortDetail() {
      if (this.post.descriptions.length > 250) {
        return `${this.post.descriptions.slice(0, 250)} .....`;
      } else {
        return this.post.descriptions;
      }
    },
    routeToAuthor(){
      return `/users/profile/${this.post.author.id}`
    },
  },
};
</script>

<style scoped>
.post-left {
  border: 2px solid rgba(8, 16, 126, 0.692);
  font-size: 0.8rem;
}
.post-short {
  border: 2px solid steelblue;
}
.post-image{
  max-width: 100%;
}
</style>
