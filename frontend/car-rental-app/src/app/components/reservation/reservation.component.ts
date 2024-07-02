import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth/auth.service';
import { BehaviorSubject, of, tap } from 'rxjs';
import { OfferService } from '../offer/offer.service';
import { BaseRouter } from 'src/app/base/base.router';
import { Router } from '@angular/router';
import { UserService } from '../auth/user.service';

@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.scss']
})
export class ReservationComponent extends BaseRouter implements OnInit {
  private reservationsSub$ = new BehaviorSubject<any>(null);
  reservations$ = this.reservationsSub$.asObservable();

  constructor(
    router: Router,
    readonly authService: AuthService,
    readonly offerService: OfferService,
    readonly userService: UserService
  ) {
    super(router);
  }

  ngOnInit(): void {
    this.offerService.getReservations(this.userService.getCurrentUser())
    .pipe(
      tap((res) => this.reservationsSub$.next(res.reservations))
    )
    .subscribe();
  }

}
