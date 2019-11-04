<template>
  <div id="blog">
    <Pacman></Pacman>
    <Articles>
      <banner />
    </Articles>

  </div>
</template>

<script>
import Articles from "../components/blog/Articles"
import Banner from "../components/blog/Banner"
import Pacman from "../components/Pacman"
  export default {
    name: 'Blog',

    components: {
      Articles,
      Banner,
      Pacman
    },
    props: {
    }
  }
</script>
