import axios from 'axios';

const BASE_URL = 'http://localhost:5000/api';

export const api = axios.create({
    baseURL: BASE_URL,
});

export const registerUser = (data) => api.post('/users/register', data);
export const loginUser = (data) => api.post('/users/login', data);
export const fetchMedia = () => api.get('/media');
export const borrowMedia = (data) => api.post('/borrow', data);
export const returnMedia = (data) => api.post('/return', data);
