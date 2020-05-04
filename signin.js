import React , { Component } from 'react';
import { Redirect} from "react-router-dom";
import './signin.css';


import axios  from "axios"
export default class signin extends React.Component {
    constructor(props) {
        super(props);
    
        this.state= {
            userName: "",
            password: "",
            loggedIn:false,
            errors:{ userName: '', password: '', common: '',}
        };
    
        this.onSubmit = this.onSubmit.bind(this);
        this.change = this.change.bind(this);
      }
      componentDidMount() {
        console.log("done");
      }
      componentDidUpdate() {
        
        console.log(this.state.loggedIn);
        
      }
      
    
    change = e => {
        
        this.setState({
           [e.target.name]: e.target.value
        });
    };
    handleValidation = () => {
      const { userName,password} = this.state;
      let errors = { userName: '',password:'',common: ''};
      if (!userName) {
        errors.userName = 'Field cannot be empty';
      }
      if (!password) {
        errors.password = 'Field cannot be empty';
      }
     
      if (errors.userName.length>0||errors.password.length>0||errors.common.length>0)
      {
      this.setState({ errors });
      return false;
    }
      return true;
    } 
    onSubmit = e => {
        e.preventDefault();
        const isValid = this.handleValidation();
       if (isValid) {
        console.log(this.state);
     
        axios({
          method: 'post',
          url: 'http://localhost:5000/signin',
          crossorigin: true,
          withCredentials: false,
          data:{email: this.state.userName,
            password:this.state.password} // True otherwise I receive another error
        }).then(response => {
          if (response.data=="True") {
            console.log( response);
            this.setState({loggedIn:true});
            console.log(this.state.loggedIn);
            //history.push("/Home");
        }
        else if(response.data!=="True"){
          let errors = {common:''}
          errors.common=response.data;
          this.setState({errors})
           console.log(this.state.errors.common);
        }
          
        }).catch(error => {console.log(error);})
        this.setState({
        userName: "",
        password: "",
        loggedIn:false
        });
        if(this.state.errors.common.length > 0)
          {
          alert(this.state.errors.common)
         // window.location.reload(false);
  
          }
        }
        
      }
    render () {
      const {errors} = this.state;
        if (this.state.loggedIn == true) {
            return <Redirect to="/Home" />;
          }
          
        return (
           
        <div className='wrapper'>
          <div className='form-wrapper'>
            <h2>Sign In</h2>
            <form>
                <p class="small">
                <div>
                <input
                 type="userName"
                 name="userName"
                 placeholder="Email " value={this.state.userName} 
                 onChange={e => this.change(e)} 
                /> 
                <br />
                {errors.userName.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.userName}</span>}
                <br />
                </div>
                
                <br />
                <div>
                <input
                 type="password"
                 name="password"
                 placeholder="Password " value={this.state.password} 
                 onChange={e => this.change(e)} 
                /> 
                <br />
                {errors.password.length > 0 && <span className='error' style={{color: "red"}}>{this.state.errors.password}</span>}
                <br />
                </div>
                
                <br />  
                <button type="submit" onClick ={e => this.onSubmit(e)}>Login</button>
                </p>
            </form>
            </div>
        </div>
        );
    }

}

       