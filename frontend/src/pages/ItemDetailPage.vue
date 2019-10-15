<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
        <!-- start : item-list -->
        <v-flex xs7>
            ---------------itemDetailPage-------------
            <ItemList :itemListCards="itemList" />
        </v-flex>
        <!-- end : item-list -->
        </v-layout>
    </v-container>
</template>

<script>
import ItemList from '../components/ItemList.vue'
export default {
    components: {
        ItemList
    },
    data: () => ({
        itemList : 
        [
            {name : "이름1" , body: "바디1", link: "http://www.naver.com"},
            {name: "이름2", body: "바디2", link: "http://www.daum.net"}
        ]
    }),
};
</script>
