import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
// import router from "../../router";

const { NOTIFICATIONS } = mutations;

const notificationsStore = {
  namespaced: true,
  state: {
    notifications: {},
  },
  getters: {
    notifications: ({ notifications }) => notifications,
  },
  mutations: {
    [NOTIFICATIONS](state, value) {
      state.notifications = value;
    },
  },
  actions: {
    async fetchNotifications({ commit }, page) {
      try {
        const response = await axios.get(
          `/api/v1/actions/notifications/?limit=10&offset=${page - 1}0`
        );
        const notificationList = response.data.results;
        commit(NOTIFICATIONS, notificationList);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchSubscribeForUser({ commit }, id) {
      const formData = new FormData();
      formData.append("object_of_observation", id);
      try {
        const response = await axios.post("/api/v1/actions/watchuser/", formData);
        console.log(response);
      } catch (error) {
        console.log(commit, error);
      }
    },
  },
};

export default notificationsStore;
