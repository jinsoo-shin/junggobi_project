<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
        -------------itemListCardComponent---------------
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                   <v-list-item-content>
                <table>
                    <tr>
                      <v-dialog v-model="enlargeImg"  max-width="290">
                      <template v-slot:activator="{ on }">
                        <td rowspan="2"><v-img color="primary" dark v-on="on" :src="img" style="width:50px; height:50px"/></td>
                        
                      </template>
                      <v-card>
                        <v-img :src="img"/>
                      </v-card>
                      </v-dialog>
                    </tr>
                    <tr>
                      <td><v-list-item-title class="headline">{{ name }}</v-list-item-title></td>
                      <td><v-list-item-subtitle>{{ body }}</v-list-item-subtitle></td>
                      <td><v-btn><a :href="link">바로가기 링크</a></v-btn></td>
                      <td>{{ price }}</td>
                    </tr>
                </table>
                </v-list-item-content>
              </v-list-item>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>

export default {
  data: () => ({
      enlargeImg: false
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
