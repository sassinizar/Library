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
    <div style={styles.container}>
      <h1 style={styles.title}>My Borrowings</h1>
      {error && <p style={styles.error}>{error}</p>}
      {borrowings.length === 0 ? (
        <p>No borrowings found.</p>
      ) : (
        <table style={styles.table}>
          <thead>
            <tr>
              <th>Media Title</th>
              <th>Borrow Date</th>
              <th>Due Date</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {borrowings.map((borrowing) => (
              <tr key={borrowing._id}>
                <td>{borrowing.media_title || "Unknown Title"}</td>
                <td>{new Date(borrowing.borrow_date).toLocaleDateString()}</td>
                <td>{new Date(borrowing.due_date).toLocaleDateString()}</td>
                <td>
                  <button
                    style={styles.button}
                    onClick={() => returnMedia(borrowing._id)}
                  >
                    Return
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

// Inline styles
const styles = {
  container: {
    padding: "20px",
  },
  title: {
    fontSize: "28px",
    fontWeight: "bold",
    marginBottom: "20px",
  },
  error: {
    color: "red",
    marginBottom: "20px",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginBottom: "20px",
  },
  button: {
    backgroundColor: "#dc3545",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    padding: "8px 12px",
    cursor: "pointer",
  },
};

export default Borrowing;
