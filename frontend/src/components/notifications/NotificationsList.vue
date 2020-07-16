<template>
  <div>
 
    <div
      class="container"
      v-for="notification in list"
      :key="notification.actions.id"
    >

    <NotificationItem :notification="notification" />
    </div>
  </div>
</template>

<script>
import NotificationItem from "@/components/notifications/NotificationItem";
export default {
  name: "NotificationsList",
  props: {
    list: {
      type: Array,
      required: true,
    },
  },
  components: {
    NotificationItem
  },
};
</script>

<style scoped>
</style>
