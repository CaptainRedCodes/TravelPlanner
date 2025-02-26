// services/api.js
export const verifyEmail = async (token) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/auth/verify-email/${token}`, {
            method: "GET",
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error verifying email:", error);
        return { success: false, message: "Verification failed." };
    }
};