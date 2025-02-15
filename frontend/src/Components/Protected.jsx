import { useNavigate } from "react-router-dom";
import { logout } from "../services/authService"; // Ensure correct path
import Navigation from "../components/Navbar"; // Correct import path

const Dashboard = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate("/login");
    };

    return (
        <div className="h-screen bg-gray-100">
            <Navigation /> {/* Navbar at the top */}
            <div className="flex flex-col items-center justify-center h-full">
                <h2 className="text-3xl font-bold mb-4">Welcome to Your Dashboard</h2>
                <button 
                    onClick={handleLogout} 
                    className="mt-4 px-6 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
                >
                    Logout
                </button>
            </div>
        </div>
    );
};

export default Dashboard;
