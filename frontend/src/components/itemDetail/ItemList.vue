<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
        --------------itemListComponent---------------
        <v-select
          v-model="sortMethod"
          :items="sortMethodList"
          label="정렬방법"
          dense
          solo
          @change="ccc()"
        ></v-select>
        <itemListCard v-for="card in itemListCards" :key="card.name" :name="card.name" :body="card.body" :link="card.link" :price="card.price" :img="card.img">
        </itemListCard>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: {
    itemListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    sortMethod: "",
    sortMethodList: ["높은가격순", "낮은가격순"]
  }),
  methods:{
    sortByLowToHigh_price() {
      this.itemListCards.sort((a,b) => a['price'] < b['price'] ? -1 : 1)
    },
    sortByHighToLow_price() {
      this.itemListCards.sort((a,b) => a['price'] > b['price'] ? -1 : 1)
    },
    ccc() {
      if(this.sortMethod==="높은가격순") {
        this.sortByHighToLow_price();
      } else {
        this.sortByLowToHigh_price();
      }
    }
    
  }  
}
</script>
