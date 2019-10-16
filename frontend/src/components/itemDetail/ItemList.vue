<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
        --------------itemListComponent---------------
        <!-- <v-flex pa-1> -->
            <!-- <itemListCard  v-for="card in myObjectSorted" :key="card.name" :name="card.name" :body="card.body" :link="card.link" :price="card.price"/> -->
        <!-- </v-flex> -->
        <ul>
          <!-- <li v-for="n in evenNumbers">{{n}}</li> -->
          {{itemListCards.price}}
          <li v-for="n in evenNumbers"></li>
        </ul>
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
    numbers: [1,2,3,4,5]
  }),
  computed: {
    evenNumbers() {
      console.log(this.itemListCards.price)
      return this.itemListCards.price
    }
  }
  
}
</script>
