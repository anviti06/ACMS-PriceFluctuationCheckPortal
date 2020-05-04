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
import axios from 'axios';
  const initialState = {
    oductId: "",productName: "", threshold: "",
    errors: { threshold: '',common:'' },
   };
export default class Home extends React.Component {
  state= {
    productId: "",productName: "", threshold: "",
    errors: { threshold: '',common:'' },
  };
  change = e => {
    e.preventDefault();
    this.setState({
        [e.target.name]: e.target.value
     });
    };
    handleValidation = () => {
      const { threshold} = this.state;
      let errors = { threshold: '',common: ''};
      if (!threshold) {
        errors.threshold = 'Field cannot be empty';
      }
     
      if (errors.threshold.length>0||errors.common.length>0)
      {
      this.setState({ errors });
      return false;
    }
      return true;
    } 
    onsubmit= e => {
      e.preventDefault();
      const isValid = this.handleValidation();
      
     
      if (isValid) {
        console.log(this.state);
     
         axios({
          method: 'post',
          url: 'http://localhost:5000/Home',
          crossorigin: true,
          withCredentials: false,
          data:{threshold: this.state.threshold} // True otherwise I receive another error
        }).then(response => {
          if (response.data==="True") {
            console.log( response);
        }
        else if(response.data!=="True"){
         let errors = {common:''}
         errors.common=response.data;
         this.setState({errors})
          console.log(this.state.errors.common);
        } 
          
        }).catch(error => {console.log(error);})
          this.setState(initialState);
  }
  };
  
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
          <form className="form-inline" onSubmit={this.onsubmit}>
           <input
           type="text"
           className="form-control mb-2 mr-sm-2 align-self-md-center"
           placeholder="Enter threshold"
            name="threshold"
            value={this.state.threshold}
            
            onChange={e => this.change(e)} 
            />
            <br />
            {this.state.errors.threshold.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.threshold}</span>}
                <br />
     
           <input type="submit" className="button1" value="Add item" />
     </form>
          </div> 
           </div>  
        </div>  
           
          <div className="col-sm-4">  
        <div class="cards">  
         <div class="card-imd-top" ><img src={img1} width="50%" className="thumbnail"/></div>   
         <div  class="card-title "><h2>Product Name</h2></div> 
         <div className="card-body">
         <p class="card-text" >Product Description</p> 
         <form className="form-inline" onSubmit={this.onsubmit}>
           <input
           type="text"
           className="form-control mb-2 mr-sm-2 align-self-md-center"
           placeholder="Enter threshold"
            name="name"
            onChange={e => this.change(e)} 
     />
     <br />
                {this.state.errors.threshold.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.threshold}</span>}
                <br />
     <input type="submit" className="button1" value="Add item" />
     </form>
         </div> 
          </div>       </div>  
          
          
        <div className="col-sm-4">  
        <div class="cards">  
         <div class="card-imd-top" ><img src={img1} width="50%" className="thumbnail" /></div>   
         <div  class="card-title "><h2>Product Name</h2></div> 
         <div className="card-body">
         <p class="card-text" >Product Description</p>  
         <form className="form-inline" onSubmit={this.onsubmit}>
           <input
           type="text"
           className="form-control mb-2 mr-sm-2 align-self-md-center"
           placeholder="Enter threshold"
            name="name"
            onChange={e => this.change(e)} />
            <br />
                {this.state.errors.threshold.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.threshold}</span>}
                <br />
     
    
     <input type="submit" className="button1" value="Add item" />
     </form>
         </div> 
           </div>  
           </div> 
           </div> 
           
</>
 
    );
    }
}
