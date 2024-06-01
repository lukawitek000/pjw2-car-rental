import { NgModule } from "@angular/core";
import { OfferComponent } from "./offer.component";
import { OfferService } from "src/app/services/offers/offer.service";
import { CommonModule } from "@angular/common";
import { CalendarModule } from 'primeng/calendar';

@NgModule({
    declarations: [
        OfferComponent
    ],
    imports: [
        CommonModule,
        CalendarModule
    ],
    exports: [
        OfferComponent
    ],
    providers: [
        OfferService
    ]
  })
  export class OfferModule { }