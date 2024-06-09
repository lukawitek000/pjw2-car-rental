import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { CarService } from '../../car.service';
import { AuthService } from 'src/app/components/auth/auth.service';
import { BaseRouter } from 'src/app/base/base.router';
import { Router } from '@angular/router';


@UntilDestroy()
@Component({
  selector: 'app-car-add',
  templateUrl: './car-add.component.html',
  styleUrls: ['./car-add.component.scss']
})
export class CarAddComponent extends BaseRouter implements OnInit {

  public carForm = this.fb.group({
    car_id: [null, Validators.required],
    car_model: [null, Validators.required],
    car_make: [null, Validators.required],
    car_year: [null, Validators.required],
    fuel_type: [null, Validators.required],
    transmission: [null, Validators.required],
    mileage: [null, Validators.required],
    additional_features: [null, Validators.required],
  });


  constructor(
    router: Router,
    readonly authService: AuthService,
    private readonly fb: FormBuilder,
    private carService: CarService,
    private readonly datePipe: DatePipe
  ) { 
    super(router); 
  }

  ngOnInit(): void {
    this.carService.gatCarModels().subscribe(console.log)
  }

  onCarAdd() {
    const timeFormat = 'yyyy-MM-ddTHH:mm:ss';
    const request = {
      ...this.carForm.getRawValue(),
      car_year: this.datePipe.transform(this.carForm.value.car_year, timeFormat)
    };

    this.carService.addCar(request)
    .pipe(
      untilDestroyed(this)
    )
    .subscribe()
  }
}
