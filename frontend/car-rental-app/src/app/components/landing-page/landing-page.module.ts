import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { AuthModule } from "../auth/auth.module";
import { LandingPageComponent } from "./landing-page.component";
import {ToastModule} from 'primeng/toast';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MessageService } from "primeng/api";

@NgModule({
    declarations: [
        LandingPageComponent
    ],
    imports: [
        FormsModule,
        ReactiveFormsModule,
        AuthModule,
        ToastModule,
        BrowserAnimationsModule,
    ],
    exports: [
        LandingPageComponent
    ],
    providers: [
        MessageService
    ]
  })
  export class LandingPageModule { }