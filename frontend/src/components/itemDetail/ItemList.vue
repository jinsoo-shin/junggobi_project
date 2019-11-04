<!--itemList component 아이템 목록 -->
<template>
<v-container class="pa-2" fluid grid-list-md>
  <v-layout>
    <v-flex >
    <v-row>
      <b-button v-b-toggle.collapse-3 class="m-1">정렬방법</b-button>
      <b-collapse invisible id="collapse-3">
        <b-form-select v-model="selected" :options="options" size="sm" class="mt-3" value="select"></b-form-select>
      </b-collapse>
      <div>

      <v-col align-self="center">
            <div class="hidden-sm-and-down" style="cursor:pointer" @click="avgChart = true" >
              <v-alert outlined dense color="info">
                <span class="mdi mdi-poll-box"></span> 
                가격 변동 
              </v-alert>
            </div>
            <v-snackbar color="white" v-model="avgChart">
            <v-col>
              <v-row>
                <multipleChart :chartDatas ='chartDatas'></multipleChart>
              </v-row>
              <v-row justify="end" >
                <v-btn color="grey" text @click="avgChart = false">Close</v-btn>
              </v-row>
            </v-col>
            </v-snackbar>
          </v-col>
      </div>
        <div class="mt-3"><strong> {{itemLen()}}</strong></div>
    </v-row>
    <!-- {{priceList}}
    <v-row>
       <HistogramSlider
            style="margin: 200px auto"
            :width="600"
            :bar-height="50"
            :data="priceList"
            :drag-interval="true"
            :force-edges="false"
            :colors="['#4facfe', '#00f2fe']"
            :min="chartLP"
            :max="chartRP"
            :step="10000"
          />
    </v-row> -->
    <carousel></carousel>
    <v-flex wrap>
      <v-row>
        <itemListCard v-for="i in NowItems.length > length ? length :NowItems.length"
          :key="i" :item="NowItems[i-1]" class="mt-1"/>
      </v-row>
    </v-flex>
    <v-row>
      <!-- start : loadMore button 더 보기 버튼 -->
      <v-col v-if="moreBtn">
        <v-btn outlined @click = "loadMore">더보기</v-btn>
      </v-col>
      <!-- end : loadMore -->
    </v-row>
    </v-flex>
  </v-layout>
  
</v-container>
</template>

<script>
import HistogramSlider from 'vue-histogram-slider';
import 'vue-histogram-slider/dist/histogram-slider.css';

export default {
  data: () => ({
    avgChart: false,
    chartDatas : {},
    moreBtn: true,      // 더보기버튼 출력
    NowItems : [],
    chartLP : 0,
    chartRP : 1000000,
    length: 9,
    
    selected: null,
    select :"",
    priceList : [],
    options: [
      { value: null, text: '정렬 옵션' },
      { value: 'lowPrice', text: '낮은 가격순' },
      { value: 'highPrice', text: '높은 가격순' },
      { value: 'nowDate', text: '최근순' },
      { value: 'oldDate', text: '오래된순' },
    ]
  }),
  methods:{
    itemLen() { // 검색된 데이터 정보 양 출력
      return "검색 결과 : " + this.NowItems.length + " 건";
    },
    sortyBy(action) { //select 된 정렬 방법 메소드 실행
      if(action==="highPrice") {
        this.sortByHighToLow_price();
      } else if(action==="lowPrice") {
        this.sortByLowToHigh_price();
      } else if(action==="nowDate") {
        this.sortByDateNow();
      } else {
        this.sortByDateOld();
      }
    },
    sortByLowToHigh_price() { // 정렬 - 낮은가격순
      this.NowItems = this.itemList;
      this.NowItems.sort((a,b) => a['_source']['price'] < b['_source']['price'] ? -1 : 1)
    },
    sortByHighToLow_price() { // 정렬 - 높은가격순
      this.NowItems = this.itemList;
      this.NowItems.sort((a,b) => a['_source']['price'] > b['_source']['price'] ? -1 : 1)
    },
    sortByDateNow(){
      this.NowItems = this.itemList;
      this.NowItems.sort(function(a,b){
        return new Date(b._source.date) - new Date(a._source.date);
      });
    },
    sortByDateOld(){
      this.NowItems = this.itemList;
      this.NowItems.sort(function(a,b){
        return new Date(a._source.date) - new Date(b._source.date); 
      });
    },
    loadMore() {  // 더보기 버튼 
      this.length += 9;
      if (this.length >= this.itemList.length) this.moreBtn = false;
    },
  },
  props :{ 
    itemList : { type: Array , default: () => new Array() },
    itemPriceList : { type: Array , default: () => new Array() }
  },
  created() {
    this.NowItems = this.itemList;
    this.EventBus.$on("search", () => {this.selected =null; } )
  },
  watch: {
    itemList :function(newVal, oldVal) {
      this.NowItems = this.itemList;
      this.priceList = this.itemPriceList
      this.chartDatas = this.$store.getters['data/getChartData']
    },
    selected :function(newVal, oldVal) {
      this.sortyBy(newVal);
    },
  },
}
</script>
