import React from 'react';
import './home.css';
import {Link} from 'react-router-dom';

function NotFound() {
  return (
    <div className="home">
      <header className="home-header">
        error. user is not found.
      </header>
      <nav>
      <ul>
      <li><Link to='/lab9/build/'>Home</Link></li>
      </ul>
      </nav>
    </div>
  );
}

export default NotFound;