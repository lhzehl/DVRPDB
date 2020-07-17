import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
// import router from "../../router";

const { NOTIFICATIONS, NOTIFICATIONSNUM } = mutations;

const notificationsStore = {
  namespaced: true,
  state: {
    notifications: {},
    countNotification: {},
    currentPage: 1,
    perPage: 10,
  },
  getters: {
    notifications: ({ notifications }) => notifications,
    countNotification: ({ countNotification }) => countNotification,
    currentPage: ({ currentPage }) => currentPage,
    perPage: ({ perPage }) => perPage,
  },
  mutations: {
    [NOTIFICATIONS](state, value) {
      state.notifications = value;
    },
    [NOTIFICATIONSNUM](state, value) {
      state.countNotification = value;
    },
  },
  actions: {
    async fetchNotifications({ commit }, page) {
      try {
        const response = await axios.get(
          `/api/v1/actions/notifications/?limit=10&offset=${page - 1}0`
        );
        const notificationList = response.data.results;
        const countNotification = response.data.count;
        commit(NOTIFICATIONSNUM, countNotification);
        commit(NOTIFICATIONS, notificationList);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchSubscribeForUser({ commit }, id) {
      const formData = new FormData();
      formData.append("object_of_observation", id);
      try {
        const response = await axios.post(
          "/api/v1/actions/watchuser/",
          formData
        );
        console.log(response);
      } catch (error) {
        console.log(commit, error);
      }
    },
  },
};

export default notificationsStore;
