import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { CarService } from './car.service';
import { AuthService } from '../auth/auth.service';
import { Router } from '@angular/router';
import { BaseRouter } from 'src/app/base/base.router';

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.scss']
})
export class CarComponent extends BaseRouter implements OnInit {

  ownerCars$: Observable<any> | undefined;

  constructor(
    router: Router,
    readonly authService: AuthService,
    private readonly carService: CarService
  ) {
    super(router); 
  }

  ngOnInit(): void {
    this.getCars();
  }

  onDeleteCar(ownerCar: any) {
    this.carService.deleteCar(ownerCar.car_id).subscribe();
    this.getCars();
  }

  getCars() {
    this.ownerCars$ = this.carService.getAllOwnerOffers();
  }
}

