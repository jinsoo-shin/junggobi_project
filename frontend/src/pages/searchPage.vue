<!-- itemDetailPage 상세 페이지 -->
<template>
    <v-container grid-list-md text-center>  
        <br/>
        <router-link to="/">
            <img src="./src/Untitled.png" alt="Vuetify.js" height="200">    
        </router-link>
        <center>
            <v-flex lg8>
                <v-text-field
                    v-model="model"
                    :placeholder="placeholder"
                    :rounded="rounded"
                    :solo="solo"
                    :clearable="clearable"
                    v-on:keyup.enter="searchById(model)"
                ></v-text-field>
            </v-flex>
        </center> 

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
        <itemList :itemList="itemList" ></itemList><!-- :itemPriceList="itemPriceList" -->


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
        model:"",
        placeholder: '상품을 검색하세요.',
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
                turnItemList : true;
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

<style scoped>
hr.type_3 {
  border: 0;
  height: 50px;
  width: 800px;
  background-image: url(Untitled1.png);
  background-repeat: no-repeat;
}
</style>
