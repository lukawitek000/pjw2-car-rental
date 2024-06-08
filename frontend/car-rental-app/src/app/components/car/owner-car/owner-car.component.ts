import { Component, OnInit } from '@angular/core';
import { CarService } from '../car.service';
import { AuthService } from '../../auth/auth.service';

@Component({
  selector: 'app-owner-car',
  templateUrl: './owner-car.component.html',
  styleUrls: ['./owner-car.component.scss']
})
export class OwnerCarComponent implements OnInit {

  constructor(
    private readonly carService: CarService,
    private readonly authService: AuthService
  ) { }

  ngOnInit(): void {
    this.carService.getAllOwnerOffers().subscribe(console.log)
  }
  
  onLogout() {
    this.authService.logout();
  }
}
