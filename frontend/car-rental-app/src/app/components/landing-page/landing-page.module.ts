import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { AuthModule } from "../auth/auth.module";
import { LandingPageComponent } from "./landing-page.component";

@NgModule({
    declarations: [
        LandingPageComponent
    ],
    imports: [
        FormsModule,
        ReactiveFormsModule,
        AuthModule
    ],
    exports: [
        LandingPageComponent
    ]
  })
  export class LandingPageModule { }