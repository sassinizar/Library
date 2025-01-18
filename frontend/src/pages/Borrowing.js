import React, { useEffect, useState } from "react";
import axios from "axios";

const Borrowing = () => {
  const [borrowings, setBorrowings] = useState([]);
  const [error, setError] = useState("");

  // Fetch borrowing data from the backend
  useEffect(() => {
    axios
      .get("/api/borrowings") // Update this with the correct API endpoint
      .then((response) => {
        setBorrowings(response.data);
        setError("");
      })
      .catch((err) => {
        setError("Failed to fetch borrowing data.");
        console.error(err);
      });
  }, []);

  // Handle return media
  const returnMedia = (borrowingId) => {
    axios
      .post("/api/return", { borrowing_id: borrowingId }) // Update this with the correct API endpoint
      .then(() => {
        alert("Media returned successfully!");
        setBorrowings((prev) =>
          prev.filter((borrowing) => borrowing._id !== borrowingId)
        );
      })
      .catch((err) => {
        setError("Failed to return media.");
        console.error(err);
      });
  };

  return (
    <div className="container mt-4">
      <div className="card shadow">
        <div className="card-header bg-primary text-white">
          <h3>My Borrowings</h3>
        </div>
        <div className="card-body">
          {error && <div className="alert alert-danger">{error}</div>}
          {borrowings.length === 0 ? (
            <p className="text-center">No borrowings found.</p>
          ) : (
            <div className="table-responsive">
              <table className="table table-bordered table-striped">
                <thead className="thead-dark">
                  <tr>
                    <th>#</th>
                    <th>Media Title</th>
                    <th>Borrow Date</th>
                    <th>Due Date</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  {borrowings.map((borrowing, index) => (
                    <tr key={borrowing._id}>
                      <td>{index + 1}</td>
                      <td>{borrowing.media_title || "Unknown Title"}</td>
                      <td>
                        {new Date(borrowing.borrow_date).toLocaleDateString()}
                      </td>
                      <td>
                        {new Date(borrowing.due_date).toLocaleDateString()}
                      </td>
                      <td>
                        <button
                          className="btn btn-danger btn-sm"
                          onClick={() => returnMedia(borrowing._id)}
                        >
                          Return
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Borrowing;
