import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { CarService } from './car.service';
import { AuthService } from '../auth/auth.service';
import { Router } from '@angular/router';
import { BaseRouter } from 'src/app/base/base.router';
import { MessageService } from 'primeng/api';

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
    private readonly carService: CarService,
    private readonly messageService: MessageService
    
  ) {
    super(router); 
  }

  ngOnInit(): void {
    this.getCars();
  }

  onDeleteCar(ownerCar: any) {
    this.carService.deleteCar(ownerCar.car_id).subscribe();
    this.messageService.add({severity:'error', summary: 'Error', detail: `Car deleted succesfully`});
    this.getCars();
  }

  getCars() {
    this.ownerCars$ = this.carService.getAllOwnerCars();
  }
}

