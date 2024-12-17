import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Media from './pages/Media';
import Borrowing from './pages/Borrowing';
import Navbar from './components/Navbar';

function App() {
    return (
        <Router>
            <div>
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/media" element={<Media />} />
                    <Route path="/borrowings" element={<Borrowing />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
