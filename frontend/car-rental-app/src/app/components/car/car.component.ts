import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Observable } from 'rxjs';
import { CarService } from './car.service';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.scss']
})
export class CarComponent implements OnInit {

  public ownerCars$: Observable<any> | undefined;

  constructor(
    private readonly carService: CarService,
    private readonly authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.ownerCars$ = this.carService.getAllOwnerOffers();
  }

  onDeleteCar(ownerCar: any) {
    if (confirm(`Are you sure you want to delete ${ownerCar.car_make} ${ownerCar.car_model}?`)) {
    }
  }

  onLogout() {
    this.authService.logout();
  }
}

