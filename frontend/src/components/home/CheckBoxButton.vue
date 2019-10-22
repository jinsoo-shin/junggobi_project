<template>
    <div id="app">
        <input type="checkbox" v-model ="objectData" true-value='yes' false-value='no'>
        <label for="jack">{{this.objectData}}}</label>
        <input type="checkbox" true-value='yes' false-value='no' v-model="objectKey">
        <label for="john">{{this.objectKey}}</label>
        <input type="checkbox" true-value='yes' false-value='no' v-model="objectValue">
        <label for="mike"><span>{{this.objectValue}}</span></label>
        <br>
        <span>체크한 이름: </span>
    </div>
</template>
<script>
export default {
    data() {
        return{
            
        }
    },
    props: {
    objectData:{type:Object},
    objectKey:{type:String},
    objectValue:{type:Array},
},
}
</script>
<style>

</style>