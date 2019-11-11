import axios from 'axios'

// const apiUrl = process.env.VUE_APP_API_URL

const apiUrl = '/api'

export default {

    test() {
        return axios.get(`${apiUrl}/product/`)
    },
    getBlogpost() {
        return axios.get(`${apiUrl}/news/`)
    },
    searchById(id) {
        return axios.get(`${apiUrl}/search/?search_word=`+id)
    }
}