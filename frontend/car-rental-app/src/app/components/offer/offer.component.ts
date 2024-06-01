import { Component, OnInit } from '@angular/core';
import { OfferService } from 'src/app/services/offers/offer.service';

@Component({
  selector: 'app-offer',
  templateUrl: './offer.component.html',
  styleUrls: ['./offer.component.scss']
})
export class OfferComponent implements OnInit {

  public offers$ = this.offerService.getAllOffers();

  constructor(
    private offerService: OfferService
  ) { }

  ngOnInit(): void {
    this.offerService.getAllOffers().subscribe(console.log)
  }

}
