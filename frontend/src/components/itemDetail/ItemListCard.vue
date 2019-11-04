<!-- itemListCard 아이템 출력 -->
<template>
<div>
      <!-- <v-card :elevation="hover ? 8 : 2"> -->
      
  <b-card 
    class="ml-2" 
    :img-src="item._source.img_src"
    img-height="320px"
    img-alt="Image"
    img-top
    style="width: 20rem; height: 40rem; margin: 10px"
  >
    <b-card-text>
      <p class="target1 title font-weight-black" v-html="item.highlight.title[0]"></p>
      <!-- <p class="target1 title font-weight-black	" v-html="item._source.title"></p> -->
      <div class="target2">
        <span v-for="(content,index) in item.highlight.contents" :key="index" v-html="content"></span>
      </div>
       <!-- class="target2" v-html="item.highlight.contents" -->
    </b-card-text>
    <span class="mdi mdi-star"></span>
    <span class="mdi mdi-star"></span>
    <span class="mdi mdi-star"></span>
    <span class="mdi mdi-star-half"></span>
    <span class="mdi mdi-star-outline"></span>
    <br/>

   {{item._source.price}}원
    <!-- <b-button variant="primary" >Go somewhere</b-button> -->
    <!-- <b-button squared variant="outline-secondary">Button</b-button> -->
   <template v-slot:footer>
       <b-list-group>
      <b-list-group-item>
 <v-btn text small color="error" @click="visitLink(item._source.link, item._source.price)">방문하기</v-btn>
    <v-btn text small @click="addItem">관심상품</v-btn>
    
    <v-btn @click="go">asdf</v-btn>
      </b-list-group-item>
      <!--거래방법 없어졌나요? 직거래?-->
    </b-list-group>
      <small class="text-muted">updated : {{item._source.date}}</small>
    </template>
  </b-card>
</div> 
</template>






<script>

export default {
  data: () => ({
    active: false,
  }),
  props: {
    item : { type: Object },
  },
  methods: {
    addItem() {
      let array = this.$store.getters['data/getFavoriteItems'];
      for(var i=0; i<array.length; i++){
        if(array[i]._id === this.item._id) {
          this.alertSwal("error")
          return;
        }
      }
      this.alertSwal("success")
      this.$store.commit("data/setAddFavoriteItems", this.item)
    },
    visitLink(link, price) {
      let routeData = this.$router.resolve({name: 'redirectPage', query: {link: link, price: price}});
      window.open(routeData.href, '_blank');
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
    go() {
      this.$router.push({ name : "itemPage", params: {item: this.item}})
    }
  }
};
</script>

<style>
.target2 {
 overflow: hidden;
 text-overflow: ellipsis;
 display: -webkit-box;
 -webkit-line-clamp: 2;
 -webkit-box-orient: vertical;
}
.target1 {
 overflow: hidden;
 text-overflow: ellipsis;
 display: -webkit-box;
 -webkit-line-clamp: 1;
 -webkit-box-orient: vertical;
}
</style>