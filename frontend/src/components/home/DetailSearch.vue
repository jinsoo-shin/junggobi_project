<template>
  <v-flex id="back">
    <div id="font1">검색 옵션</div>
    <v-row>
      <v-col cols="12" sm="6">
        <v-combobox
          :items="items"
          v-model="value"
          label="어떤 기기를 원하시나요?"
        ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value=='태블릿'">
          <v-combobox
            :items="tablet"
            v-model="value1"
            
            label="태블릿 종류를 고르세요"
          ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value1=='아이패드'">
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
      <v-col cols="12" sm="6" v-if="value1=='갤럭시탭'">
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
      <v-col cols="12" sm="6" v-if="value=='모바일/스마트폰'">
        <v-combobox
          v-model="value6"
          :items="mobile"
          
          label="제조사를 골라주세요"
        ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value6=='삼성전자 갤럭시'">
        <v-combobox
          v-model="value7"
          :items="gal_category"
          
          label="갤럭시"
        ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value7=='갤럭시 S'">
        <v-combobox 
          v-model="value8"
          :items="s_category"
          chips
          label="갤럭시 S라인"
        ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value7=='갤럭시 노트'">
        <v-combobox
          v-model="value9"
          :items="note_category"
          
          label="갤럭시 노트라인"
        ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value7=='그 외'">
        <v-combobox
          v-model="value10"
          :items="g_category"
          
          label="갤럭시 노트라인"
        ></v-combobox>
      </v-col>
      <v-col cols="12" sm="6" v-if="value6=='애플 아이폰'">
        <v-combobox
          v-model="value11"
          :items="iphone_category"
          
          label="아이폰 세대"
        ></v-combobox>
      </v-col>      
      <v-col cols="12" sm="6" >
        <center>
          <v-btn x-large color="blue lighten-2" dark id="font">
            <v-icon dark left>mdi-checkbox-marked-circle</v-icon> 검색
          </v-btn>
        </center>
      </v-col>
    </v-row>
  </v-flex>
</template>

<script>
export default {
  data () {
    return {
      value: ['어떤 기기를 원하세요?'],
      items: ['태블릿', '모바일/스마트폰'],
      value1: ['태블릿 종류를 고르세요'],
      tablet: ['아이패드', '갤럭시탭', '상관없음'],
      value2: ['크기'],
      ipad_size: ['16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB', '상관없음'],
      value3: ['종류'],
      ipad_category: ['미니','에어','프로'],
      value4: ['세대'],
      ipad_gene: ['1세대', '2세대', '3세대', '4세대', '5세대', '6세대', '7세대'],
      ipad_wifi: ['WIFI', '셀룰러'],
      value5: ['셀룰러/WIFI'],
      galaxy_category: ['A','E','S'],
      value6: ['제조사를 골라주세요'],
      mobile: ['삼성전자 갤럭시', '애플 아이폰'],
      iphone_category: ['상관없음', '11', '11 프로', 'XS', 'XS 플러스', 'XS MAX', 'XR', 'X',
      'S', '8 플러스', '8', '7 플러스', '7', '6S', '6 플러스', '6'],
      value7 : ['갤럭시 종류'],
      gal_category: ['갤럭시 S', '갤럭시 노트', '그 외', '상관없음'],
      value8 : ['갤럭시 S라인'],
      s_category : ['S10','S10플러스','S10E', 'S9', 'S9플러스', 'S8', 'S8플러스',
      'S7', 'S7엣지', 'S6', 'S5', 'S3'],
      value9 : ['갤럭시 노트라인'],
      note_category : ['10', '10플러스', '9', 'FE', '8', '8플러스', '7', '5', '4'],
      value10 : ['전체 갤럭시'],
      g_category : ['A30', 'A5', 'A7', 'A8', 'A9', 'J6'],
      value11 : ['아이폰 세대']
      
    }
  },
}
</script>

<style scoped>
#font {
  font-family: 'Cute Font', cursive;
  font-size: 25px;
}
#font1 {
  font-family: 'Cute Font', cursive;
  font-size: 60px;
}
</style>