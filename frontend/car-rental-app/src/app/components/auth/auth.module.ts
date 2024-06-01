import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { RegisterComponent } from "./register/register.component";

@NgModule({
    declarations: [
        RegisterComponent
    ],
    imports:[
        FormsModule,
        ReactiveFormsModule
    ],
    exports: [
        RegisterComponent
    ]
  })
  export class AuthModule { }