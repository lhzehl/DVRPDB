<template>
  <div>
    <div v-for="comment in comments" :key="comment.date_add">
      <CommentItem :comment="comment" />
    </div>
  </div>
</template>

<script>
import CommentItem from "@/components/comment/CommentItem";
export default {
  name: "CommentsList",
  props: {
    comments: {
      type: Array,
      required: true,
    },
  },
  components: {
    CommentItem,
  },
};
</script>

<style scoped></style>
