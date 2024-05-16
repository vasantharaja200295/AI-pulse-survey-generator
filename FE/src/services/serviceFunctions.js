import axios from "axios";


export const getData = async (url) => {
    const { data } = await axios.get(url);
    return data
}

export const postData = async (url, data) => {
    const { data: res } = await axios.post(url, data);
    return res
}

export const putData = async (url, data) => {
    const { data: res } = await axios.put(url, data);
    return res
}