<template>
  <div id="blog">
    <Articles>
      <banner />
    </Articles>
  </div>
</template>

<script>
import Articles from "../components/blog/Articles"
import Banner from "../components/blog/Banner"
  export default {
    name: 'Blog',
    components: {
      Articles,
      Banner,
    }
  }
</script>
