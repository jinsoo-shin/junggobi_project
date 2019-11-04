import axios from 'axios'

// const apiUrl = process.env.VUE_APP_API_URL

const apiUrl = '/api'

export default {
    //   searchMovies(params) {
    //     return axios.get(`${apiUrl}/movies/`, {
    //       params,
    //     })
    //   },
    test() {
        return axios.get(`${apiUrl}/product/`)
    },
    getBlogpost() {
        return axios.get(`${apiUrl}/news/`)
    }
}