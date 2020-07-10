import Vue from "vue";
import VueRouter from "vue-router";
import PostList from "../views/PostList";
import PostDetail from "../views/PostDetail";
import Authorization from "../views/Authorization";
import Registration from "../views/Registration";

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
    path: "/auth",
    name: "Authorization",
    component: Authorization,
  },
  {
    path: "/registration",
    name: "Registration",
    component: Registration,
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

const router = new VueRouter({
  routes,
});

export default router;
