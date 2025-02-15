import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ProtectedPage from '../../frontend/src/Components/Protected';
import Register from '../../frontend/src/Components/Register';
import Login from "./Components/Login";
import PrivateRoute from "./routes/PrivateRoute";
import Landingpage from './Components/Landingpage';
function App() {
  
  return (
    <Router>
      
      <Routes>
      <Route path='/' element={<Landingpage/>}/>  
      <Route path="/register" element={<Register />} />
      <Route path='/login' element={<Login/>}/>
      <Route element={<PrivateRoute/>}>
        <Route path="/protected" element={<ProtectedPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
