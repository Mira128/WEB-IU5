import React from 'react';
import './home.css';
import { useHistory } from 'react-router-dom';

function HomePage() {
  console.log("HomePage");
  const history = useHistory();

  function enter_todo(ev) { // ввод записи
    if(ev.key === 'Enter') {
      
      localStorage.setItem('login', ev.target.value);
      history.push('/lab9/build/project')
    }
  }

  function to_project() {
    let value = document.getElementById('input_user');
    console.log(value.value);
    localStorage.setItem('login', value.value);
    console.log("to_project");
    console.log(localStorage.login);
    history.push('/lab9/build/project');
  }

  return (
    <div className="home">
      <input className="userame_input" id="input_user" placeholder="write here username..." onKeyDown={(ev)=>enter_todo(ev)} />
      <button onClick={()=>to_project()}> Ok </button>
      
    </div>
  );
}

export default HomePage;
