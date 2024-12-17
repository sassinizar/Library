import React, { useEffect, useState } from 'react';
import { fetchMedia } from '../api';

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

    return (
        <div>
            <h1>Media List</h1>
            <ul>
                {mediaList.map((media) => (
                    <li key={media._id}>{media.title} - {media.type}</li>
                ))}
            </ul>
        </div>
    );
};

export default Media;
