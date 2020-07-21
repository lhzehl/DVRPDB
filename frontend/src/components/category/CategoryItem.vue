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
