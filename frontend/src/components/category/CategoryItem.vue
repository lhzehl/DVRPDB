<template>
  <div>
    <router-link :to="params" class="category-item">{{
      item.title
    }}</router-link>
  </div>
</template>

<script>
export default {
  name: "CategoryItem",
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  computed: {
    params() {
      return `/posts/${this.item.title}`;
    },
  },
};
</script>
<style scoped>
.category-item {
  color: black;
  font-family: "Times New Roman", Times, serif;

  font-style: italic;
  box-shadow: rgba(37, 37, 37, 0.267);
  font-weight: bold;
}
.category-item:hover{
  font-size: x-large;
}
</style>
