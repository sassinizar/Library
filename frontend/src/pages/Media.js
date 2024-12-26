import React, { useEffect, useState } from 'react';
import { fetchMedia, deleteMedia } from '../api';

const Media = () => {
    const [mediaList, setMediaList] = useState([]);

    useEffect(() => {
        const loadMedia = async () => {
            try {
                const response = await fetchMedia();
                setMediaList(response.data);
            } catch (error) {
                console.error('Failed to fetch media', error);
            }
        };
        loadMedia();
    }, []);

    const handleDelete = async (id) => {
        try {
            await deleteMedia(id); // Assuming `deleteMedia` is an API call to delete media
            setMediaList(mediaList.filter((media) => media._id !== id));
        } catch (error) {
            console.error('Failed to delete media', error);
        }
    };

    const handleModify = (id) => {
        console.log(`Modify media with ID: ${id}`);
        // Implement your modify logic (e.g., open a modal for editing)
    };

    const handleAdd = () => {
        console.log('Add new media');
        // Implement your add logic (e.g., open a modal for adding)
    };

    return (
        <div className="container mt-4">
            <h1 className="mb-4">Media List</h1>
            <button className="btn btn-primary mb-3" onClick={handleAdd}>
                Add Media
            </button>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Title</th>
                        <th>Type</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {mediaList.map((media, index) => (
                        <tr key={media._id}>
                            <td>{index + 1}</td>
                            <td>{media.title}</td>
                            <td>{media.type}</td>
                            <td>
                                <button
                                    className="btn btn-warning btn-sm me-2"
                                    onClick={() => handleModify(media._id)}
                                >
                                    Modify
                                </button>
                                <button
                                    className="btn btn-danger btn-sm"
                                    onClick={() => handleDelete(media._id)}
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Media;
