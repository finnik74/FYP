import axiosInstance from './index'

const axios = axiosInstance


export const getUserInfo = () => {return axios.get(`http://localhost:8000/api/user/`, )}
export const postUserInfo = (Username, Password,Birthday) => {return axios.post(`http://localhost:8000/api/user/`, {'name': Username, 'password': Password,'birth':Birthday})}


