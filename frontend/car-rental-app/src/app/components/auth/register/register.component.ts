import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { MessageService } from 'primeng/api';
import { AuthService } from 'src/app/components/auth/auth.service';
import { Router } from '@angular/router';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';

export enum Role {
  CAR_OWNER = 'car_owner',
  CUSTOMER = 'customer'
}

@UntilDestroy()
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {

  public userForm = this.fb.group({
    username: null,
    email: null,
    password: null,
    isCustomer: true
  })

  public shouldRegister = false;

  constructor(
    private readonly authService: AuthService,
    private readonly messageService: MessageService,
    private readonly fb: FormBuilder,
    private readonly router: Router
  ) { }

  onLogin() {
    const credentials = {
      username: this.userForm.value.username,
      password: this.userForm.value.password,
    }

    this.authService.login(credentials)
    .pipe(
      untilDestroyed(this)
    )
    .subscribe({
      error: err => this.showError(err),
      next:response => this.showLogin(response)
    });
  }

  onRegister() {
    const credentials = {
      username: this.userForm.value.username,
      email: this.userForm.value.email,
      password: this.userForm.value.password,
    }

    this.authService.register(this.determineCredentialsRole(credentials))
    .subscribe({
      error: err => this.showError(err),
      next:response => this.showLogin(response)
    });
  }

  showError(err: any) {
    this.messageService.add({severity:'error', summary: 'Error', detail: `${err.error.message}, you need to register`});
    this.shouldRegister = true;
  }

  showLogin(res: any) {
    this.messageService.add({severity:'success', summary: 'KCHOW!!!', detail: `Welcome ${res.username}`});
    setTimeout(() => {
      res.role === Role.CAR_OWNER ? this.redirectToOwnerCars() : this.redirectToOffers();
    }, 500);
  }

  onRegisterBack() {
    this.shouldRegister = !this.shouldRegister;
  }

  private determineCredentialsRole(credentials: any) {
    if(this.userForm.value.isCustomer) {
      return {
        ...credentials,
        role: Role.CUSTOMER
      }
    }
    else {
      return {
        ...credentials,
        role: Role.CAR_OWNER
      }
    }
  }

  private redirectToOffers() {
    this.router.navigate(['/offers']);
  }

  private redirectToOwnerCars() {
    this.router.navigate(['/cars']);
  }
}
