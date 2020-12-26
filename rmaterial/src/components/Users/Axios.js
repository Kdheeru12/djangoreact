import axios from 'axios'

const Baseurl = 'http://127.0.0.1:8000/api/'

// creating headers

const AxiosSend = axios.create({
    baseURL: Baseurl,
    timeout:5000,
    headers:{
        Authorization: localStorage.getItem('access_token')
                    ? 'JWT ' + localStorage.getItem('access_token')
                    :null,
                'Content-Type': 'application/json',
                accept: 'application/json',
    },
});

export {AxiosSend}