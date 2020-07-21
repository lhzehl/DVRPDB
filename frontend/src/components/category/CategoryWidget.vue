<template>
  <div class="category-block">
    <p class="category-head">Categories:</p>
    <div v-if="list.length">
      <div v-for="item in list" :key="item.id">
        <CategoryItem :item="item" />
      </div>
    </div>
  </div>
</template>

<script>
import CategoryItem from "@/components/category/CategoryItem";
export default {
  name: "CategoryWidget",
  props: {
    list: {
      type: Array,
      //   default: [],
    },
  },
  components: {
    CategoryItem,
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
