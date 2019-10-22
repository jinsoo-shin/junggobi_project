<template>
    <div id="app">
        <input type="checkbox" v-model ='checkedNames["hi1"]' true-value='yes' false-value='no'>
        <label for="jack">Jack</label>
        <input type="checkbox" true-value='yes' false-value='no' v-model="checkedNames['hi2']">
        <label for="john">John</label>
        <input type="checkbox" true-value='yes' false-value='no' v-model="checkedNames['hi3']">
        <label for="mike"><span>{{this.test}}</span></label>
        <br>
        <span>체크한 이름: {{ checkedNames }}</span>
    </div>
</template>
<script>
export default {
    data() {
        return
    },
    props: {
    data:{type:Object},
    manufacturer : {type:String},
    measureOfCapacity : {type:String},
    networkOfTheDevice : {type:String},
},
}
</script>
<style>

</style>