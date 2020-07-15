<template>
  <div>
    <div v-for="dialog in reply" :key="dialog.date_add">
      <ReplyItem :dialog="dialog" />
    </div>
  </div>
</template>

<script>
import ReplyItem from "@/components/dialog/ReplyItem";
export default {
  name: "ReplyList",
  props: {
    reply: {
      type: Array,
      required: true,
    },
  },
  components: {
    ReplyItem,
  },
};
</script>

<style scoped></style>