import { Component, OnInit } from '@angular/core';
import { CarService } from '../car.service';
import { AuthService } from '../../auth/auth.service';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { ConfirmationService } from 'primeng/api';

@Component({
  selector: 'app-owner-car',
  templateUrl: './owner-car.component.html',
  styleUrls: ['./owner-car.component.scss']
})
export class OwnerCarComponent implements OnInit {

  public ownerCars$: Observable<any> | undefined;

  constructor(
    private readonly carService: CarService,
    private readonly authService: AuthService,
    private readonly router: Router,
    private confirmationService: ConfirmationService
  ) { }

  ngOnInit(): void {
    this.ownerCars$ = this.carService.getAllOwnerOffers();
  }
  
  onEditCar(ownerCar: any) {
    this.router.navigate(['/edit-car', ownerCar.id]);
  }

  onDeleteCar(ownerCar: any) {
    if (confirm(`Are you sure you want to delete ${ownerCar.car_make} ${ownerCar.car_model}?`)) {
    }
  }

  onLogout() {
    this.authService.logout();
  }
}
