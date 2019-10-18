<template>
    <v-container grid-list-md text-center>
        
        <!-- start : item-list -->
            ---------------itemDetailPage-------------
            <itemList :itemListCards="itemList"/>
        <!-- end : item-list -->
    </v-container>
</template>

<script>
export default {
    data: () => ({
        itemList : 
        [
            {name : "아이패드" , body: "부서졌어요 ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ ㅁㅁㅁㅁ aaaaaaaaaaaaaaa aaaaaaaaaaa ㅁㅁㅁ", link: "http://www.naver.com", price: 500, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name: "아이패드3", body: "침수폰입니다.", link: "http://www.daum.net", price: 1000, img : "https://i.pinimg.com/236x/7c/6c/6f/7c6c6f0108890f07cc7f6f6c2a40024d.jpg"},
            {name : "어른패드" , body: "아주좋아요 깨끗", link: "http://www.naver.com", price: 300, img : "//thumbnail14.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2019/03/07/4202152557/a2a2758d-efaa-462a-a25b-d0dab4675f4f.jpg"},
            {name: "청년패드", body: "아주 박살났어요 ㅎ", link: "http://www.daum.net", price: 4000, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name : "아이패치" , body: "S급입니다.", link: "http://www.naver.com", price: 200, img : "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcT7t3XH0xGjqrJDU6lQQMKiUo6EG0j_frk-IoG_3HGW_mHK0QO6fFw--31ycHd5wxIDtpRdpYNJ8aQsM69k590lrZoQQWgAtfnsGYrHtJLfgncMev16KPirJA&usqp=CAE"},
            {name: "아이쇼핑", body: "미개봉입니다.", link: "http://www.daum.net", price: 1000, img : "https://view01.wemep.co.kr/wmp-product/3/319/228623193/pm_75aamjb0kwud.jpg?1569558419"}

        ]
    }),
};
</script>
