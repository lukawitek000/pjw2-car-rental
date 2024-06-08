import { NgModule } from "@angular/core";
import { CarComponent } from "./car.component";
import { CarAddComponent } from "./components/car-add/car-add.component";
import { CommonModule, DatePipe } from "@angular/common";
import { RouterModule } from "@angular/router";
import { ReactiveFormsModule } from "@angular/forms";
import { CalendarModule } from "primeng/calendar";
import { CarService } from "./car.service";

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
        DatePipe
    ]
  })
  export class CarModule { }