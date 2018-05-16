import { Injectable } from '@angular/core';
import { Http } from '@angular/http'
import 'rxjs/add/operator/map'

@Injectable()
export class DataService {

  constructor(public http:Http) {
  }

  getPosts() {
    //console.log(this.http.get('http://jsonplaceholder.typicode.com/posts'))

    return this.http.get('http://jsonplaceholder.typicode.com/posts')
      .map(res => res.json())
  }

}
