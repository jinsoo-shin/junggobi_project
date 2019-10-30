<template>
    <v-flex>
        <v-text-field
            v-model="model"
            :outlined="outlined"
            :rounded="rounded"
            :solo="solo"
            :clearable="clearable"
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
}
</script>

<style>
/* #font {
    color: rgb(96, 172, 235);
} */
</style>