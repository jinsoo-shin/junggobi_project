<template>
    <div id="app">
   <v-app light>
    <v-toolbar color="white">
      <v-toolbar-title>Log</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <section>
        <v-parallax src="http://file2.instiz.net/data/cached_img/upload/2016/05/09/23/7d931c39c52fe2837a5ec177e7223d36.jpg" height="600">
          <v-layout
            column
            align-center
            class="white--text"
          >
            <img src="./src/Untitled.png" alt="Vuetify.js" height="200">
            <h1 class="white--text mb-2 text-center" id="font">JunggoBi (중고비)</h1>
            <h1 class="subheading mb-4 text-center" id="main_font">저렴한 중고제품이 필요해!?</h1>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-12"
          align-center
        >
          <v-flex xs12 sm4 class="my-4">
            <div class="text-center">
              <h2 id="font">The best way to find Ipad, Iphone, Galaxy...</h2>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12>
                  <v-card flat class="transparent">
                    <v-card-text class="text-center">
                      <!-- <v-icon x-large class="blue--text text--lighten-2">mdi-flash </v-icon> -->
                      <!-- <h1 id="font"> 필요한 게 뭐에요? </h1> -->
                      <search/>
                    </v-card-text>
                    <br/>
                    <br/>
                    <center>
                      <hr class="type_3">
                    </center>
                    <br/>
                    <br/>
                    <detailsearch/>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>

      <section>
        <v-parallax src="http://file2.instiz.net/data/cached_img/upload/2016/05/09/23/dd22139d831d87ff1c2a096d5f42a400.jpg" height="380">
          <v-layout column align-center justify-center>
            <div class="white--text mb-4 text-center" id="main_font">가격이 이렇게까지 싸다고!?</div>
            <em id="font">가장 저렴한 제품 구경가기</em>
            <v-btn
              class="mt-12"
              color="blue lighten-2"
              dark
              large
              id="font"
              href="/pre-made-themes"
            >
              최저가 보러가기
            </v-btn>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-container grid-list-xl>
          <v-layout row wrap justify-center class="my-12">
            <v-flex xs12 sm4>
              <v-card flat class="transparent">
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">JunggoBi Info</div>
                </v-card-title>
                <v-card-text>
                  Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                  Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
                  Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 sm4 offset-sm1>
              <v-card flat class="transparent">
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">Contact us</div>
                </v-card-title>
                <v-card-text>
                  Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                </v-card-text>
                <v-list class="transparent">
                  <v-list-item>
                    <v-list-item-action>
                      <v-icon class="blue--text text--lighten-2">mdi-phone</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>777-867-5309</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-action>
                      <v-icon class="blue--text text--lighten-2">mdi-map-marker</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>Chicago, US</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-action>
                      <v-icon class="blue--text text--lighten-2">mdi-email</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>john@vuetifyjs.com</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <center>
          <hr class="type_3">
        </center>
        <br/>
        <br/>
      </section>

      <v-footer color="blue darken-2">
        <v-layout row wrap align-center>
          <v-flex xs12>
            <div class="white--text ml-4">
              Made with
              <v-icon class="red--text">mdi-heart</v-icon>
              by <a class="white--text" href="https://vuetifyjs.com" target="_blank">Vuetify</a>
              and <a class="white--text" href="https://github.com/vwxyzjn">Costa Huang</a>
            </div>
          </v-flex>
        </v-layout>
      </v-footer>
    </v-content>
  </v-app>
 </div>
</template>

<script>
export default {
  
}
</script>
<style scoped>
#font {
  font-family: 'Stylish', sans-serif;
  font-size: 30px;
}
#main_font {
  font-family: 'Stylish', sans-serif;
  font-size: 50px;
}
hr.type_3 {
  border: 0;
  height: 50px;
  width: 800px;
  background-image: url(Untitled1.png);
  background-repeat: no-repeat;
}
</style>
