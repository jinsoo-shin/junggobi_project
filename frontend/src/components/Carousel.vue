<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        img-src="https://d2g44tvvp35wo2.cloudfront.net/photo/kr/2019/02/20/%EC%82%BC%EC%84%B1_Galaxy_S10%EF%BC%8B.jpg"
        style="height:550px;"
      >
        <h1 id="font2">삼성 전자 갤럭시 S10</h1>
        <p id="font2">안드로이드 10과 함께 더욱 새로워진 One UI, 갤럭시 S10에서 만나요</p>
      </b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide img-src="http://www.bloter.net/wp-content/uploads/2019/09/DSC03066.jpg"
        style="height:550px;"
      >
        <h1 id="font2">삼성전자 갤럭시 폴드</h1>
        <p id="font2">갤럭시 폴드 글로벌 버전의 스냅 드래곤 탑재, '환영할 일'</p>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide img-src="https://t1.daumcdn.net/cfile/tistory/995AAB4E5D46EBEF07"
        style="height:550px;"
      >
        <h1 id="font2">애플 맥북 중고제품 Comming Soon</h1>
      </b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide img-src="https://cdn.clien.net/web/api/file/F01/8775522/2be640820f8c3e.jpg?w=780&h=30000&gif=true"
        style="height:550px;"
      >
        <h1 id="font2">애플 아이패드 프로</h1>
        <p id="font2">'MS 서피스 프로 X vs. 12.9인치 아이패드 프로'··· 최고의 생산성 태블릿은?</p>
      </b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
      <b-carousel-slide img-src="https://pds.joins.com/news/component/htmlphoto_mmdata/201909/11/htm_20190911102258695034.JPG"
        style="height:550px;"
      >
        <h1 id="font2">애플 아이폰 11 Pro</h1>
        <p id="font2">아이폰11 PRO MAX 지속적인 흥행 요인은 에어팟2 프로모션</p>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>

<style scoped>
#font2 {
  font-family: 'Cute Font', cursive;
}
</style>