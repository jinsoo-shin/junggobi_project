<!--itemList component 아이템 목록 -->
<template>
  <v-container class="pa-2" fluid grid-list-md>
    <div>
      {{data}}
    </div>
  </v-container>
</template>

<script>

export default {
  data: () => ({ }),
  methods:{},
  props :{ 
    data : { type: Array }
  }
}
</script>
