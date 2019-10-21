<!-- itemDetailPage 상세 페이지 -->
<template>
    <v-container grid-list-md text-center>        
    
        <!-- start : item-list -->
        <itemList :itemListCards="itemList"/>
        <!-- end : item-list -->
        
        <!-- start : sideMenu -->
        <sideMenu></sideMenu>
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
                <v-icon>mdi-plus</v-icon>
            </v-btn>
        </v-fab-transition>
        <!-- end : sideMenu -->
    
    </v-container>
</template>

<script>
export default {
    data: () => ({
        itemList : // 메인 페이지에서 전달 받은 데이터로 변경 해주세요.
        [   //name, gb, area, registrationDate, link, img
            {name: "갤럭시탭", gb: "32", area: "광주광역시 오선동", registrationDate: "2018.10.19", price: "200,000", link: "http://www.naver.com", img :"//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name: "아이패드", gb: "32", area: "광주광역시 수완동", registrationDate: "2018.10.18", price: "10,000", link: "http://www.naver.com", img :"https://i.pinimg.com/236x/7c/6c/6f/7c6c6f0108890f07cc7f6f6c2a40024d.jpg"},
            {name: "아이패드2", gb: "32", area: "목포시 상동", registrationDate: "2018.10.17", price: "140,000", link: "http://www.naver.com", img :"//thumbnail14.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2019/03/07/4202152557/a2a2758d-efaa-462a-a25b-d0dab4675f4f.jpg"},
            {name: "갤럭시s3", gb: "32", area: "서울시", registrationDate: "2018.10.16", price: "6,000", link: "http://www.naver.com", img :"//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name: "아이쇼핑", gb: "32", area: "강남", registrationDate: "2018.10.18", price: "50,000", link: "http://www.naver.com", img :"https://view01.wemep.co.kr/wmp-product/3/319/228623193/pm_75aamjb0kwud.jpg?1569558419"},
            {name: "어른패드", gb: "32", area: "첨단도시", registrationDate: "2018.10.19", price: "120,000", link: "http://www.naver.com", img :"https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcT7t3XH0xGjqrJDU6lQQMKiUo6EG0j_frk-IoG_3HGW_mHK0QO6fFw--31ycHd5wxIDtpRdpYNJ8aQsM69k590lrZoQQWgAtfnsGYrHtJLfgncMev16KPirJA&usqp=CAE"},
            {name: "아이키커", gb: "32", area: "미래동", registrationDate: "2018.10.20", price: "420,000", link: "http://www.naver.com", img :"//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},

        ]
    }),
    methods: {
        side() { 
            console.log("asdf")
            this.EventBus.$emit("sideMenu", true)
        }
    }
};
</script>
