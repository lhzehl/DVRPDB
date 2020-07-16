<template>
  <div>
      <NotificationsList v-if="isExist" :list="notifications" />
    
  </div>
</template>

<script>
import NotificationsList from "@/components/notifications/NotificationsList";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Notifications",
  props: {},
  components: {
    NotificationsList,
  },
  computed: {
    ...mapGetters("notifications", ["notifications"]),
    isExist() {
      return Boolean(this.notifications.length);
    },
  },
  mounted() {
    this.fetchNotifications(1);
  },
  methods: {
    ...mapActions("notifications", ["fetchNotifications"]),
  },
};
</script>

<style scoped></style>
