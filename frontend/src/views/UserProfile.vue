<template>
  <div>
    <UsersProfile v-if="userProfile.id" :profile="userProfile" />
  </div>
</template>

<script>
import UsersProfile from "@/components/profile/UsersProfile";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "UserProfile",
  components: {
    UsersProfile,
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  watch: {
    "$route.params": {
      handler: "onProfileParamsChange",
      immediate: true,
      depp: true,
    },
  },

  methods: {
    ...mapActions("profile", ["fetchUserProfile"]),
    onProfileParamsChange({ id = this.id } = {}) {
      this.fetchUserProfile(Number(id));
    },
  },
  computed: {
    ...mapGetters("profile", ["userProfile"]),
  },
};
</script>

<style scoped></style>
