import { NgModule } from "@angular/core";
import { OfferComponent } from "./offer.component";
import { CommonModule, DatePipe } from "@angular/common";
import { CalendarModule } from 'primeng/calendar';
import { OfferAddComponent } from './components/offer-add/offer-add.component';
import { RouterModule } from "@angular/router";
import { ReactiveFormsModule } from "@angular/forms";
import { OfferService } from "./offer.service";
import { HTTP_INTERCEPTORS } from "@angular/common/http";
import { AuthInterceptor } from "../auth/auth.interceptor";

@NgModule({
    declarations: [
        OfferComponent,
        OfferAddComponent
    ],
    imports: [
        CommonModule,
        CalendarModule,
        RouterModule,
        ReactiveFormsModule,
    ],
    exports: [
        OfferComponent,
        OfferAddComponent
    ],
    providers: [
        OfferService,
        DatePipe,
        { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
    ]
  })
  export class OfferModule { }