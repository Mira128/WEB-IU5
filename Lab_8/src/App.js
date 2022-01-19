import React from 'react';
import './App.css';
import ProjectPage from './pages/project/index.js';
import HomePage from './pages/home/index.js';
import NotFound from './pages/home/notfound.js';
import { Switch, Route} from 'react-router-dom';

function App () {

  return (
    <div className="App">
      <header className="App-header">
        Github search users
      </header>
        <Switch>
            <Route path='/lab9/build/project' component={ProjectPage} />
            <Route exact path='/lab9/build/' component={HomePage} />
            <Route component={NotFound} />
        </Switch>
    </div>
  );
};

export default App;
