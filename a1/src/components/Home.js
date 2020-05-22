import React, { Component } from 'react';
import { Link } from "react-router-dom";
import { Nav, Navbar, NavItem } from "react-bootstrap";
import img1 from "../assets/shop.jpg";
import './Home.css';
import Toolbar from '../components/Toolbar';
import axios from 'axios';
import Carousel from 'react-elastic-carousel';

    //const count = Object.keys(data).length;
    //console.log(count);
export default class Home extends React.Component {
  
  state= {
    productId: "",productName: "", threshold:"",th:[],
    errors:{threshold:"",common:""},
    data:[]
  };
  
  constructor() {
    super()
    this.onsubmit = this.onsubmit.bind(this);
    this.change = this.change.bind(this);
  }
  componentDidMount() {
    this.getData();
    this.interval = setInterval(() => {
      this.getData();
    }, 30000);
  }
  getData() {
    fetch('http://localhost:5000/product',{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
      })
      .then((response) => {
          return response.json()
      }).then((json) => {
          this.setState({data: json});
          console.log(json);
      }).catch(error => {console.log(error);})
}
 
  componentDidUpdate() {
    
  }
  
 componentWillUnmount() {
  clearInterval(this.interval);
}
  
  change = (index,e) => {
    e.preventDefault();
    const th=[...this.state.th];
    th[e.target.id]=e.target.value;
    this.setState({th});
    console.log(this.state.th);
    this.setState({threshold:th[index]});
     //const uArray=[...this.state.th];
     //uArray[index]=this.state.threshold;
     //console.log(uArray[index]);
     //this.setState({th:uArray});
    
    };
    handleValidation = (index) => {
    // const errors ={threshold:"",common:""};
     //this.setState({errors},()=>{console.log(this.state.errors);});
      //const longeur = res.data.length;
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
     pRequest=async(index) =>{
    try{
     const config={ method: 'post',
     url: 'http://localhost:5000/Home',
     crossorigin: true,
     withCredentials: false,
     data:{threshold: this.state.th[index],name:this.state.data[index].name,pid:this.state.data[index].pid}}
     let res=await axios(config)
     console.log(res.data);
     if (res.data==="True") {
      console.log( res.data);
      }
     else if(res.data!=="True"){
     let errors = {common:''}
     errors.common=res.data;
     this.setState({errors})
     console.log(this.state.errors.common);
    }
  }
    catch(error){
     console.log(error);
    }
    if(this.state.errors.common.length>0)
    {
     const error=this.state.errors.common;
     const errors ={threshold:"",common:""};
     this.setState({errors},()=>{console.log(this.state.errors);});
     alert(error)
    }
   }
    onsubmit= (index,e) => {
      e.preventDefault();
      this.setState({threshold:this.state.th[index]});
      const isValid = this.handleValidation(index);
      if (isValid) {
      console.log(this.state);
      this.pRequest(index);
      this.setState({productId: "",productName: "", threshold:""});
      const th=[...this.state.th];
      th[index]="";
      this.setState({th});
      }
      if(!isValid){
          alert(this.state.errors.threshold)
         }
      const errors ={threshold:"",common:""};
      this.setState({errors},()=>{console.log(this.state.errors);});
         //e.target.reset();        
 };
  _createCardsUI(){
   // var data = this.state.data;
   return(<div className="container"> <Carousel itemsToShow={4}  itemsToScroll={4} enableMouseSwipe={true} enableSwipe={true}>{
      this.state.data.map(({pid,name,mrp,price,description,img_file},index) => ( 
     <div className="col-sm-4" > 
      <div class="cards" key={index} >    
        <div class="card-imd-top" ><img src={require('../assets/' + img_file + '.jpg')} width="50%" className="thumbnail"/></div>   
         <div  class="card-title "><h4>{name}</h4></div> 
         <div className="card-body">
         <h5>MRP: {mrp}</h5> 
         <h6>Current Price: {price}</h6>
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
      <Toolbar/>
          {this._createCardsUI()}
           
      </>
 
    );
    }
}
