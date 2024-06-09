import { Component, OnInit } from '@angular/core';
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
    public readonly authService: AuthService,
    private readonly carService: CarService
  ) { }

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

