<template>
<div class="container">
  <div class="col-md-12">
    <div>
      <div class="row">
        <div class="col-12 col-md-4 offset-md-4">
          <v-row>
            <img :src="item._source.img_src" alt="">
          </v-row>
        </div>
      </div>

      <div>
        <h4>$ {{ item._source.price }}</h4>
        <h4> {{ item._source.title }}</h4>
        <p> {{ item._source.contents }} </p>
        <p> {{ item._source.storage }} </p>
        <p> {{ item._source.price }} </p>
        
      </div>
      <div>
        <p>
            <button @click="routerBack" class="btn btn-success">
                뒤로가기
            </button>
        </p>
         <img src="@/assets/gif/chart.gif" alt="차트보기">
      </div>
    </div>
  </div>
</div>
</template>


<script>


export default {
    data(){
        return {
            

        }
    },
    props: {
        item : { type: Object, default: () => new Object() },
    },
    methods: {
        routerBack() {
            this.$router.go(-1);
        }
    }
}
</script>