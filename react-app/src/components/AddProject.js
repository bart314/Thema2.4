import React, { Component } from 'react';
import uuid from 'uuid'


class AddProject extends Component {
  static defaultProps = {
    'categories': ['Web Design','Web development', 'Mobile development']
  }

  constructor() {
    super()
    this.state = {
      'newproject':{}
    }
  }

  handleSubmit(e) {
    console.log('submitted')
    console.log(this.refs.title.value)
    this.setState( { newproject: {
      id:uuid.v4(),
      title: this.refs.title.value,
      category: this.refs.category.value,
    }}, function() {
      console.log(this.state)
      this.props.addProject(this.state.newproject)
    })
    e.preventDefault()
  }

  render() {
    let catOps = this.props.categories.map( c => {
      return <option key={c} value={c}>{c}</option>
    })

    return (
      <div>
      <h3>Add Project</h3>
      <form onSubmit={this.handleSubmit.bind(this)}>
        <label>Project name:</label>
        <input type="text" ref="title" />

        <label>Project category:</label>
        <select ref="category">
          {catOps}
        </select>
        <input type="submit" value="submit" / >
      </form>
      </div>
    );
  }
}

export default AddProject;
