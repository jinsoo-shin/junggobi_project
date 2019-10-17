<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
        <!-- start : item-list -->
        <div xs7>
            ---------------itemDetailPage-------------
            <itemList :itemListCards="itemList"/>
        </div>
        <!-- end : item-list -->
        </v-layout>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        itemList : 
        [
            {name : "1" , body: "바디1", link: "http://www.naver.com", price: 500, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name: "3", body: "바디2", link: "http://www.daum.net", price: 1000, img : "https://i.pinimg.com/236x/7c/6c/6f/7c6c6f0108890f07cc7f6f6c2a40024d.jpg"},
            {name : "2" , body: "바디1", link: "http://www.naver.com", price: 300, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name: "4", body: "바디2", link: "http://www.daum.net", price: 4000, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name : "5" , body: "바디1", link: "http://www.naver.com", price: 200, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"},
            {name: "6", body: "바디2", link: "http://www.daum.net", price: 1000, img : "//image-notepet.akamaized.net/resize/620x-/seimage/20190705%2F300c8f262e69893db9d3c97fad37dc91.jpg"}

        ]
    }),
};
</script>
