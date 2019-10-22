<!--itemList component 아이템 목록 -->
<template>
  <v-container class="pa-2" fluid grid-list-md>
    <div>
      <v-flex>
        <v-row>
          
          <!-- start : avgChart 평균가 차트 -->
          <v-col align-self="center">
            <div class="hidden-sm-and-down" style="cursor:pointer" @click="avgChart = true" >
              <v-alert type="info">
                시세 변동 차트 확인
              </v-alert>
            </div>
            <v-snackbar color="white" v-model="avgChart" :timeout="timeout">
            <v-col>
              <v-row>
                <multipleChart></multipleChart>
              </v-row>
              <v-row justify="end" >
                <v-btn color="grey" text @click="avgChart = false">Close</v-btn>
              </v-row>
            </v-col>
            </v-snackbar>
          </v-col>
          <!-- end : avgChart -->

          <!-- start : sort_methods 정렬방법 설정 -->
          <v-col class="mt-2">
            <v-row>
              <v-select
              v-model="sortMethod"
              :items="sortMethodList"
              label="정렬방법"
              dense
              solo
              @change="sortyBy()"
              ></v-select>
            </v-row>
            <v-row justify="end">
              {{itemLen()}}
            </v-row>
          </v-col>
          <!-- end : sort_methods -->
        
        </v-row>
        <v-row>
        
          <!-- start : itemListCards 아이템 리스트 출력 -->
          <v-col>
            <itemListCard v-for="card in itemListCards" :key="card.name" :item="card" class="mt-1"></itemListCard>
          </v-col>
          <!-- end : itemListCards -->
        
        </v-row>
      </v-flex>
    </div>
  </v-container>
</template>

<script>
export default {
  props: {
    itemListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    avgChart: false,  // 평균 비교 차트
    timeout: 10000,   // 차트 생존 시간
    sortMethod: "",   // 정렬 방법
    sortMethodList: ["높은가격순", "낮은가격순"]  // 정렬 방법 리스트
  }),
  methods:{
    sortByLowToHigh_price() { // 정렬 - 낮은가격순
      this.itemListCards.sort((a,b) => a['price'] < b['price'] ? -1 : 1)
    },
    sortByHighToLow_price() { // 정렬 - 높은가격순
      this.itemListCards.sort((a,b) => a['price'] > b['price'] ? -1 : 1)
    },
    sortyBy() { //select 된 정렬 방법 메소드 실행
      if(this.sortMethod==="높은가격순") {
        this.sortByHighToLow_price();
      } else {
        this.sortByLowToHigh_price();
      }
    },
    itemLen() { // 검색된 데이터 정보 양 출력
      return "검색 결과 : " + this.itemListCards.length + " 건";
    },
  }  
}
</script>
