import React from 'react';
import './project.css';
import { useEffect } from 'react';
import { useHistory } from 'react-router-dom';


function ProjectPage() {
  console.log("ProjectPage");
  const history = useHistory();
  const key = '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';

  function PutUserInfo(json) { 
    if (json === "" || json === undefined){
      console.log("error username. stay default");
    } 
    else{
    console.log("the PutUserInfo func");
    console.log(json);
    document.getElementById("login").innerHTML = "login: " + json.items[0].login;
    document.getElementById("id").innerHTML = "id: " + json.items[0].id;
    document.getElementById("avatar").innerHTML = `<img height=100% width=100% src=${json.items[0].avatar_url} alt=${json.items[0].login}/>`;
    document.getElementById("node_id").innerHTML = "node_id: "  + json.items[0].node_id;
    document.getElementById("gravatar_id").innerHTML = "gravatar_id: " + json.items[0].gravatar_id;
    document.getElementById("url").innerHTML = "url: " + json.items[0].url;
    document.getElementById("html_url").innerHTML = "html_url: " + json.items[0].html_url;
    document.getElementById("followers_url").innerHTML = "followers_url: " + json.items[0].followers_url;
    document.getElementById("following_url").innerHTML = "following_url: " + json.items[0].following_url;
    document.getElementById("gists_url").innerHTML = "gists_url: " + json.items[0].gists_url;
    document.getElementById("starred_url").innerHTML = "starred_url: " + json.items[0].starred_url;
    document.getElementById("subscriptions_url").innerHTML = "subscriptions_url: " + json.items[0].subscriptions_url;
    document.getElementById("organizations_url").innerHTML = "organizations_url: " + json.items[0].organizations_url;
    document.getElementById("repos_url").innerHTML = "repos_url: " + json.items[0].repos_url;
    document.getElementById("events_url").innerHTML = "events_url: " + json.items[0].events_url;
    document.getElementById("received_events_url").innerHTML = "received_events_url: " + json.items[0].received_events_url;
    document.getElementById("type").innerHTML = "type: " + json.items[0].type;
    document.getElementById("site_admin").innerHTML = "site_admin: " + json.items[0].site_admin;
    document.getElementById("score").innerHTML = "score: " + json.items[0].score;
    console.log("the PutUserInfo func yet");
    }
  };

  function back_to_home() {
    history.push('/lab9/build/');
  }

  useEffect(() => {  // searching
    let checkevent = localStorage.login;
    console.log(localStorage.login);
    let url = new URL(`https://api.github.com/search/users?q=${checkevent}`);

      fetch(url, {
        Authorization: 'Token' + key
      }) //   получение данных
      .then(res => res.json())
      .then(res => {
        console.log(res);
        if (res.message !== "Not Found"){
          console.log('error');
          PutUserInfo(res);
        }
        
      }, [])
      .catch(er=>{
        console.log('error');
         document.getElementById("login").innerHTML ="404 user not found";
        });
    
  });

  return (
    <div className="project">
      <header className="project-header">
      
      <button onClick={()=>back_to_home()}> Home</button>
      </header>
      
      <div className="user-info">
        <div className="pict-box">
          <div className="icon-info" id="avatar"></div>
        </div>
        <div className="text-info" id="login"></div>
        <div className="text-info" id="id"></div>

        <div className="text-info" id="node_id"></div>
        <div className="text-info" id="gravatar_id"></div>
        <div className="text-info" id="url"></div>
        <div className="text-info" id="html_url"></div>
        <div className="text-info" id="followers_url"></div>
        <div className="text-info" id="following_url"></div>
        <div className="text-info" id="gists_url"></div>
        <div className="text-info" id="starred_url"></div>
        <div className="text-info" id="subscriptions_url"></div>
        <div className="text-info" id="organizations_url"></div>
        <div className="text-info" id="repos_url"></div>
        <div className="text-info" id="events_url"></div>
        <div className="text-info" id="received_events_url"></div>
        <div className="text-info" id="type"></div>
        <div className="text-info" id="site_admin"></div>
        <div className="text-info" id="score"></div>
      </div>
    </div>
  );
}

export default ProjectPage;
