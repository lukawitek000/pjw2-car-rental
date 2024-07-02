import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { OfferService } from '../../offer.service';
import { AuthService } from 'src/app/components/auth/auth.service';
import { BaseRouter } from 'src/app/base/base.router';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { CarService } from 'src/app/components/car/car.service';
import { Observable, debounceTime, distinctUntilChanged, map, switchMap } from 'rxjs';

@UntilDestroy()
@Component({
  selector: 'app-offer-add',
  templateUrl: './offer-add.component.html',
  styleUrls: ['./offer-add.component.scss']
})
export class OfferAddComponent extends BaseRouter implements OnInit {
  filteredPickupLocations$: Observable<any>;
  filteredReturnedLocations$: Observable<any>;
  private cars = [];
  filteredCars = [];

  offerForm = this.fb.group({
    car_id: [null, Validators.required],
    price_per_day: [null, Validators.required],
    extra_features: [null, Validators.required],
    start_date_time: [null, Validators.required],
    end_date_time: [null, Validators.required],
    pickup_location: [null, Validators.required],
    return_location: [null, Validators.required],
  });

  constructor(
    router: Router,
    readonly authService: AuthService,
    private readonly fb: FormBuilder,
    private readonly offerService: OfferService,
    private readonly datePipe: DatePipe,
    private readonly messageService: MessageService,
    private carService: CarService,
  ) { 
    super(router);
  }

  ngOnInit(): void {
    this.initializeCars();
    this.assignPickupLocationSubscription();
    this.assignReturnLocationSubscription();
  }

  private assignReturnLocationSubscription() {
    this.filteredReturnedLocations$ = this.offerForm.get('return_location').valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap(query => this.offerService.getSuggestedLocations(query)),
      map(location => location.suggestions.map(l => {
        return {
          location: l
        };
      }))
    );
  }

  private assignPickupLocationSubscription() {
    this.filteredPickupLocations$ = this.offerForm.get('pickup_location').valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap(query => this.offerService.getSuggestedLocations(query)),
      map(location => location.suggestions.map(l => {
        return {
          location: l
        };
      }))
    );
  }

  filterCars(event) {
    const query = event.query.toLowerCase();
    this.filteredCars = this.cars.filter(car =>
      car.name.toLowerCase().includes(query)
    );
  }

  onOfferAdd() {
    const timeFormat = 'yyyy-MM-ddTHH:mm:ss';
    const request = {
      ...this.offerForm.getRawValue(),
      car_id: this.offerForm.value.car_id.id,
      start_date_time: this.datePipe.transform(this.offerForm.value.start_date_time, timeFormat),
      end_date_time: this.datePipe.transform(this.offerForm.value.end_date_time, timeFormat)
    };

    this.offerService.addOffer(request)
    .pipe(
      untilDestroyed(this)
    )
    .subscribe(() => {
      this.messageService.add({severity:'success', summary: 'KCHOW!!!', detail: `Offer added succesfully`});
      setTimeout(() => {
        this.redirectToOffers();
      }, 500);
    })
  }

  private initializeCars() {
    this.carService.getAllOwnerCars()
    .pipe(
      untilDestroyed(this)
    )
    .subscribe((cars: any) => {
      this.cars = cars.cars.map(c => {
        return {
          id: c.car_id,
          name: `${c.car_make} ${c.car_model}`
        }
      })
    })

    this.filteredCars = this.cars;
  }
}
