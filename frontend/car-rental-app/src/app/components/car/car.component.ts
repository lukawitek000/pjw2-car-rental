import { Component, OnInit } from '@angular/core';
import { BehaviorSubject, switchMap, tap } from 'rxjs';
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
  private ownerCarsSub$ = new BehaviorSubject<any>(null);
  ownerCars$ = this.ownerCarsSub$.asObservable();

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
    this.carService.deleteCar(ownerCar.car_id)
    .pipe(
      switchMap(() => this.initializeCars())
    ).subscribe(() => this.messageService.add({severity:'error', summary: 'KCHOW!', detail: `Car deleted succesfully`}));
  }

  private getCars() {
    this.initializeCars()
    .subscribe();
  }

  private initializeCars() {
    return this.carService.getAllOwnerCars()
      .pipe(
      tap(cars => this.ownerCarsSub$.next(cars)),
    );
  }
}

