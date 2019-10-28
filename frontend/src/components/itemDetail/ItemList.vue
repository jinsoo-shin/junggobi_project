<!--itemList component 아이템 목록 -->
<template>
  <v-container class="pa-2" fluid grid-list-md>
    <div>
      <v-flex>
        <v-row>
          
          <!-- start : sort_methods 정렬방법 설정 -->
          <v-col>
            <v-row>
              <v-select
                v-model="sortMethod"
                :items="sortMethodList"
                label="정렬방법"
                dense
                :hint=itemLen()
                persistent-hint
                @change="sortyBy()"
              ></v-select>
            </v-row>
          </v-col>
          <!-- end : sort_methods -->

          <!-- start : avgChart 평균가 차트 -->
          <v-col align-self="center">
            <div class="hidden-sm-and-down" style="cursor:pointer" @click="avgChart = true" >
              <v-alert outlined dense color="info">
                <span class="mdi mdi-poll-box"></span> 
                가격 변동 
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

        </v-row>
        <v-row>
        
          <!-- start : itemListCards 아이템 리스트 출력 -->
          <v-col>
            <!-- <itemListCard v-for="card in itemListCards" :key="card.name" :item="card" class="mt-1"></itemListCard> -->
            <itemListCard v-for="i in itemListCards.length > length ? length : itemListCards.length"
              :key="i" :item="itemListCards[i]" class="mt-1"/>
          </v-col>
          <!-- end : itemListCards -->
        
        </v-row>
        <v-row>
          <v-col>
            <v-btn outlined @click = "loadMore">더보기</v-btn>
          </v-col>
          <v-col>
            <v-btn outlined>Top</v-btn>
          </v-col>
        </v-row>
      </v-flex>
      <v-btn
            v-scroll="onScroll"
            v-show="fab"
            fab
            dark
            fixed
            bottom
            right
            color="primary"
            @click="toTop"
          >
          <v-icon>keyboard_arrow_up</v-icon>
          </v-btn>
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
    sortMethodList: ["높은가격순", "낮은가격순"], // 정렬 방법 리스트
    length: 3,
    fab: false
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
    loadMore() {
      this.length += 20;
      if (this.length >= this.itemListCards.length) this.more = false;
    },
    onScroll (e) {
      if (typeof window === 'undefined') return
      const top = window.pageYOffset ||   e.target.scrollTop || 0
      this.fab = top > 20
    },
    toTop () {
      this.$vuetify.goTo(0)
    }
  }  
}
</script>
