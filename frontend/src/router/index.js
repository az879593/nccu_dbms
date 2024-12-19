import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
        path: '/',
        name: 'home',
        component: HomeView,
    },
    {
        path: '/user',
        name: 'user',
        component: () => import('../views/UserView.vue')
    },
    {
        path: '/book',
        name: 'book',
        component: () => import('../views/BookView.vue')
    },
    {
        path: '/post',
        name: 'post',
        component: () => import('../views/PostView.vue')
    },
    {
        path: '/comments',
        name: 'comments',
        component: () => import('../views/CommentView.vue')
    }
  ],
});

export default router;
