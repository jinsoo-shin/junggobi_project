<!-- itemDetailPage 상세 페이지 -->
<template>
    <v-container grid-list-md text-center>        
        <h1>junggobi</h1>
        <v-divider></v-divider>
        <p class="font-weight-black" style="color:indigo">판매가격 {{ numberWithCommas(price) }} </p>
        
        <!-- start : progressBar 출력 -->
        <v-layout class="justify-center">
            <v-progress-circular
                :rotate="90"
                :size="500"
                :width="40"
                :value="value"
                color="red"
            >
                <!-- {{ value }} -->
                {{ link }}<br>
                해당 사이트로 이동 중입니다.<br>
                잠시만 기다려주세요.
            </v-progress-circular>
        </v-layout>
        <!-- end : progressBar -->

    </v-container>
</template>

<script>
export default {
    data: () => ({
        interval: {},
        value: 0,   // progressbar percent
        link: "",   
        price: 0,
    }),
    methods: {
        openLink(link) {    // 페이지 오픈
            window.location.assign(link)
        },
        numberWithCommas(x) {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }
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
</style>