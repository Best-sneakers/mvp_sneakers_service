import React, {useState} from 'react';
import './FileUpload.css';

const FileUpload = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [result, setResult] = useState(null);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        setSelectedFile(file);
    };

    const handleUpload = () => {
        if (selectedFile) {
            const formData = new FormData();
            formData.append('file', selectedFile);

            fetch('http://0.0.0.0:5010/api/v1/classificator/classificate', {
                method: 'POST',
                body: formData,
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Response:', data);
                    setResult(data);
                })
                .catch(error => {
                    console.error('Error uploading file:', error);
                });
        } else {
            console.error('No file selected.');
        }
    };

    return (
        <div className="center-container">
            <h2>File Upload</h2>
            <label htmlFor="file" className="custom-button">
                Choose File
            </label>
            <input
                id="file"
                type="file"
                className="input-file"
                onChange={handleFileChange}
            />
            <button className="custom-button" onClick={handleUpload}>
                Upload
            </button>

            {/* Display the result in the HTML */}
            {result !== null && (
                <div>
                    <h3>Result:</h3>
                    {Object.keys(result).length > 0 ? (
                        <p>{JSON.stringify(result)}</p>
                    ) : (
                        <p>No data found in the result object</p>
                    )}
                </div>
            )}
        </div>
    );
};

export default FileUpload;
