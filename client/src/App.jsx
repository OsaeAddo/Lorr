import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'


import { Home } from "./pages/all-pages"



const App = () => {
  
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="" />
      </Switch>
    </Router>
  )
  
}

export default App;
