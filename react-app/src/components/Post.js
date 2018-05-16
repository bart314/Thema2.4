import React, { Component } from 'react';

export default class Post extends Component {
  render() {
    return (
      <div>
        <b>{this.props.post.title}</b><br/>
        <p>{this.props.post.body}</p>
      </div>
    )
  }
}
