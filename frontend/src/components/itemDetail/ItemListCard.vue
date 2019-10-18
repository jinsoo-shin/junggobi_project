<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
        <!-- -------------itemListCardComponent--------------- -->
        <div text-center>
              <v-list-item>
                <v-list-item-content>
                  <v-row>
                    <v-col md="4">
                      <v-dialog v-model="enlargeImg"  max-width="290">
                      <template v-slot:activator="{ on }">
                        <v-img dark v-on="on" :src="img" style="width:200px; height:200px"/>
                      </template>
                      <v-card><v-img :src="img"/></v-card>
                      </v-dialog>
                    </v-col>
                    <v-col md="6">
                     



                    </v-col>
                    <v-col md="2">
                      <v-btn text small color="error" :href="link" target="_blank">방문하기</v-btn>                     
                    </v-col>
                  </v-row>
                </v-list-item-content>
              </v-list-item>
        </div>
    </v-card>
  </v-hover>


   <!-- <v-row style="height: 50px;">
                        <v-list-item-title>{{ price }}</v-list-item-title>
                      </v-row>
                      <v-row>
                        <v-list-item-title class="headline">{{ name }}</v-list-item-title>
                      </v-row>
                      <v-row>
                        <p>{{ body }}</p>
                      </v-row> -->
</template>






<script>

export default {
  data: () => ({
    enlargeImg: false,
    items: [
      {
        name: 'Frozen Yogurt',
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        sodium: 87,
        calcium: '14%',
        iron: '1%',
      },
    ]
  }),
  props: {
    name: {
      type: String,
      default: ""
    },
    body: {
      type: String,
      default: ""
    },
    link: {
      type: String,
      default: ""
    },
    price: {
      type: Number,
      default: 0
    },
    img: {
      type: String,
      default: ""
    }
  },
};
</script>
