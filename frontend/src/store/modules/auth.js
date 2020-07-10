import axios from "@/plugins/axios";
// import router from "@/router"; /auth/users/
import mutations from "@/store/mutations";

const {
  ISAUTH,
  ERRREGISTERMAIL,
  ERRREGISTERPASS,
  ERRLOGIN,
  CREATEDNEWACC,
} = mutations;

const authStore = {
  namespaced: true,
  state: {
    authData: {},
    errRegMail: "",
    errRegPass: "",
    errLogin: "",
    isCreated: "",
    isLogin: Boolean(localStorage.getItem("lhzehl-blog-t")),
  },
  getters: {
    isLogin: ({ isLogin }) => isLogin,
    errRegMail: ({ errRegMail }) => errRegMail,
    errRegPass: ({ errRegPass }) => errRegPass,
    isCreated: ({ isCreated }) => isCreated,
    errLogin: ({ errLogin }) => errLogin,
  },
  mutations: {
    [ISAUTH](state, value) {
      state.isLogin = value;
    },
    [ERRREGISTERMAIL](state, value) {
      state.errRegMail = value;
    },
    [ERRREGISTERPASS](state, value) {
      state.errRegPass = value;
    },
    [ERRLOGIN](state, value) {
      state.errLogin = value;
    },
    [CREATEDNEWACC](state, value) {
      state.isCreated = value;
    },
  },
  actions: {
    async fetchLogin({ commit }, authData) {
      const formData = new FormData();
      Object.keys(authData).forEach((el) => {
        formData.append(el, authData[el]);
      });
      try {
        const response = await axios.post("/auth/token/login", formData);
        const token = response.data.auth_token.slice(1, -1);
        localStorage.setItem("lhzehl-blog-t", token);
        commit(ISAUTH, true);
      } catch (err) {
        let errText = err.response.data.non_field_errors[0];
        commit(ERRLOGIN, errText);
      }
    },
    async fetchNewUser({ commit }, authData) {
      const formData = new FormData();
      Object.keys(authData).forEach((el) => {
        formData.append(el, authData[el]);
      });
      try {
        commit(ERRREGISTERMAIL, "");
        commit(ERRREGISTERPASS, "");
        commit(CREATEDNEWACC, "");

        const response = await axios.post("/auth/users/", formData);
        commit(CREATEDNEWACC, response.statusText);
        
      } catch (err) {
        const errTextMail = err.response.data.email;
        const errTextPass = err.response.data.password;
        if (errTextMail) {
          commit(ERRREGISTERMAIL, errTextMail[0]);
        }
        if (errTextPass) {
          commit(ERRREGISTERPASS, errTextPass[0]);
        }
      }
    },
  },
};
export default authStore;
