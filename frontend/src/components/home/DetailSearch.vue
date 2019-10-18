<template>
    <div id="app">
    <v-app id="inspire">
        <v-stepper v-model="e6" vertical>
            <v-stepper-step :complete="e6 > 1" step="1">
                Select an app
                <small>Summarize if needed</small>
            </v-stepper-step>
        
            <v-stepper-content step="1">
                <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
                <v-btn color="primary" @click="e6 = 2">Continue</v-btn>
                <v-btn text>Cancel</v-btn>
            </v-stepper-content>
        </v-stepper>

        <v-card
            v-for="(item, index) in jsondata.data"
            v-bind:item="item"
            v-bind:index="index"
            v-bind:key="item.id"
        >{{item}} {{item.price}}</v-card>
    </v-app>
    </div>
</template>
<script>
export default {
    data() {
        return {
        e6: 0 ,
        jsondata:{
                data:[
                    {"id":1,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":3,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":2,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":4,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":5,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":10,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":9,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":6,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":11,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":12,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":13,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                    {"id":14,"price" :1000,"model":11, "gen":2,"display":3,"celluar":"wifi","capa":10,"region":"광주","date":3.23,"data_url": "www.naver.com","img_url" : 'www.daum.net',"sell":true,},
                ]
                
                
               
                
                
                
                
                
                
                
                
        }
            
        };

    },
    methods: {
        clickbtn: function () {
        // console.log(this.e13);
        this.e13 = this.e13 + 1;

        } }
    
}
</script>
<style>

</style>