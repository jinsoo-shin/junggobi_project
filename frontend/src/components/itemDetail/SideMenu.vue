<!--itemList component 아이템 목록 -->
<template>
    <div>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      right
    >
      <v-list-item>
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>관심 항목</v-list-item-title> <span class="mdi mdi-delete-empty mdi-24px"></span>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>

        <v-list-item v-for="item in items" :key="item.idx">
              
          <!--start : favoriteItems 관심항목 출력 -->
          <v-card
            class="mx-auto"
            max-width="344"
            outlined
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-2">{{item.company}}</div>
                <v-list-item-title class="mb-1">{{item.title}}</v-list-item-title>
                <v-list-item-subtitle>{{item.description}}</v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-avatar
                tile
                size="80"
              ><v-img  class="outlineImg" :src=item.img style="width:100px; height:100px"></v-img>
                    
              </v-list-item-avatar>
            </v-list-item>

            <v-card-actions>
              <v-btn text>Button</v-btn>
              <v-btn text>delete</v-btn>
            </v-card-actions>
          </v-card>
          <!--end : favoriteItems -->
          
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </div>
</template>

<script>
export default {
    data () {
         return {
            drawer: null,
            items: {}
        }
    },
    created() {
        this.EventBus.$on("sideMenu", res=> {this.drawer=true; this.items = this.$store.getters.getFavoriteItems})
    }
}
</script>

<style>
.outlineImg { /*이미지 외곽선 css */
  max-width:95%;border:3px dashed #545565;
}
</style>