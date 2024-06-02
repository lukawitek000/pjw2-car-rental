import { DatePipe } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { OfferService } from 'src/app/services/offers/offer.service';

@UntilDestroy()
@Component({
  selector: 'app-offer-add',
  templateUrl: './offer-add.component.html',
  styleUrls: ['./offer-add.component.scss']
})
export class OfferAddComponent {

  public offerForm = this.fb.group({
    car_id: [null, Validators.required],
    price_per_day: [null, Validators.required],
    extra_features: [null, Validators.required],
    start_date_time: [null, Validators.required],
    end_date_time: [null, Validators.required],
    pickup_location: [null, Validators.required],
    return_location: [null, Validators.required],
  });

  constructor(
    private readonly fb: FormBuilder,
    private readonly offerService: OfferService,
    private readonly datePipe: DatePipe
  ) { }

  onOfferAdd() {
    const timeFormat = 'yyyy-MM-ddTHH:mm:ss';
    const request = {
      ...this.offerForm.getRawValue(),
      start_date_time: this.datePipe.transform(this.offerForm.value.start_date_time, timeFormat),
      end_date_time: this.datePipe.transform(this.offerForm.value.end_date_time, timeFormat)
    };

    this.offerService.addOffer(request)
    .pipe(
      untilDestroyed(this)
    )
    .subscribe()
  }
}
