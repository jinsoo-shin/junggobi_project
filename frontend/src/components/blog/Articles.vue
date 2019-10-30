<template>
  <section id="feed">
    <Feed>
      <slot />
    </Feed>
  </section>
</template>

<script>
import Feed from "../Feed"
  export default {
    components: {
      Feed
    }
  }
</script>
