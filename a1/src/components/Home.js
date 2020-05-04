import React, { Component } from 'react';
import { Link } from "react-router-dom";
import { Nav, Navbar, NavItem } from "react-bootstrap";

//import 'bootstrap/dist/css/bootstrap.min.css';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import CardDeck from 'react-bootstrap/CardDeck';
import img1 from "../assets/shop.jpg";
import './Home.css';
import Toolbar from '../components/Toolbar';
export default class Home extends React.Component {
render(){
    return (
      <>
      <Toolbar/>
      <div class="container">
       
       <div className="col-sm-4" > 
       <div class="cards">    
         <div class="card-imd-top" ><img src={img1} width="50%" className="thumbnail"/></div>   
          <div  class="card-title "><h2>Product Name</h2></div> 
          <div className="card-body">
          <p class="card-text" >Product Description</p>  
          <form className="form-inline">
           <input
           type="text"
           className="form-control mb-2 mr-sm-2 align-self-md-center"
           placeholder="Enter threshold"
            name="name"
     /></form>
     <input type="submit" className="button1" value="Add item" />
          </div> 
           </div>  
        </div>  
           
          <div className="col-sm-4">  
        <div class="cards">  
         <div class="card-imd-top" ><img src={img1} width="50%" className="thumbnail"/></div>   
         <div  class="card-title "><h2>Product Name</h2></div> 
         <div className="card-body">
         <p class="card-text" >Product Description</p> 
         <form className="form-inline">
           <input
           type="text"
           className="form-control mb-2 mr-sm-2 align-self-md-center"
           placeholder="Enter threshold"
            name="name"
     /></form>
     <input type="submit" className="button1" value="Add item" />
         </div> 
          </div>       </div>  
          
          
        <div className="col-sm-4">  
        <div class="cards">  
         <div class="card-imd-top" ><img src={img1} width="50%" className="thumbnail" /></div>   
         <div  class="card-title "><h2>Product Name</h2></div> 
         <div className="card-body">
         <p class="card-text" >Product Description</p>  
         <form className="form-inline">
           <input
           type="text"
           className="form-control mb-2 mr-sm-2 align-self-md-center"
           placeholder="Enter threshold"
            name="name"
     /></form>
     <input type="submit" className="button1" value="Add item" />
         </div> 
           </div>  
           </div> 
           </div> 
           
</>
 
    );
    }
}
