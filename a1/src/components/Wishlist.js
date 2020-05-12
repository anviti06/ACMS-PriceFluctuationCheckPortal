import React, { Component } from 'react';
import { Link } from "react-router-dom";
import { Nav, Navbar, NavItem } from "react-bootstrap";
import Data from '../assets/data.json';
import img1 from "../assets/shop.jpg";
import './Home.css';
import Toolbar1 from '../components/Toolbar1';
import axios from 'axios';
import Carousel from 'react-elastic-carousel';
  const initialState = {
    productId: "",productName: "", threshold:"",th:[],
    errors:{threshold:"",common:""},Data};
    const count = Object.keys(Data).length;
    console.log(count);
export default class Wishlist extends React.Component {
  
  state= {
    productId: "",productName: "", threshold:"",th:[],
    errors:{threshold:"",common:""},
    Data
  };
  
  constructor() {
    super()
    this.onsubmit = this.onsubmit.bind(this);
    this.change = this.change.bind(this);
  }
  componentDidMount() {
    console.log("done");
  }
 
  componentDidUpdate() {
    
 }
 
  change = (index,e) => {
    e.preventDefault();
    const th=[...this.state.th];
    //const th=[];
    th[e.target.id]=e.target.value;
    this.setState({th});
    console.log(this.state.th);
    this.setState({threshold:th[index]});
    };
    handleValidation = (index) => {
      if (!this.state.th[index]) {
        this.state.errors.threshold= 'Field cannot be empty';
      }
      else if (!Number(this.state.th[index])) {
        this.state.errors.threshold="It can contain only digits";
      }
      if (this.state.errors.threshold.length>0||this.state.errors.common.length>0)
      {
        console.log(this.state.errors.threshold);
        return false;
      }
      return true;
    } 
    onsubmit= (index,e) => {
      e.preventDefault();
      this.setState({threshold:this.state.th[index]});
      const isValid = this.handleValidation(index);
      if (isValid) {
      console.log(this.state);
      axios({
          method: 'post',
          url: 'http://localhost:5000/Home',
          crossorigin: true,
          withCredentials: false,
          data:{threshold: this.state.th[index],name:this.state.Data[index].name,pid:this.state.Data[index].pid} // True otherwise I receive another error
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
        this.setState({productId: "",productName: "", threshold:"",Data});
        const th=[...this.state.th];
        th[index]="";
        this.setState({th});
         }
         else{
          alert(this.state.errors.threshold)
         }
         if(this.state.errors.common.length>0)
         {
          alert(this.state.errors.common)
         }
         const errors ={threshold:"",common:""};
         this.setState({errors},()=>{console.log(this.state.errors);});
         //e.target.reset();
         
 };
  _createCardsUI(){
    //var data = this.state.data;
    //instead of Data write data
 
    return(<div className="container"> <Carousel itemsToShow={4}  itemsToScroll={4} enableMouseSwipe={true} enableSwipe={true}>{
    Data.map(({pid,name,mrp,price,description},index) => ( 
     <div className="col-sm-4" > 
      <div class="cards" key={index} >    
        <div class="card-imd-top" ><img src={img1} width="50%" className="thumbnail"/></div>   
         <div  class="card-title "><h4>{name}</h4></div> 
         <div className="card-body">
         <h5>{mrp}</h5> 
         <h6>{price}</h6>
         <p class="card-text" >{description}</p>  
         <form className="form-inline" onSubmit={e=>this.onsubmit(index,e)} key={index}>
          <input
          key={index}
          id={index}
          type="text"
          className="form-control mb-2 mr-sm-2 align-self-md-center"
          placeholder="Enter threshold"
          name={pid}
          value={this.state.th[index]}
          onChange={e => this.change(index,e)} 
           />
           <input type="submit" className="button1" value="Add item" id={index} key={index} />
           
          </form>
         </div> 
        </div>  
       </div>
     
    )
          )

    }</Carousel> </div>);
    
}


  
render(){
    return (
      <>
      <Toolbar1/>
          {this._createCardsUI()}
           
      </>
 
    );
    }
}
