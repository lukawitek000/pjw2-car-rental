import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Observable } from 'rxjs';
import { OfferService } from './offer.service';

@Component({
  selector: 'app-offer',
  templateUrl: './offer.component.html',
  styleUrls: ['./offer.component.scss']
})
export class OfferComponent implements OnInit {
  
  public offers$: Observable<any> | undefined;

  private today = new Date();
  private twoWeeksFromToday = new Date(this.today.getTime() + (14 * 24 * 60 * 60 * 1000));

  public utilForm = this.fb.group({
    search: [''],
    fromDate: [this.today],
    toDate: [this.twoWeeksFromToday]
  })
  
  constructor(
    private offerService: OfferService,
    private readonly fb: FormBuilder,
    private readonly datePipe: DatePipe
  ) { }

  ngOnInit(): void {
    this.onOffersGet();
  }

  onOffersGet(): void {
    const timeFormat = 'yyyy-MM-ddTHH:mm:ss';

    const filters = {
      search: this.utilForm.value.search,
      fromDate: this.datePipe.transform(this.utilForm.value.fromDate, timeFormat),
      toDate: this.datePipe.transform(this.utilForm.value.toDate, timeFormat)
    };

    this.offers$ = this.offerService.getAllOffers(filters);
  }
}
