
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import history from './components/history';
import Form from "./components/Form";
import signin from "./components/signin";
import Home from "./components/Home";
import Wishlist from "./components/Wishlist";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Link,
  Redirect
} from "react-router-dom";
/*useEffect(() => {
  fetch("/Form").then(response =>
    response.json().then(data => {
      console.log(data);
    })
  );
}, []);*/

class App extends React. Component {
 

  render () {
    return (
      <div className="App">
        
        <Router history={history}>
        
        <Route exact path="/" component={Form} />
        <Route exact path="/signin" component={signin} />
        <Route exact path="/Home" component={Home} />
        <Route exact path="/wishlist" component={Wishlist} />
      
    </Router>
        

      </div>
      
    );
  }
}

export default App;
 


