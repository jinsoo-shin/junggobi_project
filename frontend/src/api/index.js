import axios from 'axios'

// const apiUrl = process.env.VUE_APP_API_URL

const apiUrl = '/api'

export default {
//   searchMovies(params) {
//     return axios.get(`52.78.203.0/api/movies/`, {
//       params,
//     })
//   },
    test() {
        return axios.get(`${apiUrl}/product/`)
    }
}
