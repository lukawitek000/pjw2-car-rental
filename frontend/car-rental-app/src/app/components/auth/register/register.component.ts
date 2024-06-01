import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {

  constructor() { }

  newUsername: string = '';
  newPassword: string = '';

  onRegister() {
    // Add your registration logic here
    console.log('Register clicked', this.newUsername, this.newPassword);
  }

}
