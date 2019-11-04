<!-- itemDetailPage 상세 페이지 -->
<template>
<v-container grid-list-md text-center>  
    <v-flex>
        <v-text-field
            v-model="value"
            :outlined="outlined"
            :rounded="rounded"
            :solo="solo"
            :clearable="clearable"
            v-on:keyup.enter="searchById(value)"
        ></v-text-field>
    </v-flex> 
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
    <itemList :itemList="itemList" :itemPriceList="itemPriceList"></itemList>

    <!-- end : item-list -->
    
    <!-- start : sideMenu -->
    <sideMenu></sideMenu>
    <!-- end : sideMenu -->
    <v-btn
    v-scroll="onScroll" v-show="fab"
    fab dark fixed bottom right
    color="primary" @click="toTop"
  >
    <v-icon>keyboard_arrow_up</v-icon>
  </v-btn> 
</v-container>
</template>

<script>
export default {
    name: "searchPage",
    data: () => ({
        value: '',
        outlined: true,
        rounded: true,
        solo: true,
        clearable: true,
        itemList: [],
        itemPriceList : [],
        fab: false,
    }),
    methods: {
        side() { 
            this.EventBus.$emit("sideMenu", true)
        },
        async searchById(id) {
            await this.$store.dispatch('data/searchById', id)
            .then(res => {
                this.EventBus.$emit("changedItemList");
                this.itemList = res;
                this.getPriceList();
                this.EventBus.$emit("search")
            })
        },
        getPriceList() {
            for(var i=0; i<this.itemList.length; i++){
                this.itemPriceList[i] = this.itemList[i]._source.price;
            }
        },
        onScroll (e) {  // 맨위로 이동
            if (typeof window === 'undefined') return
                const top = window.pageYOffset ||   e.target.scrollTop || 0
                this.fab = top > 20
        },
        toTop () {      // 맨위좌표 기억
            this.$vuetify.goTo(0)
        },
    },
    created() {
        this.itemList = this.itemListSub;
        this.$vuetify.goTo(0)
    },
    props: {
        itemListSub : {
            type: Array , default: () => new Array()
        }
    }
};
</script>
