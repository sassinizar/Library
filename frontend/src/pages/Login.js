import React from 'react';
import UserForm from '../components/UserForm';
import { loginUser } from '../api';

const Login = () => {
    const handleLogin = async (formData) => {
        try {
            const response = await loginUser(formData);
            alert('Login successful: ' + response.data.message);
        } catch (error) {
            alert('Login failed: ' + error.response.data.error);
        }
    };

    return <UserForm onSubmit={handleLogin} buttonText="Login" />;
};

export default Login;
