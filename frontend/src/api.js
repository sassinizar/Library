import axios from 'axios';

const BASE_URL = 'http://localhost:52690/api';

export const api = axios.create({
    baseURL: BASE_URL,
});

export const registerUser = (data) => api.post('/users/register', data);
export const loginUser = (data) => api.post('/users/login', data);
export const borrowMedia = (data) => api.post('/borrow', data);
export const returnMedia = (data) => api.post('/return', data);
export const addMedia = (data) => api.post('/medias/add', data);
export const updateMedia = (id, data) => api.put(`/medias/update/${id}`, data);
export const fetchMedia = async () => {
    return axios.get('http://localhost:52690/api/medias/all');
};
export const fetchBorrow = async () => {
    return axios.get('localhost:52690/api/borrowings/all');
};
export const deleteMedia = async (id) => {
    return axios.delete(`http://localhost:52690/api/medias/delete/${id}`);
};
