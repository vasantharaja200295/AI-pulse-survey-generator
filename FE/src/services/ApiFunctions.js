import { getData, postData, putData } from "../services/serviceFunctions";


export const getPulses = async () => {
    try{
        const { data } = await getData('/api/pulses')
        return data
    }catch(err){
        throw new Error(err?.message)
    }
}


export const createPulse = async (data) => {
    try{
        const { data: res } = await postData('/api/pulses', data)
        return res
    }catch(err){
        throw new Error(err?.message)
    }
}


export const updatePulse = async (data) => {
    try{
        const { data: res } = await putData('/api/pulses', data)
        return res
    }catch(err){
        throw new Error(err?.message)
    }
}