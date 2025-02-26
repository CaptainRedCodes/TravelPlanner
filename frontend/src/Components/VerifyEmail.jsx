import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { verifyEmail } from "../services/api";

const VerifyEmail = () => {
    const { token } = useParams();
    const [status, setStatus] = useState("Verifying...");

    useEffect(() => {
        const verify = async () => {
            const result = await verifyEmail(token);
            if (result.success) {
                setStatus("Email verified successfully! You can now log in.");
            } else {
                setStatus("Verification failed: " + result.message);
            }
        };
        verify();
    }, [token]);

    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-xl font-bold">{status}</h1>
        </div>
    );
};

export default VerifyEmail;