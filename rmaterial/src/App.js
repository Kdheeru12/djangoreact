import './App.css';
import React from 'react';
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom'
import Themes from './components/Themes'
import MediaCard from './components/posts';
import { Header } from './components/Header';
import { Footer } from './components/Footer';
import { Detail } from './components/Detail';
import Login from './components/Users/Login';
import Registration from './components/Users/Registration'
import Logout from './components/Users/Logout'


function App() {
  return (
    <React.Fragment>
      <Router>
      <Header/>
        <Switch>
          <Route exact path='/' component={MediaCard}/>
          <Route path='/api/:id' component = {Detail} />
          <Route path='/login' component = {Login} />
          <Route path='/reg' component={Registration} />
          <Route path='/logout' component={Logout} />
        </Switch>
        <Footer/>
      </Router>
    </React.Fragment>
    
  );
}

export default App;
