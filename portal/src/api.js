import axios from 'axios';
const getApiService = () => {
    const token = JSON.parse(localStorage.getItem('token'));

    const apiService = {
        service: axios.create({
            // baseURL: 'http://localhost:5000/api/',
            baseURL: 'https://admin-grupo13.proyecto2022.linti.unlp.edu.ar/api/',
            withCredentials: false,
            //xsrfCookieName: 'csrf_access_token',
        }),
        servicesAuth: axios.create({
            //baseURL: 'http://localhost:5000/api/',
            baseURL: 'https://admin-grupo13.proyecto2022.linti.unlp.edu.ar/api/',
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