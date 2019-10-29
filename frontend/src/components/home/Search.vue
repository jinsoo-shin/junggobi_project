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
            color="cyan darken"
            label="Text field"
            placeholder="Start typing..."
            loading
        >
            <template v-slot:progress>
                <v-progress-linear
                    v-if="custom"
                    :value="progress"
                    :color="color"
                    absolute
                    height="7"
                ></v-progress-linear>
            </template>
        </v-text-field>
    </v-flex>
</template>

<script>
export default {
computed: {
    progress () {
      return Math.min(100, this.value.length * 10)
    },
    color () {
      return ['error', 'warning', 'success'][Math.floor(this.progress / 40)]
    },
  }
}
</script>

<style>

</style>