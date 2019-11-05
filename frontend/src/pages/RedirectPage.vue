<!-- itemDetailPage 상세 페이지 -->
<template>
    <v-container grid-list-md text-center>  
        <img src="./src/Untitled.png" alt="Vuetify.js" height="100">      
        <h1 class="fontMain">junggobi</h1>

        <v-divider></v-divider>
        <p class="fontSub font-weight-black" style="color:indigo">판매가격 {{ numberWithCommas(price) }} </p>
        <!-- {{ value }} -->
        <p class="fontSub">
            {{ link }}<br>
        </p>
        <div>
            <b-alert show variant="success">
                <h4 class="alert-heading fontSub">해당 사이트로 이동 중입니다.</h4>
                <p class="fontSub">
                잠깐! 중고비에서 알려드립니다.
                중고비는 가격비교 정보 중개자로서 상품판매와는 직접적인 관련이 없습니다.<br>
                사이트로 이동 후 상품의 주문, 배송, 환불의 책임은 해당 쇼핑몰에 있습니다.<br>
                사이트로 이동 후 상품과 가격이 일치하는지 다시 한번 확인하시기 바랍니다.<br>
                </p>
                <hr>
                <p class="mb-0 fontSub">
                주문과정에서의 판매자의 현금 할인 직거래 및 타 계좌 유도를 하는 사이트가 있을 경우를 주의하세요.
                </p>
            </b-alert>
        </div>

        <!-- start : progressBar 출력 -->
        <v-layout class="justify-center">
            <v-progress-circular
                :rotate="90"
                :size="500"
                :width="20"
                :value="value"
                color="brown"
            >
            <lottie :options="defaultOptions" :height="400" :width="400" v-on:animCreated="handleAnimation"/>
        </v-progress-circular>
        </v-layout>
         <v-layout>
              
         </v-layout>
        <!-- end : progressBar -->
    </v-container>
</template>

<script>
import Lottie from '../components/lottie/lottie.vue';
import * as animationData from '../components/lottie/box.json';

export default {
    data: () => ({
        interval: {},
        value: 0,   // progressbar percent
        link: "",   
        price: 0,
        defaultOptions: {animationData: animationData.default},
        animationSpeed: 1
    }),
    components: {
      'lottie': Lottie
    },
    methods: {
        openLink(link) {    // 페이지 오픈
            window.location.assign(link)
        },
        numberWithCommas(x) {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
        handleAnimation: function (anim) {
            this.anim = anim;
        },
    },
    beforeDestroy () {  
      clearInterval(this.interval)
    },
    mounted () {    // interval 설정
        this.price = this.$route.query.price;
        this.link = this.$route.query.link;
        this.interval = setInterval(() => {
            if (this.value === 100) {   //완료시 진행될 일
                return this.openLink(this.link)
            }
            this.value += 20 // 정해진 시간당 오르는 게이지
        }, 1000)    // 시간단위
    },
}
</script>
<style scoped>
.v-progress-circular {
    margin: 1rem;
}
.fontMain {
  font-family: 'Cute Font', cursive;
  font-size: 30px;
}
.fontSub {
    font-family: 'Cute Font', cursive;
    font-size: 30px;
}
</style>