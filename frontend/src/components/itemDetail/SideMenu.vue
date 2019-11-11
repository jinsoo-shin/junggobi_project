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
        <v-list-item-content>
        <v-hover v-slot:default="{ hover }">
        <div id="div1"
          style="width:300px;"
          @dragover.prevent 
          @drop="dragFinish(-1, $event)">
            <v-alert dense outlined color="indigo" :elevation="hover ? 6 : 2">
              <span class="mdi mdi-delete-empty mdi-24px"></span>
            </v-alert>
        </div>
        </v-hover>
        </v-list-item-content>
      </v-list-item>
      
      <v-divider></v-divider>

      <v-list dense>
        <v-list-item-title>관심 항목</v-list-item-title> 
          
        <v-list-item v-for="item in items" :key="item._id">
          
          <!--start : favoriteItems 관심항목 출력 -->
          <v-hover v-slot:default="{ hover }">
          <div style="cursor: pointer;" @click="openUrl(item._source.link, item._source.price)">
          <v-card 
            :elevation="hover ? 6 : 2"
            draggable="true"
            @dragstart="dragStart(item._id, $event)"
            @dragover.prevent 
            @dragend="dragEnd" 
            @drop="dragFinish(item._id, $event)"
            class="mt-2"
            max-width="230"
            outlined
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-2">{{item._source.model_name}}</div>
                <v-list-item-title class="mb-1">{{item._source.price}}</v-list-item-title>
                <v-list-item-subtitle>{{item._source.contents}}</v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-avatar
                tile
                size="80"
              ><v-img  class="outlineImg" :src=item._source.img_src style="width:100px; height:100px"></v-img>
                    
              </v-list-item-avatar>
            </v-list-item>

            <!-- <v-card-actions>
              <v-btn text>Button</v-btn>
              <v-btn text>delete</v-btn>
            </v-card-actions> -->
          </v-card>
          </div>
          </v-hover>
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
      this.EventBus.$on("sideMenu", res=> {this.drawer=true; this.items = this.$store.getters['data/getFavoriteItems']})
  },
  methods: {
    dragStart(which, ev) {
      ev.dataTransfer.dropEffect = 'move'
      this.dragging = which;
    },
    dragEnd(ev) {
      this.dragging = -1
    },
     dragFinish(to, ev) {
      this.moveItem(this.dragging, to);
      ev.target.style.marginTop = '2px'
      ev.target.style.marginBottom = '2px'
    },
    moveItem(from, to) {
      if (to === -1) {
        this.$store.commit('data/setDeleteFavoriteItems', from)
      }
    },
    openUrl(link, price) {  // url 연결페이지로
      let routeData = this.$router.resolve({name: 'redirectPage', query: {link: link, price: price}});
      window.open(routeData.href, '_blank');
    },
  }
}
</script>

<style>
.outlineImg { /*이미지 외곽선 css */
  max-width:95%;border:3px dashed #545565;
}
</style>