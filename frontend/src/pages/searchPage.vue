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
        <itemList :data="itemList"/>
        <!-- end : item-list -->
        
        <!-- start : sideMenu -->
        <!-- <sideMenu></sideMenu> -->
        <!-- end : sideMenu -->
    
    </v-container>
</template>

<script>
export default {
    name: "itemDetailPage",
    data: () => ({
        value: '',
        outlined: true,
        rounded: true,
        solo: true,
        clearable: true,
        itemList: [],
    }),
    methods: {
        side() { 
            this.EventBus.$emit("sideMenu", true)
        },
        async searchById(id) {
            await this.$store.dispatch('data/searchById', id)
            .then(res => {
                console.log(res)
                this.EventBus.$emit("changedItemList");
                this.itemList = res;
                this.itemList = res;
            })
        }
    },
    created() {
    }
};
</script>
