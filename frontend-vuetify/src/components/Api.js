  import axios from 'axios';

export default axios.create({
    baseURL: "https://backend-chile-test.herokuapp.com/api/",
    responseType: "json",
});