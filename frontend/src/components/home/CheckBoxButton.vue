<template>
    <form action="">
        <fieldset class="options">
            <legend>Checkbox</legend>
            <ul>
                <li><input id="checkbox1" value="hi1" name="checkbox" type="checkbox" @click="clickcheck()" v-model="this.checkedNames['hi1']"> <label for="checkbox1" >Choice A</label></li>
                <li><input id="checkbox2" value="hi2" name="checkbox" type="checkbox" @click="clickcheck()" v-model="this.checkedNames['hi2']"> <label for="checkbox2">Choice B</label></li>
                <li><input id="checkbox3" value="hi3" name="checkbox" type="checkbox" @click="clickcheck()" v-model="this.checkedNames['hi3']"> <label for="checkbox3">Choice C</label></li>
            </ul>
        </fieldset>
    </form>    
</template>
<script>
export default {
    data : {
        checkedNames : {'hi1':'',
                        'hi2':'',
                        'hi3':'',
        },
    },
    methods: {
        clickcheck(){
            console.log("hihihihihi")
            console.log(this.checkedNames)
        }
    }
    
}
</script>
<style lang="stylus">

</style>