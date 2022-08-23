import React from 'react'
import { BrowserRouter as Router, Routes, Route, Switch, Link } from 'react-router-dom'


import { Home } from "./pages/all-pages"



const App = () => {
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="admin/" element={<AdminLayout />}> //url route for admin related pages
          <Route index element={<AdminHome />} />
        </Route>
      </Routes>
    </Router>
  )
  
}

export default App;
