import React, { Component } from 'react';
import Post from './Post'
var axios = require('axios')

export default class GetPosts extends Component {
  constructor() {
    super()
    this.state = {'posts':[]}
  }

  getPosts() {
    axios.get('http://jsonplaceholder.typicode.com/posts')
      .then( resp => {
        this.setState({posts:resp.data})
      })
  }


  render() {
    let posts;
    if (this.state.posts) {
      posts = this.state.posts.map( p => {
        return (
          <Post key={p.id} post={p}/>
        )
      })
    }

    return (
      <div className="getposts">
        <button onClick={this.getPosts.bind(this)}>Get Posts</button>
        { posts }
      </div>
    )
  }
}
