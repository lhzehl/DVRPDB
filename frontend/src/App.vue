<template>
  <div id="app">
    <NavBar />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import { mapActions } from "vuex";
export default {
  name: "BlogApp",
  components: {
    NavBar,
  },
  data: () => ({
    notificationSocket: null,
  }),
  mounted() {
    this.fetchCategoryList();
  },
  // created: function() {
  //   console.log("Start connection");

  //   this.notificationSocket = new WebSocket(
  //     "ws://" "127.0.0.1:8000/" + "notification/"
  //   );

  //   // this.requestSocket
  // },
  methods: {
    ...mapActions("category", ["fetchCategoryList"]),
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* #nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
