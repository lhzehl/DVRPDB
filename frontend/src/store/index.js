import Vue from "vue";
import Vuex from "vuex";
import posts from "./modules/posts";
import auth from "./modules/auth";
import profile from "./modules/profile";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    posts,
    auth,
    profile,
  },
});
