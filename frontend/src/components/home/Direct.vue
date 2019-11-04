<template>
    <v-container>
        <v-row dense>
            <v-col
                v-for="(item, i) in items"
                :key="i"
                cols="12"
                xs="12" lg="2" md="3"
            >
                <center>
                    <a href="#" @click="direct_move(item.idx)">
                        <v-avatar
                            class="ma-3"
                            size="125"
                            id="tag"
                        >
                            <v-img :src="item.src"></v-img>
                        </v-avatar>
                    </a>
                </center>
                <center id="font">{{item.title}}</center>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from "axios";
const apiUrl = "/api"

export default {
    data: () => ({
        value:"",
        items: [
            {
                title: "아이폰 XS, XR",
                src : "https://image.flaticon.com/icons/svg/2223/2223340.svg",
                idx : 0
            },
            {
                title: "아이폰 7, 8",
                src : "https://image.flaticon.com/icons/svg/148/148998.svg",
                idx : 1
            },
            {
                title: "아이폰 6 이하",
                src : "https://image.flaticon.com/icons/svg/164/164413.svg",
                idx : 2
            },
            {
                title: "아이패드 프로",
                src : "https://image.flaticon.com/icons/svg/644/644425.svg",
                idx : 3
            },
            {
                title: "아이패드 미니",
                src : "https://image.flaticon.com/icons/svg/273/273579.svg",
                idx : 4
            },
            {
                title: "아이패드 에어",
                src : "https://image.flaticon.com/icons/svg/125/125271.svg",
                idx : 5
            },
            {
                title: "갤럭시탭",
                src : "https://image.flaticon.com/icons/svg/204/204282.svg",
                idx : 6
            },
            {
                title: "갤럭시 폴드",
                src : "https://www.flaticon.com/premium-icon/icons/svg/1796/1796311.svg",
                idx : 7
            },
            {
                title: "갤럭시 S",
                src : "https://image.flaticon.com/icons/svg/254/254040.svg",
                idx : 8
            },
            {
                title: "갤럭시 노트",
                src : "https://image.flaticon.com/icons/svg/1373/1373263.svg",
                idx : 9
            },
            {
                title: "갤럭시",
                src : "https://image.flaticon.com/icons/svg/2152/2152553.svg",
                idx : 10
            },
            {
                title: "삼성전자 제품",
                src : "https://image.flaticon.com/icons/svg/882/882747.svg",
                idx : 11
            }
        ]
    }),
    methods:{
        async direct_move(id) {
            console.log(this.items[id].title)
            await this.$store.dispatch('data/searchById', this.items[id].title)
            .then(res => {
                console.log(res)
                this.EventBus.$emit("changedItemList");
                this.itemList = res;
                this.EventBus.$emit("search")
                this.$router.push({ name : "searchPage", params: {itemListSub: res}})
            })
        }
    }
}
</script>

<style>
#font {
  font-family: 'Cute Font', cursive;
  font-size: 30px;
}
#tag{
    background-color: rgb(233, 102, 102);
}

</style>