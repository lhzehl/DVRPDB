<template>
  <div id="nav">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand to="/">Home</b-navbar-brand>

      <b-navbar-brand  to="/create/post" v-if="isLogin">CreatePost</b-navbar-brand>
      <!-- <b-navbar-brand  to="/create/category" v-if="isLogin">CreateCategory</b-navbar-brand> -->
      
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- <b-navbar-nav>
          <b-nav-item to="/about">About</b-nav-item>
<a class="mine">lhzehl blog</a> -->
        <!-- </b-navbar-nav> -->

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right v-if="isLogin">
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>{{ ownProfile.username }}</em>
            </template>
            <b-dropdown-item to="/profile">Profile</b-dropdown-item>
            <b-dropdown-item to="/create/post">Create Post</b-dropdown-item>
            <b-dropdown-item to="/dialog">Messages</b-dropdown-item>
            <!-- notifications -->
            <b-dropdown-item to="/notifications">Notifications</b-dropdown-item>
            <b-dropdown-item @click="logOut">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item-dropdown right v-else>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>Auth</em>
            </template>
            <b-dropdown-item to="/authorization">Login</b-dropdown-item>
            <b-dropdown-item to="/registration">Register</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <router-view />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Navbar",
  computed: {
    ...mapGetters("auth", ["isLogin"]),
    ...mapGetters("profile", ["ownProfile"]),
  },
  methods: {
    ...mapActions("auth", ["changeStoreToNonAuth"]),
    logOut() {
      localStorage.removeItem("lhzehl-blog-t");
      localStorage.removeItem("ownProfile");
      this.changeStoreToNonAuth()
      this.$router.push("/authorization");
    },
  },
};
</script>

<style scoped>
.mine {
  color: darkgray;
}
.bg-info{
  background-color: black !important;
}

</style>
