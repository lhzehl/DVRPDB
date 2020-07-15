import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
import router from "@/router";

const { DIALOGSI, DIALOGSO, DIALOGDETAIL } = mutations;

const dialogStore = {
  namespaced: true,
  state: {
    dialogInList: {},
    dialogOutList: {},
    dialogDetail: {},
  },
  getters: {
    dialogInList: ({ dialogInList }) => dialogInList,
    dialogOutList: ({ dialogOutList }) => dialogOutList,
    dialogDetail: ({ dialogDetail }) => dialogDetail,
  },
  mutations: {
    [DIALOGSI](state, value) {
      state.dialogInList = value;
    },
    [DIALOGSO](state, value) {
      state.dialogOutList = value;
    },
    [DIALOGDETAIL](state, value) {
      state.dialogDetail = value;
    },
  },
  actions: {
    async fetchStartDialog({ commit }, data) {
      const formData = new FormData();
      Object.keys(data).forEach((el) => {
        formData.append(el, data[el]);
      });
      try {
        const responce = await axios.post("/api/v1/dialog/start/", formData);
        const dialog_id = responce.data.id;
        router.push(`/dialog/${dialog_id}`);
      } catch (error) {
        console.log(error, commit);
      }
    },
    async fetchDialogList({ commit }) {
      try {
        const responceI = await axios.get("/api/v1/dialog/rlist/");
        const responceO = await axios.get("/api/v1/dialog/slist/");

        const dialogInList = responceI.data.results;
        const dialogOutList = responceO.data.results;

        commit(DIALOGSI, dialogInList);
        commit(DIALOGSO, dialogOutList);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchDialogDetail({ commit }, id) {
      try {
        const responce = await axios.get(`/api/v1/dialog/${id}`);
        const dialogDetail = responce.data;
        commit(DIALOGDETAIL, dialogDetail);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchReplyDialog({ commit }, data) {
      const formData = new FormData();

      Object.keys(data).forEach((el) => {
        formData.append(el, data[el]);
      });
      try {
        const dialogResponse = await axios.post(
          "/api/v1/dialog/reply/",
          formData
        );
        // console.log(dialogResponse)
        const dialog_id = dialogResponse.data.dialog;
        const getResponse = await axios.get(`/api/v1/dialog/${dialog_id}`);
        const dialogDetail = getResponse.data;
        commit(DIALOGDETAIL, dialogDetail);
      } catch (error) {
        console.log(error);
      }
    },
  },
};

export default dialogStore;
