<template>
    <v-layout>
    <!-- <v-flex class="col-xs-8 col-sm-6 col-md-4 col-lg-3"> -->
        <!-- <div class="col-12 col-xs-12 col-sm-6 col-md-4 col-lg-3">
        <card data-image="//thumbnail11.coupangcdn.com/thumbnails/remote/492x492ex/image/product/image/vendoritem/2019/04/18/4643931503/dd451310-4204-4862-a147-f828601c99b8.jpg">
            <h1 slot="header">아이패드</h1>
            <p slot="content">가격 1000만원</p>
            <p slot="content">________________________________</p>
        </card>
        </div>
        <div class="col-12 col-xs-12 col-sm-6 col-md-4 col-lg-3">
        <card data-image="https://view01.wemep.co.kr/wmp-product/5/451/190154515/pm_btsscw1hrwgo.jpg?1571018406">
            <h1 slot="header">아이패드</h1>
            <p slot="content">가격 1000만원</p>
            <p slot="content">________________________________</p>
        </card>
        </div>
        <div class="col-12 col-xs-12 col-sm-6 col-md-4 col-lg-3">
        <card data-image="https://image.shop.kt.com/upload/product/WL00050937/1557378259213.png">
            <h1 slot="header">아이패드</h1>
            <p slot="content">가격 1000만원</p>
            <p slot="content">________________________________</p>
        </card>
        </div>
        <div class="col-12 col-xs-12 col-sm-6 col-md-4 col-lg-3">
        <card data-image="https://cafefiles.pstatic.net/MjAxOTEwMTZfMjEz/MDAxNTcxMTk4MjI4ODA2.ZKnRywxA_gI0cQX8_N3H9gF_l49zevcXwz3WenBSViAg.nhXp3t0w2-Xp8vFR0RzZ2-ljevmzMNpDWk_scl_LzqAg.JPEG/E53E6D44-4F01-4D56-903F-811B83498D60.jpeg?type=s3">
            <h1 slot="header">아이패드</h1>
            <p slot="content">가격 1000만원</p>
            <p slot="content">________________________________</p>
        </card>
        </div> -->

        <!-- </div> -->
        <!-- <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
            helloworld
        </div>
        <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
            helloworld
        </div>
        <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
            helloworld
        </div>
        <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
            helloworld
        </div>

 -->
         <!-- <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
            helloworld
        </div>
         <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
            helloworld
        </div> -->
        
    <!-- </v-flex> -->

    <div>
    <v-layout row wrap>
       
        <v-flex d-flex xs12 sm6 md3>
            <card data-image="//thumbnail11.coupangcdn.com/thumbnails/remote/492x492ex/image/product/image/vendoritem/2019/04/18/4643931503/dd451310-4204-4862-a147-f828601c99b8.jpg">
                <h1 slot="header">아이패드</h1>
                <p slot="content">가격 1000만원</p>
                <p slot="content">________________________________</p>
            </card>
        </v-flex>
         <v-flex d-flex xs12 sm6 md3>
            <card data-image="//thumbnail11.coupangcdn.com/thumbnails/remote/492x492ex/image/product/image/vendoritem/2019/04/18/4643931503/dd451310-4204-4862-a147-f828601c99b8.jpg">
                <h1 slot="header">아이패드</h1>
                <p slot="content">가격 1000만원</p>
                <p slot="content">________________________________</p>
            </card>
        </v-flex>    
        <v-flex d-flex xs12 sm6 md3>
            <card data-image="//thumbnail11.coupangcdn.com/thumbnails/remote/492x492ex/image/product/image/vendoritem/2019/04/18/4643931503/dd451310-4204-4862-a147-f828601c99b8.jpg">
                <h1 slot="header">아이패드</h1>
                <p slot="content">가격 1000만원</p>
                <p slot="content">________________________________</p>
            </card>
        </v-flex>  
        <v-flex d-flex xs12 sm6 md3>
            <card data-image="//thumbnail11.coupangcdn.com/thumbnails/remote/492x492ex/image/product/image/vendoritem/2019/04/18/4643931503/dd451310-4204-4862-a147-f828601c99b8.jpg">
                <h1 slot="header">아이패드</h1>
                <p slot="content">가격 1000만원</p>
                <p slot="content">________________________________</p>
            </card>
        </v-flex>  
    </v-layout>
    </div>



    </v-layout>
    
</template>

<script>
import card from './card.vue'
export default {
    components: {
        card,
    },
    data(){
        return {

        }
    },
    
}
</script>
<style>
/* body {
  margin: 40px 0;
  font-family: "Raleway";
  font-size: 14px;
  font-weight: 500;
  background-color: #BCAAA4;
  -webkit-font-smoothing: antialiased;
} */

/* .title {
  font-family: "Raleway";
  font-size: 24px;
  font-weight: 700;
  color: #5D4037;
  text-align: center;
}

p {
  line-height: 1.5em;
}

h1 + p, p + p {
  margin-top: 10px;
} */

/* .container {
  padding: 40px 80px;
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
} */


</style>