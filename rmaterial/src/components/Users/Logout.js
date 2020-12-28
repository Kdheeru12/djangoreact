import React ,{useEffect} from 'react';
import { useHistory } from 'react-router';
import { AxiosSend } from './Axios';


const Logout = () => {
    const history = useHistory()
    useEffect(() => {
        const res = AxiosSend.post(`logout`,{
            refresh_token: localStorage.getItem('refresh_token'),
        })
        .then
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        AxiosSend.defaults.headers['Authorization'] = null
        history.push('/')
    }, [])
    return (
        <div>
            bb
        </div>
    );
}

export default Logout;
