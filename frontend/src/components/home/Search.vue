<template>
<div>
    <v-col cols="12" sm="12" md="12">
        <v-text-field
            label="Outlined"
            placeholder="Placeholder"
            outlined
            v-on:keyup.enter='searchAll("hi")'
        ></v-text-field>
        {{itemList}}
    </v-col>
</div>
</template>

<script>
export default {
    data()  {
        return {
            data1 : {'1':'2'},
            itemList: []
        }
        
    },
    methods: {
        async searchAll(keyWord) {
            await this.$store.dispatch('data/test1')
            this.itemList = this.$store.getters['data/getItems']
            this.$router.push('itemDetailPage');
        },
        async goTodetail(proId) {
        this.$router.push({ name: "itemDetailPage", params: { 'id': this.data1 } });
        }




    }

}
</script>

<style>

</style>