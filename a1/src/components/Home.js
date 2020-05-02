import React, { Component } from 'react';
import { Link } from "react-router-dom";
import { Nav, Navbar, NavItem } from "react-bootstrap";

//import 'bootstrap/dist/css/bootstrap.min.css';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import CardDeck from 'react-bootstrap/CardDeck';
import img from "../assets/shop.jpg";
import './Home.css';
import Toolbar from '../components/Toolbar';
export default class Home extends React.Component {
render(){
    return (
      <>
      <Toolbar/>
      <CardDeck >
  <Card>
    <Card.Img variant="top" src={img} />
    <Card.Body>
      <Card.Title>Card title</Card.Title>
      <Card.Text>
      Product name
       Description
       Price
      </Card.Text>
      <Card.Link href="#">Add item</Card.Link>
    </Card.Body>
    <Card.Footer>
      <small className="text-muted">Last updated 3 mins ago</small>
    </Card.Footer>
  </Card>
 <Card>
    <Card.Img variant="top" src={img} />
    <Card.Body>
      <Card.Title>Card title</Card.Title>
      <Card.Text>
      Product name
       Description
       Price
      </Card.Text>
      <Card.Link href="#">Add item</Card.Link>
    </Card.Body>
    <Card.Footer>
      <small className="text-muted">Last updated 3 mins ago</small>
    </Card.Footer>
  </Card>
  <Card>
    <Card.Img variant="top" src={img} />
    <Card.Body>
      <Card.Title>Card title</Card.Title>
      <Card.Text>
       Product name
       Description
       Price
      </Card.Text>
      <Card.Link href="#">Add item</Card.Link>
     
    </Card.Body>
    <Card.Footer>
      <small className="text-muted">Last updated 3 mins ago</small>
    </Card.Footer>
  </Card>
  
</CardDeck>
</>
 
    );
    }
}
