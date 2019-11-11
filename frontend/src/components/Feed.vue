<template>
  <v-container
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>

      <feed-card
        v-for="(article, i) in paginatedArticles"
        :key="article.title"
        :size="layout[i]"
        :value="article"
      />
    </v-layout>

    <v-layout align-center>
      <v-flex xs3>
        <base-btn
          v-if="page !== 1"
          class="ml-0"
          title="Previous page"
          square
          @click="page--"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </base-btn>
      </v-flex>

      <v-flex
        xs6
        text-xs-center
        subheading
      >
        PAGE {{ page }} OF {{ pages }}
      </v-flex>

      <v-flex
        xs3
        text-xs-right
      >
        <base-btn
          v-if="pages > 1 && page < pages"
          class="mr-0"
          title="Next page"
          square
          @click="page++"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </base-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import FeedCard from "../components/FeedCard"
  import {
    mapState
  } from 'vuex'

  export default {
    name: 'Feed',
    components: {
      FeedCard
    },
    created(){
      this.articles = this.$store.getters["data/getBlogPosts"].data
    },
    data: () => ({
      layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3],
      page: 1,
      articles:[
//   {
//     "title": "애플 4분기 실적, 서비스·아이패드 이끌다",
//     "author": "블로터 닷넷",
//     "category": "애플",
//     "hero": "https://www.bloter.net/wp-content/uploads/2019/10/2019032718564546.png",
//     "url":"https://www.bloter.net/archives/359515"
//   },
//     {
//     "title": "애플 4분기 실적, 서비스·아이패드 이끌다",
//     "author": "블로터 닷넷",
//     "category": "애플",
//     "hero": "https://www.bloter.net/wp-content/uploads/2019/10/2019032718564546.png",
//     "url":"https://www.bloter.net/archives/359515"
//   },
]

    }),

    computed: {
      //  ...mapState(['articles']),
      pages () {
        return Math.ceil(this.articles.length / 11)
      },
      paginatedArticles () {
        const start = (this.page - 1) * 11
        const stop = this.page * 11

        return this.articles.slice(start, stop)
      }

    },

    watch: {
      page () {
        window.scrollTo(0, 0)
      }
    },
    methods: {
      eventA() {
        let a = this.$store.getters["data/getBlogPosts"]
      }
    }
  }
</script>
