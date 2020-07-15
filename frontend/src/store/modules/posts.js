import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
import router from "../../router";
// import router from "@/router";

const { POSTS, POSTDETAIL, ISAUTH } = mutations;

const postsStore = {
  namespaced: true,
  state: {
    posts: {},
    postDetail: {},
  },
  getters: {
    postList: ({ posts }) => posts,
    postDetail: ({ postDetail }) => postDetail,
  },
  mutations: {
    [POSTS](state, value) {
      state.posts = value;
    },
    [POSTDETAIL](state, value) {
      state.postDetail = value;
    },
    [ISAUTH](state, value) {
      state.isLogin = value;
    },
  },
  actions: {
    async fetchNewPost({ commit }, data) {
      const formData = new FormData();
      Object.keys(data).forEach((el) => {
        formData.append(el, data[el]);
      });
      try {
        const response = await axios.post("/api/v1/post/newpost/", formData);
        const post_id = response.data.id;
        router.push(`/post/${post_id}`);
      } catch (error) {
        console.log(error, commit);
        // localStorage.removeItem("lhzehl-blog-t")
        // commit(ISAUTH, false)
      }
    },
    async fetchPosts({ commit }) {
      try {
        //   console.log(context);
        const response = await axios.get("/api/v1/post/posts/");
        //   console.log(response.data);
        const posts = response.data.results;
        commit(POSTS, posts);
      } catch (err) {
        console.log(err);
      }
    },
    async fetchPostDetail({ commit }, id) {
      try {
        const response = await axios.get(`/api/v1/post/posts/${id}`);
        const postDetail = response.data;
        commit(POSTDETAIL, postDetail);
        // console.log(postDetail, commit)
      } catch (err) {
        console.log(err);
        localStorage.removeItem("lhzehl-blog-t");
      }
    },
    async fetchNewComment({ commit }, data) {
      const formData = new FormData();

      Object.keys(data).forEach((el) => {
        formData.append(el, data[el]);
      });
      try {
        const postResponse = await axios.post(
          "/api/v1/post/newcomment/",
          formData
        );
        // console.log(response, commit);
        const post_id = postResponse.data.post;
        const getResponse = await axios.get(`/api/v1/post/posts/${post_id}`);
        const postDetail = getResponse.data;
        commit(POSTDETAIL, postDetail);

        // const post_id
      } catch (error) {
        console.log(error);
      }
    },
  },
};
export default postsStore;
