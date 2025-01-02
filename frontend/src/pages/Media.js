import React, { useEffect, useState } from 'react';
import { fetchMedia, deleteMedia, addMedia, updateMedia } from '../api'; // Import `addMedia` API call

const Media = () => {
    const [mediaList, setMediaList] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [editMediaId, setEditMediaId] = useState(null); 
    const [newMedia, setNewMedia] = useState({
        title: '',
        type: '',
        isbn: '',
        author: '',
        publisher: '',
    });

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
            await deleteMedia(id);
            setMediaList(mediaList.filter((media) => media._id !== id));
        } catch (error) {
            console.error('Failed to delete media', error);
        }
    };

    const handleModify = async (id,data) => {
        const mediaToEdit = mediaList.find((media) => media._id === id);
        setNewMedia(mediaToEdit); // Pre-fill the modal with media data
        setEditMediaId(id); // Store the ID of the media being edited
        setShowModal(true); // Show the modal     
    };

    const handleAdd = () => {
        setShowModal(true);
    };

    const handleInputChange = (e) => {
        setNewMedia({ ...newMedia, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        try {
            if (editMediaId) {
                await updateMedia(editMediaId, newMedia);
                setMediaList((prevList) =>
                    prevList.map((media) =>
                        media._id === editMediaId ? { ...media, ...newMedia } : media
                    )
                );
            } else {
            const response = await addMedia(newMedia); // Call `addMedia` API
            setMediaList([...mediaList, response.data]); // Add new media to the list
            setShowModal(false);
            setNewMedia({ title: '', type: '', isbn: '', author: '' }); // Reset form
            }
        } catch (error) {
            console.error('Failed to add media', error);
        }
    };

    return (
        <div className="container mt-4">
            <h1 className="mb-4 text-center">Media List</h1>
            <button className="btn btn-primary mb-3" onClick={handleAdd}>
                Add Media
            </button>
            <div className="row">
                {mediaList.map((media, index) => (
                    <div className="col-md-4 mb-4" key={media._id}>
                        <div className="card h-100">
                            <div className="card-header bg-primary text-white">
                                <h5 className="card-title">{media.title}</h5>
                            </div>
                            <div className="card-body">
                                <p>
                                    <strong>Type:</strong> {media.type}
                                </p>
                                <p>
                                    <strong>ISBN:</strong> {media.isbn }
                                </p>
                                <p>
                                    <strong>Author:</strong> {media.author }
                                </p>
                                <p>
                                    <strong>Publisher:</strong> {media.publisher }
                                </p>
                            </div>
                            <div className="card-footer text-center">
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
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Modal */}
            {showModal && (
                <div className="modal show d-block" tabIndex="-1" style={{ background: 'rgba(0,0,0,0.5)' }}>
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Add New Media</h5>
                                <button
                                    type="button"
                                    className="btn-close"
                                    onClick={() => setShowModal(false)}
                                ></button>
                            </div>
                            <div className="modal-body">
                                <form>
                                    <div className="mb-3">
                                        <label htmlFor="title" className="form-label">
                                            Title
                                        </label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            id="title"
                                            name="title"
                                            value={newMedia.title}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="type" className="form-label">
                                            Type
                                        </label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            id="type"
                                            name="type"
                                            value={newMedia.type}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="isbn" className="form-label">
                                            ISBN
                                        </label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            id="isbn"
                                            name="isbn"
                                            value={newMedia.isbn}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="author" className="form-label">
                                            Author
                                        </label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            id="author"
                                            name="author"
                                            value={newMedia.author}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="publisher" className="form-label">
                                            Publisher
                                        </label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            id="publisher"
                                            name="publisher"
                                            value={newMedia.publisher}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                </form>
                            </div>
                            <div className="modal-footer">
                                <button
                                    type="button"
                                    className="btn btn-secondary"
                                    onClick={() => setShowModal(false)}
                                >
                                    Cancel
                                </button>
                                <button
                                    type="button"
                                    className="btn btn-primary"
                                    onClick={handleSubmit}
                                >
                                    Add Media
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Media;
