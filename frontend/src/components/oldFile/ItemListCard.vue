<!-- itemListCard 아이템 출력 -->
<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">aaaa
      <!-- -------------itemListCardComponent--------------- -->
      <div text-center>aaaaaa
        <v-list-item>
          <v-list-item-content>
            <v-row>aaaaaafsdfsdf
        
              <!-- {{item}}
              ///sdfksdflsdjklfd
dfsafd -->aaaaaaaaaaaaaaaafsdafasfsda
              {{data}}
              <!-- start : itemImage - 아이템 이미지 출력 및 확대-->
              <!-- <v-col md="4" align-self="center">
                <v-dialog v-model="enlargeImg" max-width="30%">
                <template v-slot:activator="{ on }">
                  <v-img class="outlineImg" v-on="on" :src="item.img_src" style="width:200px; height:200px"/>
                </template>
                  <v-img :src="item.img_src"/>
                </v-dialog>
              </v-col> -->
              <!-- start : itemImage -->
              
              <!-- start : itemInfomation table - 아이템 정보 출력 부분-->
              <!-- <v-col md="6">
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                      <tr>
                        <th class="text-left">모델명</th>
                        <th class="text-left">{{item.model_name}}</th>
                      </tr>
                    </thead>
                    <thead>
                      <tr>
                        <th class="text-truncate"><tr>용량/</tr>등록일</th>
                        <th><tr>{{item.storage}}</tr>{{item.date}}</th>
                      </tr>
                    </thead>
                    <thead>
                      <tr>
                        <th>판매 지역</th>
                        <th>{{item.region}}</th>
                      </tr>
                    </thead>
                    <thead>
                      <tr>
                        <th>가격</th>
                        <th style="color:#489489">{{item.price}}</th>
                      </tr>
                    </thead>
                     <thead>
                      <tr>
                        <th>기타</th>
                        <th><span class="target">{{item.contents}}</span></th>
                      </tr>
                    </thead>
                  </template>
                </v-simple-table>
              </v-col>
              <v-col md="2" align-self="center">
                
                <v-btn text small color="error" @click="visitLink(item.link, item.price)">방문하기</v-btn>
                <v-btn text small @click="addItem">관심상품</v-btn>                     
              </v-col> -->
              <!-- end : itemInfomation table -->

            </v-row>
          </v-list-item-content>
        </v-list-item>
      </div>
    </v-card>
  </v-hover>
</template>






<script>

export default {
  data: () => ({
    enlargeImg: false,  // 이미지 확대
    data : [],
  }),
  props: {
    item: {
      type: Object,
      default: () => new Object(),
    }
  },
  methods: {
    addItem() {
      let array = this.$store.getters['data/getFavoriteItems'];
      for(var i=0; i<array.length; i++){
        if(array[i].id === this.item.id) {
          this.alertSwal("error")
          return;
        }
      }
      this.alertSwal("success")
      this.$store.commit("data/setAddFavoriteItems", this.item)
    },
    alertSwal(info) {
      const Toast = this.$swal.mixin({
        toast: true,
        position: 'center',
        showConfirmButton: false,
        timer: 3000
      })
      if(info==="success") {
        Toast.fire({
          type: 'success',
          title: '등록되었습니다.'
        })
      }else {
        Toast.fire({
          type: 'error',
          title: '이미 등록된 상품입니다..'
        })
      }
    },
    visitLink(link, price) {
      let routeData = this.$router.resolve({name: 'redirectPage', query: {link: link, price: price}});
      window.open(routeData.href, '_blank');
    },
  },
  created() {
    this.EventBus.$on("changedItemList",res => this.data = res)
  }
};
</script>

<style>
.outlineImg { /*이미지 외곽선 css */
  max-width:95%;border:3px dashed #545565;
}
.target {
 overflow: hidden;
 text-overflow: ellipsis;
 display: -webkit-box;
 -webkit-line-clamp: 2;
 -webkit-box-orient: vertical;
}

</style>