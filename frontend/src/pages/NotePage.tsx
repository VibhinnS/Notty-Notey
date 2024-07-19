import { useParams } from "react-router-dom"
import { useState, useEffect } from "react";

const NotePage = () => {
    const { id } = useParams();
    const [note, setNote] = useState(null)
    useEffect(() => {
        getNote()
    }, [id])
    let getNote = async () => {
        let response = await fetch(`/api/notes/${id}`)
        let data = await response.json()
        setNote(data)
    }
    return (
        <div>{note?.body}</div>
  )
}

export default NotePage