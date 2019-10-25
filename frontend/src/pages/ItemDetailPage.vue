<!-- itemDetailPage 상세 페이지 -->
<template>
    <v-container grid-list-md text-center>        
    <v-fab-transition>
            <v-btn
                @click="side"
                color="grey"
                fab
                dark
                small
                absolute
                right
            >
                <span class="mdi mdi-playlist-plus mdi-24px"></span>
            </v-btn>
        </v-fab-transition>

        <!-- start : item-list -->
        <itemList :itemListCards="itemList"/>
        <!-- end : item-list -->
        
        <!-- start : sideMenu -->
        <sideMenu></sideMenu>
        <!-- end : sideMenu -->
    
    </v-container>
</template>

<script>
export default {
    data: () => ({
        itemList: [],
        // itemList : // 메인 페이지에서 전달 받은 데이터로 변경 해주세요.
        // [   //name, gb, area, registrationDate, link, img
        //     {idx: 1, company: "samsung", title: "갤럭시탭", size: "32", status:"S급", shipping: "직거래", description:"액정이 파손되어서 버립니다. 싼가격에 가져가용 ㅎ", region: "광주광역시 오선동", registrationDate: "2018.10.19", price: "200,000", link: "http://www.naver.com", img :"//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
        //     {idx: 2, company: "apple", title: "아이패드", size: "32", status:"C급", shipping: "직거래", description:"램은 제가 뺐어요 ㅎㅎ 알아서 구하시길", region: "광주광역시 수완동", registrationDate: "2018.10.18", price: "10,000", link: "http://www.naver.com", img :"https://i.pinimg.com/236x/7c/6c/6f/7c6c6f0108890f07cc7f6f6c2a40024d.jpg"},
        //     {idx: 3, company: "apple", title: "아이패드2", size: "32", status:"B급", shipping: "택배", description:"생활 기스만 있어요", region: "목포시 상동", registrationDate: "2018.10.17", price: "140,000", link: "http://www.naver.com", img :"//thumbnail14.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2019/03/07/4202152557/a2a2758d-efaa-462a-a25b-d0dab4675f4f.jpg"},
        //     {idx: 4, company: "samsung", title: "갤럭시s3", size: "32", status:"S급", shipping: "택배", description:"사진 보는 그대로 S급 미개봉", region: "서울시", registrationDate: "2018.10.16", price: "6,000", link: "http://www.naver.com", img :"//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
        //     {idx: 5, company: "etc", title: "아이쇼핑", size: "32", status:"S급", shipping: "택배", description:"3번 썼어요 가져가세요.", region: "강남", registrationDate: "2018.10.18", price: "50,000", link: "http://www.naver.com", img :"https://view01.wemep.co.kr/wmp-product/3/319/228623193/pm_75aamjb0kwud.jpg?1569558419"},
        //     {idx: 6, company: "etc", title: "어른패드", size: "32", status:"A급", shipping: "직거래", description:"직거래 좋아요 !", region: "첨단도시", registrationDate: "2018.10.19", price: "120,000", link: "http://www.naver.com", img :"https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcT7t3XH0xGjqrJDU6lQQMKiUo6EG0j_frk-IoG_3HGW_mHK0QO6fFw--31ycHd5wxIDtpRdpYNJ8aQsM69k590lrZoQQWgAtfnsGYrHtJLfgncMev16KPirJA&usqp=CAE"},
        //     {idx: 7, company: "etc", title: "아이키커", size: "32", status:"B급", shipping: "직거래", description:"중봉이한테는 안팔아요.!", region: "미래동", registrationDate: "2018.10.20", price: "420,000", link: "http://www.naver.com", img :"//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},

        // ]
    }),
    methods: {
        side() { 
            this.EventBus.$emit("sideMenu", true)
        },
        async dis() {
            await this.$store.dispatch('data/test1')
            this.itemList = this.$store.getters['data/getItems']
        }
    },
    created() {
        this.dis();
    }
};
</script>
