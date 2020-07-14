import axios from "@/plugins/axios";
import mutations from "@/store/mutatuions";
// import router from "@/router";

const { DIALOGS, DIALOGDETAIL } = mutations;

const dialogStore = {
  namespaced: true,
  state: {
    dialogList: {},
    dialogDetail: {},
  },
  getters: {
    dialogList: ({ dialogList }) => dialogList,
    dialogDetail: ({ dialogDetail }) => dialogDetail,
  },
  mutations: {
    [DIALOGS](state, value) {
      state.dialogList = value;
    },
    [DIALOGDETAIL](state, value) {
      state.dialogDetail = value;
    },
  },
  actions: {
    async fetchDialogs() {
        
    },
  },
};

export default dialogStore;
