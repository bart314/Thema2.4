import React, { Component } from 'react';
import ProjectItem from './ProjectItem'

class Project extends Component {
  deleteProject(id) {
    console.log('deleteProject in Project.js')
    this.props.onDelete(id)
  }

  render() {
    console.log(this.props)
    let projectitems
    if (this.props.projects) {
      projectitems = this.props.projects.map( p => {
        return <ProjectItem key={p.title} project={p} onDelete={this.deleteProject.bind(this)} />
      })
    }

    return (
      <div className="projects">
       <h1>Projects part</h1>
       <ul>
       { projectitems }
       </ul>
      </div>
    );
  }
}

export default Project;
