import axios from 'axios'
import { error } from 'util';

const baseUrl='http://127.0.0.1:5000'

const config ={
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
}

export default {

  get: async (url = '', status) => {
    url = baseUrl + url + '?' + new Date().getTime();
    try {
        const response = await axios.get(url, config);
        return response.data;
    } catch (error) {
        console.log(error.response)
    }
  },


  post: async (url = '', data = {}) => {
    url = baseUrl + url;
    try{
        const response = await axios.post(url, data, config);
        //console.log(response)
        return response.data;
    }catch(error){
        console.log(error.response.status)
    }
    // return response;
  }
};

