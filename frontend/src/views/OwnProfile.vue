<template>
  <div>
    <div v-if="isExistProfile">
      <AuthProfile :profile="ownProfile" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AuthProfile from "@/components/profile/AuthProfile";
export default {
  name: "OwnProfile",
  components:{
      AuthProfile
  },

  mounted() {
    this.fetchOwnProfile();
  },
  methods: {
    ...mapActions("profile", ["fetchOwnProfile"]),
  },
  computed: {
    ...mapGetters("profile", ["ownProfile"]),
    isExistProfile() {
      return Boolean(this.ownProfile.id);
    },
  },
};
</script>

<style scoped></style>
