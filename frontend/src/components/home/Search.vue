<template>
<div>
    <v-col cols="12" sm="12" md="12">
        <v-text-field
            label="Outlined"
            placeholder="Placeholder"
            outlined
        ></v-text-field>
    </v-col>
</div>
</template>

<script>
export default {
    data()  {
        return {
            data1 : {},
        }
        
    },
    methods: {
        async searchAll(keyWord) {
            let searchData = new SearchData();
            const axios = require("axios");
            await axios({
            method: "GET",
            url: "http://localhost:8000/api/product",
            })
            .then(res => {
                data1 = res.data.data;
                console.log(data1)
            })
            .catch(function() {});
        },



    }

}
</script>

<style>

</style>