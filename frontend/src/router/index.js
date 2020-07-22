import Vue from "vue";
import VueRouter from "vue-router";
import PostList from "../views/PostList";
import PostDetail from "../views/PostDetail";
import Authorization from "../views/Authorization";
import Registration from "../views/Registration";
import OwnProfile from "../views/OwnProfile";
import UserProfile from "../views/UserProfile";
import CreatePost from "../views/CreatePost";
import DialogList from "../views/DialogList";
import DialogDetail from "../views/DialogDetail";
import Notifications from "../views/Notifications";
import FilteredPostListByCategory from "../views/FilteredPostListByCategory";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "PostList",
    component: PostList,
  },
  {
    path: "/post/:id",
    name: "PostDetail",
    component: PostDetail,
    props: castRouteParams,
  },
  {
    path: "/authorization",
    name: "Authorization",
    component: Authorization,
  },
  {
    path: "/registration",
    name: "Registration",
    component: Registration,
  },
  {
    path: "/profile",
    name: "OwnProfile",
    component: OwnProfile,
  },
  {
    path: "/users/profile/:id",
    name: "UserProfile",
    component: UserProfile,
    props: castRouteParams,
  },
  {
    path: "/create/post",
    name: "CreatePost",
    component: CreatePost,
  },
  {
    path: "/dialog",
    name: "DialogList",
    component: DialogList,
  },
  {
    path: "/dialog/:id",
    name: "DialogDetail",
    component: DialogDetail,
    props: castRouteParams,
  },
  {
    path: "/notifications",
    name: "Notifications",
    component: Notifications,
  },
  {
    path: "/posts/:category",
    name: "FilteredPostListByCategory",
    component: FilteredPostListByCategory,
    props: castRouteParamsCategory,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

function castRouteParams(route) {
  return {
    id: Number(route.params.id),
  };
}
function castRouteParamsCategory(route){
  return{
    category: route.params.category
  }
}

const router = new VueRouter({
  routes,
});

export default router;
