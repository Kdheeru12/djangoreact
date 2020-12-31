import React,{useState,useEffect} from 'react'
import axios from 'axios'
export const Detail = (props) => {
    const [PostsDetail, setPostsDetail] = useState({post:null})
    const [Loading, setLoading] = useState(true);
    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/${props.match.params.id}/`)
        .then(res => setPostsDetail({post:[res.data]}))
        .catch(err => console.log(err))
        setLoading(false)
    }, []);
    return (
        <React.Fragment>
            {Loading && 'loading'}
            {PostsDetail.post && PostsDetail.post.map(i =>(
                <div key={i.id}>
                    <h1> {i.title}</h1>
                    <p>{i.content}</p>
                </div>
            ))}
        </React.Fragment>
    )
}
