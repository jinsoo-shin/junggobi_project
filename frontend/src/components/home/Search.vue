<template>
<div>
    <v-col cols="12" sm="12" md="12">
        <v-text-field
            label="Outlined"
            placeholder="Placeholder"
            outlined
            v-on:keyup.enter='searchAll("hi")'
        ></v-text-field>
    </v-col>
</div>
</template>

<script>
export default {
    data()  {
        return {
            data1 : {'1':'2'},
        }
        
    },
    methods: {
        async searchAll(keyWord) {
            const axios = require("axios");
            await axios({
            method: "GET",
            url: "http://localhost:8000/api/product",
            })
            .then(res => {
                this.data1 = res.data.data;
                // this.data1 = res.data.data.keys('keyname')
                console.log(this.data1)
                return this.data1
            })
            .catch(function() {});
        },
        async goTodetail(proId) {
        this.$router.push({ name: "itemDetailPage", params: { 'id': this.data1 } });
        }




    }

}
</script>

<style>

</style>