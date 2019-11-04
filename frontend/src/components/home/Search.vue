<template>
    <v-flex>
        <v-text-field
            v-model="model"
            :placeholder="placeholder"
            :rounded="rounded"
            :solo="solo"
            :clearable="clearable"
             v-on:keyup.enter="searchById(model)"
        ></v-text-field>
    </v-flex>
</template>

<script>
export default {
    data: () => ({
        model:"",
        placeholder: '상품을 검색하세요.',
        outlined: true,
        rounded: true,
        solo: true,
        clearable: true
    }),
    methods: {
        // async search() {
        //     await this.$store.dispatch('data/test1').
        //     then(res => {
        //         this.$store.commit('data/checkCheapCost', res)
        //         this.$store.commit('data/checkExpenCost', res)
                
        //         this.$router.push({ name :"itemDetailPage", 
        //         params: {
        //             itemList : res, 
        //             min : this.$store.getters['data/getCheapCost'], 
        //             max : this.$store.getters['data/getExpenCost']
        //         }});
        //     });
        // }
        checkMaxMinValue(list) { 
            let max = Math.max.apply(Math, list.map(function(o) { return o._source.price }))
            let min = Math.min.apply(Math, list.map(function(o) { return o._source.price }))
            return {max, min}
        },
        async searchById(id) {
            await this.$store.dispatch('data/searchById', id)
            .then(res => {
                // let valueMaxMin = this.checkMaxMinValue(res);
                // this.$store.commit('data/setValueMaxMin', valueMaxMin)
                // this.$router.push({ name : "itemDetailPage"})
                // this.EventBus.$emit("changedItemList");
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
/* #font {
    color: rgb(96, 172, 235);
} */
</style>