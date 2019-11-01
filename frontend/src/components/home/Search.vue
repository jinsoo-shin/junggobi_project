<template>
    <v-flex>
        <v-text-field
            v-model="model"
            :outlined="outlined"
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
        value: '',
        model: '',
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
                console.log(res)
                let valueMaxMin = this.checkMaxMinValue(res);
                this.$store.commit('data/setValueMaxMin', valueMaxMin)
                this.$router.push({ name : "itemDetailPage"})
                this.EventBus.$emit("changedItemList");
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