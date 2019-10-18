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
import collection from 'easter-egg-collection'
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
<style lang="scss">
@import '@/styles/index.scss';
/* Remove in 1.2 */
.v-datatable thead th.column.sortable i {
  vertical-align: unset;
}
</style>