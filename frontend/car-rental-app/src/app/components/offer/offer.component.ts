import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { BehaviorSubject, Observable, debounceTime, distinctUntilChanged, map, switchMap, tap } from 'rxjs';
import { OfferService } from './offer.service';
import { AuthService } from '../auth/auth.service';
import { Router } from '@angular/router';
import { BaseRouter } from 'src/app/base/base.router';
import { UserService } from '../auth/user.service';
import { MessageService } from 'primeng/api';

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
  private readonly timeFormat = 'yyyy-MM-ddTHH:mm:ss';

  utilForm = this.fb.group({
    search: [''],
    fromDate: [this.today],
    toDate: [this.twoWeeksFromToday]
  })
  
  constructor(
    router: Router,
    readonly authService: AuthService,
    readonly userService: UserService,
    private readonly offerService: OfferService,
    private readonly fb: FormBuilder,
    private readonly datePipe: DatePipe,
    private readonly messageService: MessageService,
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
    const filters = {
      search: this.utilForm.value.search,
      fromDate: this.datePipe.transform(this.utilForm.value.fromDate, this.timeFormat),
      toDate: this.datePipe.transform(this.utilForm.value.toDate, this.timeFormat)
    };

    this.offerService.getAllOffers(filters)
    .pipe(
      tap(offers => this.offersSub$.next(offers))
    )
    .subscribe();
  }

  onReserve(offer) {
    const request = {
      user_id: this.userService.getCurrentUser(),
      offer_id: offer.offer_id,
      start_date_time: this.datePipe.transform(offer.start_date_time, this.timeFormat),
      end_date_time: this.datePipe.transform(offer.end_date_time, this.timeFormat)
    }
    this.offerService.makeReservation(request).subscribe(() => {
      this.messageService.add({severity:'success', summary: 'KCHOW!!!', detail: `Reservation made succesfully!`});
      setTimeout(() => {
        this.redirectToReservations();
      }, 500);
    })
  }
  
  redirectToReservations() {
    this.router.navigate(['/reservations']);
  }
}
