import React,{useState,useEffect} from 'react'
import axios from 'axios'

function reducer(state,action){
    switch(action.type){
        case 'make-request':
            return {loading:true,jobs:[]}
        case 'get-data':
            return {...state,loading:false,jobs:action.payload.jobs}
        case 'error':
            return {...state,loading:false,error:action.payload.error,jobs:[]}
        default:
            return state
    }
}

export const GetJobs = (params,page) => {
    const [state, dispatch] = useReducer(reducer, {jobs:[],loading:true})
    useEffect(() => {
        dispatch({
            type:'make-request'
        })
        axios.get('https://jobs.github.com/positions.json?search=node')
        .then()
        return () => {
            cleanup
        };
    }, [input]);
    return (

    )
}
