import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

const NotePage = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [note, setNote] = useState({ body: '' });

    useEffect(() => {
        getNote();
    }, [id]);

    const getNote = async () => {
        let response = await fetch(`/api/notes/${id}`);
        let data = await response.json();
        setNote(data);
    };

    const updateNote = async () => {
        const response = await fetch(`/api/notes/${id}/update`, {
            method: "PUT",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(note)
        });

        if (response.ok) {
            const updatedNote = await response.json();
            setNote(updatedNote);
        } else {
            console.error("Failed to update the note");
        }
    };

    const handleSubmit = async () => {
        await updateNote();
        navigate('/');
    };

    return (
        <div>
            <textarea
                onChange={(e) => setNote({ ...note, 'body': e.target.value })}
                value={note.body}
            />
            <button onClick={handleSubmit}>Save</button>
        </div>
    );
};

export default NotePage;
