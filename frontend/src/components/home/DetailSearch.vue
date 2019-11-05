<template>
  <v-flex id="back">
    <v-sheet
      elevation="12"
      class="pa-12"
    >
      <div id="font1">검색 옵션</div>
      <v-row>
        <v-col>
          <v-combobox
            :items="items"
            v-model="value"
            label="어떤 기기를 원하시나요?"
          ></v-combobox>
        </v-col>
        <v-col v-if="value=='태블릿'">
            <v-combobox
              :items="tablet"
              v-model="value1"
              
              label="태블릿 종류를 고르세요"
            ></v-combobox>
        </v-col>
        <v-col v-if="value1=='아이패드'">
          <v-combobox
            :items="ipad_category"
            v-model="value3"
            label="아이패드 종류"
          ></v-combobox>
          <v-combobox
            :items="ipad_gene"
            v-model="value4"
            label="아이패드 세대"
          ></v-combobox>
            <v-combobox
            :items="ipad_wifi"
            v-model="value5"
            label="셀룰러/WIFI"
          ></v-combobox>
            <v-combobox
            :items="ipad_size"
            v-model="value2"
            label="태블릿 크기"
          ></v-combobox>
        </v-col>
        <v-col v-if="value1=='갤럭시탭'">
          <v-combobox
            :items="galaxy_category"
            v-model="value3"
            
            label="갤럭시탭 종류"
          ></v-combobox>
            <v-combobox
            :items="ipad_wifi"
            v-model="value5"
            
            label="셀룰러/WIFI"
          ></v-combobox>
        </v-col>
        <v-col v-if="value=='모바일/스마트폰'">
          <v-combobox
            v-model="value6"
            :items="mobile"
            
            label="제조사를 골라주세요"
          ></v-combobox>
        </v-col>
        <v-col v-if="value6=='삼성전자 갤럭시'">
          <v-combobox
            v-model="value3"
            :items="s_category"
            label="갤럭시"
          ></v-combobox>
        </v-col>
        <v-col v-if="value6=='애플 아이폰'">
          <v-combobox
            v-model="value3"
            :items="iphone_category"
            
            label="아이폰 세대"
          ></v-combobox>
        </v-col>
      </v-row>
      <v-row>
        <v-col id="font">
          <mark>
            <strong>검색결과 : </strong>
            <span v-if="value1=='아이패드'">
              {{value1}}
            </span>
            <span v-if="value1=='갤럭시탭'">
              {{value1}}
            </span>
            <span v-if="value6=='삼성전자 갤럭시'">
              갤럭시
            </span>
            <span v-if="value6=='애플 아이폰'">
              아이폰
            </span>
            <span v-if="value3!='종류'">
              {{value3}}
            </span>
            <span v-if="value4!='세대'">
              {{value4}}
            </span> 
            <span v-if="value5!='셀룰러/WIFI'">
              {{value5}}
            </span> 
            <span v-if="value2!='크기'">
              {{value2}}
            </span>
          </mark>
        </v-col>
        <v-col cols="12">
          <v-btn right x-large color="blue lighten-2" dark id="font" @click="search_option()">
            <v-icon dark left>mdi-checkbox-marked-circle</v-icon> 검색
          </v-btn>
        </v-col>
      </v-row>      
    </v-sheet>
  </v-flex>
</template>

<script>
export default {
  data () {
    return {
      value: ['어떤 기기를 원하세요?'],
      items: ['태블릿', '모바일/스마트폰'],
      value1: ['태블릿 종류를 고르세요'],
      tablet: ['아이패드', '갤럭시탭'],
      value2: ['크기'],
      ipad_size: ['16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB'],
      value3: ['종류'],
      ipad_category: ['미니','에어','프로'],
      value4: ['세대'],
      ipad_gene: ['1세대', '2세대', '3세대', '4세대', '5세대', '6세대', '7세대'],
      ipad_wifi: ['WIFI', '셀룰러'],
      value5: ['셀룰러/WIFI'],
      galaxy_category: ['A','E','S'],
      value6: ['제조사를 골라주세요'],
      mobile: ['삼성전자 갤럭시', '애플 아이폰'],
      iphone_category: ['11', '11 프로', 'XS', 'XS 플러스', 'XS MAX', 'XR', 'X',
      'S', '8 플러스', '8', '7 플러스', '7', '6S', '6 플러스', '6'],
      value7 : ['갤럭시 종류'],
      s_category : ['S10','S10플러스','S10E', 'S9', 'S9플러스', 'S8', 'S8플러스',
      'S7', 'S7엣지', 'S6', 'S5', 'S3', '노트10', '노트10플러스', '노트9', '노트FE', '노트8', '노트8플러스', '노트7', '노트5', '노트4', 'A30', 'A5', 'A7', 'A8', 'A9', 'J6'],
      value11 : ['아이폰 세대']
      
    }
  },
    methods:{
      async search_option() {
          var search = ""
          if(this.value1=="아이패드")
            search += this.value1
          else if(this.value1=="갤럭시탭"){
            search += this.value1
          }
          if(this.value6=="삼성전자 갤럭시"){
            search += "갤럭시"
          }else if(this.value6=="애플 아이폰"){
            search += "아이폰"
          }
          if(this.value3!="종류"){
            search+=this.value3
          }
          if(this.value4!="세대"){
            search+=this.value4
          }
          if(this.value5!="셀룰러/WIFI"){
            search+=this.value5
          }
          if(this.value2!="크기"){
            search+=this.value2
          }
          console.log(search)
          await this.$store.dispatch('data/searchById', search)
          .then(res => {
              console.log(res)
              this.EventBus.$emit("changedItemList");
              this.itemList = res;
              this.EventBus.$emit("search")
              this.$router.push({ name : "searchPage", params: {itemListSub: res}})
          }
        )
      }
  }
}
</script>

<style scoped>
#font {
  font-family: 'Cute Font', cursive;
  font-size: 25px;
}
#font1 {
  font-family: 'Cute Font', cursive;
  font-size: 40px;
}

</style>