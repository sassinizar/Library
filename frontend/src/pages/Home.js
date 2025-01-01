import React from "react";

const Home = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Welcome to NS Library</h1>
      <p style={styles.description}>
        Manage your media and borrowings efficiently with our easy-to-use platform.
      </p>
      <button style={styles.button} onClick={() => alert("Explore the Library!")}>
        Explore Library
      </button>
    </div>
  );
};

// Inline styles for demonstration
const styles = {
  container: {
    textAlign: "center",
    marginTop: "50px",
    padding: "20px",
  },
  title: {
    fontSize: "36px",
    fontWeight: "bold",
  },
  description: {
    fontSize: "18px",
    color: "#555",
    marginBottom: "20px",
  },
  button: {
    backgroundColor: "#007BFF",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    padding: "10px 20px",
    cursor: "pointer",
    fontSize: "16px",
  },
};

export default Home;
