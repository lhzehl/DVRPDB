import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
const { CATEGORYLIST, CREATENEWCATEGORY } = mutations;

// function serializeResponse(data) {
//   // data.reduce
//   return data.reduce((acc, item) => {
//     // console.log(item);
//     acc[item.id] = item.title;
//     return acc;
//   }, {});
// }

const categoryStore = {
  namespaced: true,
  state: {
    categoryList: JSON.parse(localStorage.getItem("categoryList")) || [],
    isCreated: "",
  },
  getters: {
    categoryList: ({ categoryList }) => categoryList,
    isCreated: ({ isCreated }) => isCreated,
  },
  mutations: {
    [CATEGORYLIST](state, value) {
      state.categoryList = value;
    },
    [CREATENEWCATEGORY](state, value) {
      state.isCreated = value;
    },
  },
  actions: {
    async fetchCategoryList({ commit }) {
      try {
        const response = await axios.get("/api/v1/post/categories/");
        const categoryList = response.data.results;
        // console.log(JSON.stringify(categoryList));
        // const serializedCategory = serializeResponse(categoryList);
        // console.log(JSON.stringify(serializedCategory));
        localStorage.setItem("categoryList", JSON.stringify(categoryList));
        commit(CATEGORYLIST, categoryList);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchNewCategory({ commit }, data) {
      const formData = new FormData();
      Object.keys(data).forEach((el) => {
        formData.append(el, data[el]);
      });
      try {
        commit(CREATENEWCATEGORY, "");
        const response = await axios.post(
          "/api/v1/post/newcategory/",
          formData
        );
        commit(CREATENEWCATEGORY, response.statusText);
      } catch (error) {
        console.log(error);
      }
    },
  },
};

export default categoryStore;
