import axios from "axios";

const API_URL = "http://127.0.0.1:8000/token"; // FastAPI login endpoint

export const login = async (username, password) => {
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    try {
        const response = await axios.post(API_URL, formData, {
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
        });

        if (response.data.access_token) {
            localStorage.setItem("token", response.data.access_token);
        }

        return response.data;
    } catch (error) {
        console.error("Login failed", error);
        throw error;
    }
};

export const logout = () => {
    localStorage.removeItem("token");
};

export const getToken = () => {
    return localStorage.getItem("token");
};
