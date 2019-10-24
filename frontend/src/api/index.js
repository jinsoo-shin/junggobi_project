import axios from 'axios'

const apiUrl = process.env.VUE_APP_API_URL

export default {
//   searchMovies(params) {
//     return axios.get(`${apiUrl}/movies/`, {
//       params,
//     })
//   },
    test() {
        return axios.get(`${apiUrl}/index/`)
    }
}
