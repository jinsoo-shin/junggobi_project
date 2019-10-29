<template>
    <!-- <div>
        <v-col cols="12" sm="12" md="12">
            <v-text-field
                label="상품검색"
                placeholder="아이패드, 아이폰, 갤럭시S, 갤럭시탭 등을 검색하세요."
                outlined
            ></v-text-field>
        </v-col>
    </div> -->
    <v-flex>
        <v-text-field
            v-model="value"
            color="rgb(27, 99, 158)"
            label="필요한 걸 찾아요!"
            placeholder="아이패드, 아이폰, 갤럭시S, 갤럭시탭 등을 검색하세요."
            loading
        >
            <template v-slot:progress>
                <v-progress-linear
                    v-if="custom"
                    :value="progress"
                    color="rgb(96, 172, 235)"
                    absolute
                    height="7"
                ></v-progress-linear>
            </template>
        </v-text-field>
    </v-flex>
</template>

<script>
export default {
    data: () => ({
        value: '',
        custom: true,
    }),
    computed: {
        progress () {
            return Math.min(100, this.value.length * 10)
        }
    }
}
</script>

<style>
/* #font {
    color: rgb(96, 172, 235);
} */
</style>