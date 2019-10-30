<template>
    <v-flex>
        <v-text-field
            v-model="model"
            :outlined="outlined"
            :rounded="rounded"
            :solo="solo"
            :clearable="clearable"
            v-on:keyup.enter="search"
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
        async search() {
            await this.$store.dispatch('data/test1').then(() => this.$router.push({ name :"itemDetailPage"}));
        }
    }
}
</script>

<style>
/* #font {
    color: rgb(96, 172, 235);
} */
</style>