import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { BehaviorSubject, Observable, debounceTime, distinctUntilChanged, map, switchMap, tap } from 'rxjs';
import { OfferService } from './offer.service';
import { AuthService } from '../auth/auth.service';
import { Router } from '@angular/router';
import { BaseRouter } from 'src/app/base/base.router';

@Component({
  selector: 'app-offer',
  templateUrl: './offer.component.html',
  styleUrls: ['./offer.component.scss']
})
export class OfferComponent extends BaseRouter implements OnInit {
  filteredLocations$: Observable<any>;

  private offersSub$ = new BehaviorSubject<any>(null);
  offers$ = this.offersSub$.asObservable();

  private today = new Date();
  private twoWeeksFromToday = new Date(this.today.getTime() + (14 * 24 * 60 * 60 * 1000));

  utilForm = this.fb.group({
    search: [''],
    fromDate: [this.today],
    toDate: [this.twoWeeksFromToday]
  })
  
  constructor(
    router: Router,
    readonly authService: AuthService,
    private readonly offerService: OfferService,
    private readonly fb: FormBuilder,
    private readonly datePipe: DatePipe
  ) { 
    super(router);
  }

  ngOnInit(): void {
    this.assignSearchSubscription();
  }

  private assignSearchSubscription() {
    this.filteredLocations$ = this.utilForm.get('search').valueChanges.pipe(
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

  onOffersGet(): void {
    const timeFormat = 'yyyy-MM-ddTHH:mm:ss';

    const filters = {
      search: this.utilForm.value.search,
      fromDate: this.datePipe.transform(this.utilForm.value.fromDate, timeFormat),
      toDate: this.datePipe.transform(this.utilForm.value.toDate, timeFormat)
    };

    this.offerService.getAllOffers(filters)
    .pipe(
      tap(offers => this.offersSub$.next(offers))
    )
    .subscribe();
  }
}
