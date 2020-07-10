import axios from "@/plugins/axios";
import mutations from "@/store/mutations";
// import router from "@/router";

const { POSTS, POSTDETAIL } = mutations;

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
  },
  actions: {
    async fetchPosts({ commit }) {
      try {
        //   console.log(context);
        const response = await axios.get("/api/v1/post/posts/");
        //   console.log(response.data);
        const posts = response.data;
        commit(POSTS, posts);
      } catch (err) {
        console.log(err);
      }
    },
    async fetchPostDetail({commit}, id){
      try{
        const response = await axios.get(`/api/v1/post/posts/${id}`)
        const postDetail = response.data
        commit(POSTDETAIL, postDetail)
        // console.log(postDetail, commit)


      } catch(err){
        console.log(err)
        
      }
    },
  },
};
export default postsStore;
