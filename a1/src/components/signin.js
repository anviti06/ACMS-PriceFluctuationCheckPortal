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
            loggedIn:false
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
    onSubmit = e => {
        e.preventDefault();
        let d = this.state.userName
        
        axios({
          method: 'post',
          url: 'http://localhost:5000/signin',
          crossorigin: true,
          withCredentials: false,
          data:{d} // True otherwise I receive another error
        }).then(response => {
          if (response.ok) {
            console.log( response);
            this.setState({loggedIn:true});
            console.log(this.state.loggedIn);
            //history.push("/Home");
        }
          
        }).catch(error => {console.log(error);})
        this.setState({
        userName: "",
        password: "",
        loggedIn:false
        });
        
      }
    render () {
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
                 placeholder="USERNAME " value={this.state.userName} 
                 onChange={e => this.change(e)} 
                /> 
                </div>
                
                <br />
                <div>
                <input
                 type="password"
                 name="password"
                 placeholder="Password " value={this.state.password} 
                 onChange={e => this.change(e)} 
                /> 
                </div>
                
                <br />  
                <button onClick ={e => this.onSubmit(e)}>Login</button>
                </p>
            </form>
            </div>
        </div>
        );
    }

}

       