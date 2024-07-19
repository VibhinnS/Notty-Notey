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

    let updateNote = async () => {
        fetch(`/api/notes/${id}/update`, {
            method: "PUT",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(note)
    })
}
    return (
        <textarea onChange={(e) => {setNote({...note, 'body':e.target.value})}} defaultValue={note?.body}></textarea>
  )
}

export default NotePage