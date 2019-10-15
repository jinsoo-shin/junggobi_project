<template>
  <v-app>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>
<style>

</style>
<script>
import store from './store'

export default {
	name: 'App',
  components: {

  },
	store,
	data() {
		return {
		}
	}
}
</script>
