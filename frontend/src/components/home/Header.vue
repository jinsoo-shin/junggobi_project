<template>
    <v-layout>
        <v-toolbar color="white">
        <v-toolbar-title>
            <router-link to="/" id="font" style="text-decoration: none; color:black;">Junggobi</router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn text @click="blog" id="font">Post</v-btn>
            <v-btn text @click="searchAll" id="font">Search</v-btn>
        </v-toolbar-items>
        </v-toolbar>
    </v-layout>
</template>
<script>
export default {
  methods: {
    async blog() {
      await this.$store.dispatch('data/getBlogPost').then(res => this.$router.push({ name :"blogpage", params : { data : res}}));
    },
    async searchAll() {
      await this.$store.dispatch('data/searchById', "")
      .then(res => {
        this.$router.push({ name : "searchPage", params: { itemListSub: res}})
      })
    },
  }
}
</script>

