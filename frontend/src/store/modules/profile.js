import axios from "@/plugins/axios";
import router from "@/router";
import mutations from "@/store/mutations";

const { OWNPROFILE, PROFILE } = mutations;

const profileStore = {
  namespaced: true,
  state: {
    // authUser: {},
    ownProfile: JSON.parse(localStorage.getItem('ownProfile'))||{},
    userProfile: {},
  },
  getters: {
    // authUser: ({ authUser }) => authUser,
    userProfile: ({ userProfile }) => userProfile,
    ownProfile: ({ ownProfile }) => ownProfile,
  },
  mutations: {
    [OWNPROFILE](state, value) {
      state.ownProfile = value;
    },
    [PROFILE](state, value) {
      state.userProfile = value;
    },
  },
  actions: {
    async fetchOwnProfile({ commit }) {
      try {
        const responceUser = await axios.get("/auth/users/me/");
        const id = responceUser.data.id;
        const responceProfile = await axios.get(`/api/v1/users/profile/${id}`);
        const ownProfile = responceProfile.data;
        localStorage.setItem("ownProfile", JSON.stringify(ownProfile));
        commit(OWNPROFILE, ownProfile);
      } catch (error) {
        localStorage.removeItem("lhzehl-blog-t");
        localStorage.removeItem("ownProfile")
        router.push("authorization");
      }
    },
    async fetchUserProfile({ commit }, id) {
      try {
        const responce = await axios.get(`/api/v1/users/profile/${id}`);
        const userProfile = responce.data;
        commit(PROFILE, userProfile);
        
      } catch (error) {
        console.log(error);
      }
    },
    async fetchUpdateProfile({ commit }, data) {
      const formData = new FormData();
      Object.keys(data).forEach((el) => {
        formData.append(el, data[el]);
      });


      try {
        const response = await axios.patch(
          `/api/v1/users/profile/${data.id}/`,
          formData
        );
        const ownProfile=response.data
        commit(OWNPROFILE, response.data);
        console.log(ownProfile)
        localStorage.setItem("ownProfile", JSON.stringify(ownProfile));
      } catch (err) {
        console.log(err);
      }
    },
    async fetchSubscriptionsForUsers({commit}, id){
      try {
        const responce = await axios.post('/api/v1/actions/watchuser/', id)
        console.log(responce, commit)
      } catch (error) {
        console.log(error)
      }

    }
  },
};
export default profileStore;
