import React, { Component } from 'react';

class ProjectItem extends Component {
  deleteProject(id) {
    console.log('deleteProject in ProjectItem.js')
    console.log(id)
    this.props.onDelete(id)
  }

  render() {
    console.log(this.props)
    return (
      <li className="project">
        { this.props.project.title} ({this.props.project.category})
        <button onClick={this.deleteProject.bind(this, this.props.project.id)}>delete</button>
      </li>
    );
  }
}

export default ProjectItem;
