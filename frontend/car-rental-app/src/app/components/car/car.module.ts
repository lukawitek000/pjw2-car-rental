import { NgModule } from "@angular/core";
import { CarComponent } from "./car.component";
import { CarAddComponent } from "./components/car-add/car-add.component";
import { CommonModule, DatePipe } from "@angular/common";
import { RouterModule } from "@angular/router";
import { ReactiveFormsModule } from "@angular/forms";
import { CalendarModule } from "primeng/calendar";
import { CarService } from "./car.service";
import { HTTP_INTERCEPTORS } from "@angular/common/http";
import { AuthInterceptor } from "../auth/auth.interceptor";

@NgModule({
    declarations: [
        CarComponent,
        CarAddComponent
    ],
    imports: [
        CommonModule,
        RouterModule,
        CalendarModule,
        ReactiveFormsModule
    ],
    exports: [
        CarComponent,
        CarAddComponent
    ],
    providers: [
        CarService,
        DatePipe,
        { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
    ]
  })
  export class CarModule { }