import axios from 'axios';
const getApiService = () => {
    const token = JSON.parse(localStorage.getItem('token'));

    const apiService = {
        service: axios.create({
            baseURL: 'http://localhost:5000/api/',
            withCredentials: false,
            //xsrfCookieName: 'csrf_access_token',
        }),
        servicesAuth: axios.create({
            baseURL: 'http://localhost:5000/api/',
            withCredentials: true,
            //xsrfCookieName: 'csrf_access_token',
            headers: {
                Authorization: `JWT ${token}`
            }
        })
    }
    return apiService;
}

export { getApiService };