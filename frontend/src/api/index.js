import axios from 'axios'

const apiUrl = '/api'

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
