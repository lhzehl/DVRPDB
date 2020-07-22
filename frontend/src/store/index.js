import Vue from "vue";
import Vuex from "vuex";
import posts from "./modules/posts";
import auth from "./modules/auth";
import profile from "./modules/profile";
import dialog from "./modules/dialog";
import notifications from "./modules/notifications";
import category from "./modules/category";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    posts,
    auth,
    profile,
    dialog,
    notifications,
    category
  },
});
