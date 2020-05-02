import React, { Component } from 'react';
import { Link, Redirect} from "react-router-dom";
import history from './history';
import axios from 'axios';
import './Form.css';

  
  const initialState = {firstName: "",lastName: "",
  email: "", phoneNumber: "",
  password: "",errors: { firstName: '', lastName: '', email: '', phoneNumber: '', password: '',common: '' },loggedIn:false
   };
   
export default class Form extends React.Component {
  constructor(props) {
    super(props);
    };
  componentDidMount() {
    console.log("done");
  }
  /*shouldComponentUpdate(nextProps, nextState) { 
    if (nextProps.name === this.props.name) return false;

    return true;
  }*/
  componentDidUpdate() {
    
    console.log(this.state.loggedIn);
    
  }
    state= {
        firstName: "",lastName: "",
        email: "", phoneNumber: "",
        password: "",errors: { firstName: '', lastName: '', email: '', phoneNumber: '', password: '',common:'' },
        loggedIn:false
    };
     
    change = e => {
        e.preventDefault();
        this.setState({
            [e.target.name]: e.target.value
         });
        
       /* let nam = e.target.name;
        let val = e.target.value;
        let errors=this.state.errors;
        if (nam === "firstName") {
        if (val.length<2) {
        errors.firstName="Field cannot be empty ";
      }
      }
      if (nam === "phoneNumber") {
        if (!Number(val)) {
        errors.phoneNumber="It can contain only digits";
      }
      }
      if (nam=="email") {
       var re =  RegExp(/^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i);
       let v= re.test(val);
        if (!v) {
         errors.email = 'invalid email';
       }
       }
       this.setState({errors, [nam]: val});*/
    //this.setState({errors, [nam]: val}, ()=> {  console.log(errors)})
        
    };
    
    handleValidation = () => {
        const { firstName,lastName,email, phoneNumber,password} = this.state;
        let errors = {  firstName: '', lastName: '', email: '', phoneNumber: '', password: '',common: ''};
        var r=RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,20})");
        let v= r.test(password.value);
        var re =  RegExp(/^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i);
        let val= re.test(email.value);
        if (email && !val) {
          errors.email = 'Enter a valid email-id';
        }
        if (!firstName) {
          errors.firstName = 'FirstName cannot be empty';
        }
        if (!lastName) {
          errors.lastName = 'LastName cannot be empty';
        }
        if(!email && !phoneNumber)
        errors.common="You need to enter atleast one out of Phone Number and Email-id";
        if (phoneNumber && !Number(phoneNumber)) {
          errors.phoneNumber="It can contain only digits";
        }
        if(!password)
        {
        errors.password='Password cannot be null';
        }
        /*else if (!v) {
          errors.password = 'Password must contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character.The length should be atleast 8 and atmost 20';
        }*/
        if (errors.firstName.length>0||errors.email.length>0||errors.phoneNumber.length>0||errors.lastName.length>0,errors.password.length>0||errors.common.length>0)
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
          
          //this.setState({ loggedIn:true });
          /*let data = JSON.stringify({
        password: this.state.password,
        username: this.state.email
    })
*/
          let d = this.state.firstName
        
          axios({
            method: 'post',
            url: 'http://localhost:5000/signup',
            crossorigin: true,
            withCredentials: false,
            data:{d} // True otherwise I receive another error
          }).then(response => {
            if (response) {
              console.log( response);
              this.setState({loggedIn:true});
              console.log(this.state.loggedIn);
              //history.push("/Home");
          } 
            
          }).catch(error => {console.log(error);})
         /* axios.post('http://localhost:5000/signup',this.state.firstName).then (response => {console.log(response)}).catch(error => {console.log(error)});
          
         fetch("http://localhost:5000/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        firstName: this.state.firstName
      })
    }).then (response => {console.log(response)}).catch(error => {console.log(error)});;*/
      // clear form
            this.setState(initialState);
    }
    };
    render () {
        const {errors} = this.state;
        if (this.state.loggedIn == true) {
          return <Redirect to="/Home" />;
        }
          return (
          <div className='wrapper'>
          <div className='form-wrapper'>
            <h2>Sign Up</h2>
            <form onSubmit={this.onsubmit} >
              
                <div>
                <input
                 name="firstName"
                 placeholder="First name " value={this.state.firstName} 
                 onChange={e => this.change(e)} 
                /> 
                
                <br />
                {errors.firstName.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.firstName}</span>}
                <br />
                </div>
                <div>
                <input
                 name="lastName"
                 placeholder="Last name " value={this.state.lastName} 
                 onChange={e => this.change(e)} 
                /> 
                <br />
                {errors.lastName.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.lastName}</span>}
                <br />
                </div>
                <div>
                <input
                 name="password"
                 placeholder="Password " value={this.state.password} 
                 onChange={e => this.change(e)} 
                /> 
                <br />
                {errors.password.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.password}</span>}
                <br /> 
                </div> 
                <div>
                <h1>Receive notifications via:</h1>
                <br />
                </div>
                <p class="big">
                <div>
                <input
                 name="email"
                 placeholder="Email-id" value={this.state.email} 
                 onChange={e => this.change(e)}
                /> 
                <br />
                {errors.email != '' && <span className='error' style={{color: "red"}}>{this.state.errors.email}</span>}
                <br />
                </div>
                OR
                </p>
                <br />
                <div>
                <input
                 name="phoneNumber"
                 placeholder="Phone Number " value={this.state.phoneNumber} 
                 onChange={e => this.change(e)} 
                /> 
                <br />
                {errors.phoneNumber.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.phoneNumber}</span>}
                <br />
                </div>
                <br />
                {errors.common.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.common}</span>}
                <br />  
                <button type="submit">SignUp</button>
                
            </form>
            <Link to ="signin">Switch to Sign-in</Link>
            </div>
            </div>
            
        );
        
    }

}
