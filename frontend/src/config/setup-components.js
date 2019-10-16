import ItemList from '../components/itemDetail/ItemList.vue'
import ItemListCard from '../components/itemDetail/ItemListCard.vue'
import Search from '../components/home/Search.vue'
import Tap from '../components/home/Tap.vue'
import Recommend from '../components/home/Recommend.vue'

function setupComponents(Vue){

    //main page 
    Vue.component('search', Search);                // 검색 창
    Vue.component('tap', Tap);                      // 
    Vue.component('recommend', Recommend);          // 

    //item Detail page
    Vue.component('itemList', ItemList);            //detailpage - 검색 제품 목록
    Vue.component('itemListCard', ItemListCard);    //detailpage - 검색 제품 목록 내 아이템
  }
  
  
  export {
    setupComponents
  }
  