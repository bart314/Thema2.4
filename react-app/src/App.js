import React, { Component } from 'react';
import uuid from 'uuid'
import './App.css';

import Project from './components/Project'
import AddProject from './components/AddProject'
import GetPosts from './components/GetPosts'

class App extends Component {
  constructor() {
    super()
    this.state = {
      'project': []
    }
  }

  componentWillMount() {
    this.setState({
      'projects': [
        {id:uuid.v4(), 'title':'website', 'category':'web design'},
        {id:uuid.v4(), 'title':'social app', 'category':'mobile development'},
        {id:uuid.v4(), 'title':'e-commers shopping cart', 'category':'web development'},
      ]
    })
  }

  handleAddProject(project) {
    console.log('handleAddProject')
    let projects = this.state.projects
    projects.push(project)
    this.setState(projects) //this.setState(projects:projects)
  }

  handleDeleteProject(project) {
    console.log('handleDeleteProject')
    let projects = this.state.projects
    let idx = projects.findIndex ( x => x.id === project )
    projects.splice(idx, 1)
    this.setState(projects)

  }

  render() {
    return (
      <div className="App">
      <GetPosts />
      <AddProject addProject={this.handleAddProject.bind(this)}/>
       <Project projects={this.state.projects} onDelete={this.handleDeleteProject.bind(this)}/>
      </div>
    );
  }
}

export default App;
