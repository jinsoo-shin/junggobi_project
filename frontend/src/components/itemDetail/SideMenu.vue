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
        <v-list-item v-for="item in items" :key="item.idx">
          
          <!--start : favoriteItems 관심항목 출력 -->
          <v-hover v-slot:default="{ hover }">
          <div style="cursor: pointer;" onclick="window.open(${item.link},'_blank');">    <!-- 수정필요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--->
          <v-card 
            :elevation="hover ? 6 : 2"
            draggable="true"
            @dragstart="dragStart(item.idx, $event)"
            @dragover.prevent 
            @dragend="dragEnd" 
            @drop="dragFinish(item.idx, $event)"
            class="mt-2"
            max-width="344"
            outlined
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-2">{{item.title}}</div>
                <v-list-item-title class="mb-1">{{item.price}}</v-list-item-title>
                <v-list-item-subtitle>{{item.description}}</v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-avatar
                tile
                size="80"
              ><v-img  class="outlineImg" :src=item.img style="width:100px; height:100px"></v-img>
                    
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
      this.EventBus.$on("sideMenu", res=> {this.drawer=true; this.items = this.$store.getters.getFavoriteItems})
  },
  methods: {
    dragStart(which, ev) {
      console.log(ev)
      ev.dataTransfer.setData('Text', this.id);
      ev.dataTransfer.dropEffect = 'move'
      this.dragging = which;
    },
    dragEnd(ev) {
      this.dragging = -1
    },
     dragFinish(to, ev) {
      console.log(to + " df " + ev)
      this.moveItem(this.dragging, to);
      ev.target.style.marginTop = '2px'
      ev.target.style.marginBottom = '2px'
    },
    moveItem(from, to) {
      if (to === -1) {
        this.removeItemAt(from);
        this.$store.commit("setDeleteFavoriteItems", from)
        console.log("moveItem")
      } else {
        // this.todos.splice(to, 0, this.todos.splice(from, 1)[0]);
      }
    },
    removeItem(item) {
      // this.todos.splice(this.todos.indexOf(item), 1);
    },
    removeItemAt(index) {
      // this.todos.splice(index, 1);
    },
  }
}
</script>

<style>
.outlineImg { /*이미지 외곽선 css */
  max-width:95%;border:3px dashed #545565;
}
</style>