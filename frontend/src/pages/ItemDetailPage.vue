<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
        <!-- start : item-list -->
        <v-flex xs7>
            ---------------itemDetailPage-------------
            <itemList :itemListCards="itemList"/>
        </v-flex>
        <!-- end : item-list -->
        </v-layout>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        itemList : 
        [
            {name : "1" , body: "바디1", link: "http://www.naver.com", price: 500},
            {name: "2", body: "바디2", link: "http://www.daum.net", price: 1000},
            {name : "3" , body: "바디1", link: "http://www.naver.com", price: 300},
            {name: "4", body: "바디2", link: "http://www.daum.net", price: 4000},
            {name : "5" , body: "바디1", link: "http://www.naver.com", price: 200},
            {name: "6", body: "바디2", link: "http://www.daum.net", price: 1000}

        ]
    }),
};
</script>
