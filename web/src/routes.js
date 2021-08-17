import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

// PAGES
import Login from './Pages/Login/index';
import Signup from './Pages/Signup/index';
import Calendar from './Pages/Calendar/index';
import Contact from './Pages/Contact/index';
import SalesDetail from './Pages/SalesDetail/index';
// import Stage from './Pages/Stage/index';

function routes() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/signup" component={Signup} />
        <Route exact path="/calendar" component={Calendar} />
        <Route exact path="/contact" component={Contact} />
        <Route exact path="/salesdetail" component={SalesDetail} />
        <Route exact path="/salesdetail/:id" component={SalesDetail} />
        {/* <Route exact path="/" component={Stage} /> */}
      </Switch>
    </Router>
  );
}

export default routes;