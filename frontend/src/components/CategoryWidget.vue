<template>
  <div class="category-block">
    <p class="category-head">Categories:</p>
    <div v-for="item in list" :key="item.id">
      <p class="category-item">{{ item.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CategoryWidget",
  props: {
    list: {
      type: Array,
      //   default: [],
    },
  },
};
</script>

<style scoped>
.category-block {
  position: absolute;
  border: cadetblue 2px solid;
  left: 0;
  margin-top: 30px;
}
.category-head {
  font-family: "Times New Roman", Times, serif;
  /* font-size: x-large; */
  font-weight: bold;
}
.category-item {
  border: cadetblue 2px solid;
}
</style>
