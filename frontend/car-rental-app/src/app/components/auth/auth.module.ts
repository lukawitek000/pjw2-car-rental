import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { RegisterComponent } from "./register/register.component";
import { AuthService } from "src/app/components/auth/auth.service";
import {ToastModule} from 'primeng/toast';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MessageService } from "primeng/api";
import {InputSwitchModule} from 'primeng/inputswitch';

@NgModule({
    declarations: [
        RegisterComponent
    ],
    imports:[
        FormsModule,
        ReactiveFormsModule,
        ToastModule,
        BrowserAnimationsModule,
        InputSwitchModule
    ],
    exports: [
        RegisterComponent
    ],
    providers: [
        AuthService,
        MessageService
    ]
  })
  export class AuthModule { }