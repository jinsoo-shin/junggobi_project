<template>
    <div id="app">
        <!-- <input type="checkbox" v-model ="objectData" true-value='yes' false-value='no'>
        <label for="jack">{{this.objectData}}}</label>
        <input type="checkbox" true-value='yes' false-value='no' v-model="objectKey">
        <label for="john">{{this.objectKey}}</label>
        <input type="checkbox" true-value='yes' false-value='no' v-model="objectValue">
        <label for="mike"><span>{{this.objectValue}}</span></label> -->
        <li v-for="(eachValue,index) in objectValue" :key=index>
            <button v-on:click="clickevent(eachValue)">
            <input type="checkbox" id="$`eachValue`" value="$`eachValue`" >
            </button>
            <label for="$`eachValue`">{{eachValue}}</label>  
        </li>

        <br>
        <span>체크한 이름: </span>
    </div>
</template>
<script>
export default {
    data() {
        return{
            selected:[],
            
        }
    },
    props: {
    objectData:{type:Object},
    objectKey:{type:String},
    objectValue:{type:Array},
    },
    methods:{
        clickevent(da) {
            let idx = this.selected.indexOf(da)
            if (idx > -1) {
                this.selected.splice(idx,1)
            } else {
                this.selected.push(da)
        }
        console.log(this.selected)
        }
    }
}
</script>
<style>

</style>