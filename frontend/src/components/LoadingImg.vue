<template>
    <div>
        <v-skeleton-loader
            :boilerplate="false"
            :type="skeletonType"
            :tile="true"
            class="mx-auto"
        ></v-skeleton-loader>
    </div>
</template>

<script>
export default {
  data () {
        return {
            skeletonType:"list-item-avatar-three-line",
      }
  },
}
</script>

<style>
</style>