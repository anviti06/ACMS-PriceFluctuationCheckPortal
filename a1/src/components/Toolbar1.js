import React from 'react';
import { Link } from "react-router-dom";
import './Toolbar.css';

const toolbar1 = props => (
  <header className="toolbar">
    <nav className="toolbar__navigation">
    <div></div>
      
        <div className="toolbar__logo">XYZ COMPANY</div>
      
      <div className="spacer" />
      <div className="toolbar_navigation-items">
        <ul>
          <li>
          <Link to ="Home">Home</Link>
          </li>
          <li>
            <a href="/">Logout</a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
)

export default toolbar1