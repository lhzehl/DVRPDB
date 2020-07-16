import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
import router from "../../router";


const { POSTS, POSTSNUM, POSTDETAIL, ISAUTH } = mutations;

const postsStore = {
  namespaced: true,
  state: {
    posts: {},
    postDetail: {},
    countPost: "",
    currentPage: 1,
    perPage: 10,
  },
  getters: {
    postList: ({ posts }) => posts,
    postDetail: ({ postDetail }) => postDetail,
    countPost: ({ countPost }) => countPost,
    currentPage: ({ currentPage }) => currentPage,
    perPage: ({ perPage }) => perPage,
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
    [POSTSNUM](state, value) {
      state.countPost = value;
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
    async fetchPosts({ commit }, page) {
      try {

        const response = await axios.get(
          `/api/v1/post/posts/?limit=10&offset=${page - 1}0`
        );

        const posts = response.data.results;
        const countPost = response.data.count;
        commit(POSTS, posts);
        commit(POSTSNUM, countPost);
      } catch (err) {
        console.log(err);
      }
    },
    async fetchPostDetail({ commit }, id) {
      try {
        const response = await axios.get(`/api/v1/post/posts/${id}`);
        const postDetail = response.data;
        commit(POSTDETAIL, postDetail);

      } catch (err) {
        console.log(err);
        localStorage.removeItem("lhzehl-blog-t");
      }
    },
    async fetchUpdatePost({ commit }, data) {
      try {
        const formData = new FormData();
        Object.keys(data).forEach((el) => {
          formData.append(el, data[el]);
        });
        const responsePath = await axios.patch(
          `/api/v1/post/posts/${data.id}/`,
          formData
        );
        const post_id = responsePath.data.id;
        const responseGet = await axios.get(`/api/v1/post/posts/${post_id}`);
        const postDetail = responseGet.data;
        commit(POSTDETAIL, postDetail);
      } catch (error) {
        console.log(error);
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

        const post_id = postResponse.data.post;
        const getResponse = await axios.get(`/api/v1/post/posts/${post_id}`);
        const postDetail = getResponse.data;
        commit(POSTDETAIL, postDetail);

      } catch (error) {
        console.log(error);
      }
    },
    // async fetchUpdateComment({}){}
  },
};
export default postsStore;
