import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service'

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  name:string
  age:number
  email:string
  address: Address
  hobbies:string[]
  posts:Post[]
  editable:boolean = false

  constructor(private dataService:DataService) {
  }

  ngOnInit() {
    this.name = 'henk'
    this.age = 42
    this.address = {
      street:'straatnaam',
      city:'Sneek',
      state:'Fryslân',
    }
    this.hobbies = ['code','piano spelen','werken']
    this.dataService.getPosts().subscribe( p => this.posts = p )
  }

  buttonClicked() {
    this.name = 'Karel de Boer'
  }

  addHobby(h) {
    this.hobbies.push(h)
    return false
  }

  changeEdit() {
    this.editable = !this.editable
  }
}

interface Address {
  street:string,
  city:string,
  state:string,
}

interface Post {
  id:number,
  title:string,
  body:string,
  userid:number,
}
