<template>
  <div class="navbar">
    <router-link to="/">Home</router-link>
    <router-link to="/contact">Contact</router-link>
    <router-link to="/about">About</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
//   props: {
//     msg: String
//   }
}
</script>