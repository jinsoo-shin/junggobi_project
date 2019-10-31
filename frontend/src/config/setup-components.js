import ItemList from '../components/itemDetail/ItemList.vue'
import ItemListCard from '../components/itemDetail/ItemListCard.vue'
import Search from '../components/home/Search.vue'
import Tap from '../components/home/Tap.vue'
import Recommend from '../components/home/Recommend.vue'

import Headercomponent from '../components/home/Headercomponent.vue'
import DetailSearch from '../components/home/DetailSearch.vue'
import CheckBoxButton from '../components/home/CheckBoxButton.vue'

import MultipleChart from '../components/chart/MultipleChart.vue'
import SideMenu from '../components/itemDetail/SideMenu.vue'
import LoadingImg from '../components/LoadingImg.vue'
// import HistogramSlider from '../components/chart/HistogramSlider.vue'

function setupComponents(Vue){

    //main page 
    Vue.component('search', Search);                // 검색 창
    Vue.component('tap', Tap);                      // 
    Vue.component('recommend', Recommend);          // 
    Vue.component('headercomponent', Headercomponent);
    Vue.component('detailsearch', DetailSearch);
    Vue.component('checkboxbutton',CheckBoxButton);
    //item Detail page
    Vue.component('itemList', ItemList);            //detailpage - 검색 제품 목록
    Vue.component('itemListCard', ItemListCard);    //detailpage - 검색 제품 목록 내 아이템
    Vue.component('sideMenu', SideMenu)             //detailpage - 사이드바 ( 최근검색목록 등 출력 )
    
    //chart
    Vue.component('multipleChart', MultipleChart);  //최소값,평균값,최대값 가격 비교를 위한 차트
    Vue.component('loadingImg', LoadingImg);        //loading시 대체 이미지
    // Vue.component('histogramSlider', HistogramSlider);
  }
  
  
  export {
    setupComponents
  }
  