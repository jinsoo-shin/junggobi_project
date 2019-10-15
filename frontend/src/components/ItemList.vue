<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
        --------------itemListComponent---------------
        <v-flex v-for="card in itemListCards" :key="card.name" pa-1>
            <ItemListCard :name="card.name" :body="card.body" :link="card.link"/>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ItemListCard from './ItemListCard.vue'
export default {
  components: {
      ItemListCard
  },
  props: {
      itemListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
  }),
  computed: {

  },
};
</script>
