<template>
  <div>
    <template v-if="isExist">
      <NotificationsList :list="notifications" />
      <Pagination
        :count="countNotification"
        :current-page="currentPage"
        :per-page="perPage"
        @pageChanged="onPageChange"
      />
    </template>
  </div>
</template>

<script>
import NotificationsList from "@/components/notifications/NotificationsList";
import Pagination from "@/components/Pagination";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Notifications",
  props: {},
  components: {
    NotificationsList,
    Pagination,
  },
  computed: {
    ...mapGetters("notifications", [
      "notifications",
      "countNotification",
      "currentPage",
      "perPage",
    ]),
    isExist() {
      return Boolean(this.notifications.length);
    },
  },
  mounted() {
    this.fetchNotifications(1);
  },
  methods: {
    ...mapActions("notifications", ["fetchNotifications"]),
    onPageChange(page) {
      console.log(this.$route);
      this.fetchNotifications(page);
    },
  },
};
</script>

<style scoped></style>
