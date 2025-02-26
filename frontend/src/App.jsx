import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from '../../frontend/src/Components/Register';
import Login from "./Components/Login";
import PrivateRoute from "./routes/PrivateRoute";
import Landingpage from './Components/Landingpage';
import ProfilePage from './Components/ProfilePage';
import ChangePassword from './Components/ChangePassword';
import TripResults from './Components/TripResults';
function App() {
  
  return (
    <Router>
      
      <Routes>
      <Route path='/' element={<Landingpage/>}/>  
      <Route path="/register" element={<Register />} />
      <Route path='/login' element={<Login/>}/>
      <Route element={<PrivateRoute/>}>
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/changePassword" element={<ChangePassword />} />
        <Route path="/trip-results" element={<TripResults/>} />
        </Route>
      
      </Routes>
    </Router>
  );
}

export default App;
