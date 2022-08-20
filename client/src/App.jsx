import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'


import { Home } from "./pages/all-pages"



const App = () => {
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="" />
      </Switch>
    </Router>
  )
  
}

export default App;
