<template>
<div class="container">
  <div class="col-md-12">
    <div style="min-width:500px">
      <div>
        <div class="col-12 col-md-4 offset-md-4">
          <v-row>
            <img :src="item._source.img_src" alt="">
          </v-row>
        </div>
      </div>

      <div>
        <b-alert show variant="success">
        <h4> {{ item._source.title }}</h4>
        <p> {{ item._source.contents }} </p>
        <p> 기타 : {{ item._source.storage }} </p>
        <p> 가격 :{{ numberWithCommas(item._source.price) }} </p>
        </b-alert>
      </div>
      <div>
        <p>
            <button @click="routerBack" class="btn btn-success">
                뒤로가기
            </button>
        </p>
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
    },
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  }
}
</script>