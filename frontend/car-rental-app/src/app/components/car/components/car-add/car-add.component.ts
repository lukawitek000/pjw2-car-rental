import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { CarService } from '../../car.service';
import { AuthService } from 'src/app/components/auth/auth.service';
import { BaseRouter } from 'src/app/base/base.router';
import { Router } from '@angular/router';
import { Observable, map } from 'rxjs';
import { MessageService } from 'primeng/api';


@UntilDestroy()
@Component({
  selector: 'app-car-add',
  templateUrl: './car-add.component.html',
  styleUrls: ['./car-add.component.scss']
})
export class CarAddComponent extends BaseRouter implements OnInit {
  private carMakers = [];
  private carModels = [];
  filteredCarMakers = [];
  filteredModels = [];

  carForm = this.fb.group({
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
    private readonly datePipe: DatePipe,
    private readonly messageService: MessageService,
  ) { 
    super(router); 
  }

  ngOnInit(): void {
    this.initializeDropdowns()
  }

  onCarAdd() {
    const timeFormat = 'yyyy';
    const request = {
      ...this.carForm.getRawValue(),
      car_make: this.carForm.value.car_make.name,
      car_model: this.carForm.value.car_model.name,
      car_year: this.datePipe.transform(this.carForm.value.car_year, timeFormat)
    };

    this.carService.addCar(request)
    .pipe(
      untilDestroyed(this)
    )
    .subscribe(() => {
      this.messageService.add({severity:'success', summary: 'KCHOW!!!', detail: `Car added succesfully`});
      setTimeout(() => {
        this.redirectToOwnerCars();
      }, 500);
    })
  }

  filterCarMakers(event) {
    const query = event.query.toLowerCase();
    this.filteredCarMakers = this.carMakers.filter(manufacturer =>
      manufacturer.name.toLowerCase().includes(query)
    );
  }

  filterCarModels(event) {
    const query = event.query.toLowerCase();
    this.filteredModels = this.carModels.filter(model =>
      model.name.toLowerCase().includes(query) && 
      model.manufacturer.toLowerCase().includes(this.carForm.value.car_make.name.toLowerCase())
    );
  }

  private initializeDropdowns() {
    this.carService.getCarModels()
    .pipe(
      untilDestroyed(this)
    )
    .subscribe(dict => {
      this.initializeCarMakers(dict);
      this.initializeCarModels(dict);
    })
  }

  private initializeCarMakers(dict) {
    this.carMakers = dict.cars.map(c => {
      return {
        name: c.manufacturer
      }
    });

    this.filteredCarMakers = this.carMakers;
  }

  private initializeCarModels(dict) {
    this.carModels = dict.cars.flatMap(c => {
      return c.models.flatMap(m => {
        return {
          manufacturer: c.manufacturer,
          name: m.model
        }
      })
    });
    
    this.filteredCarMakers = this.carModels;
  }
}
