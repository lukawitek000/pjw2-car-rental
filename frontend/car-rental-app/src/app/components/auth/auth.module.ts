import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { RegisterComponent } from "./register/register.component";
import { AuthService } from "src/app/components/auth/auth.service";
import {ToastModule} from 'primeng/toast';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MessageService } from "primeng/api";
import {InputSwitchModule} from 'primeng/inputswitch';
import { UserService } from "./user.service";
import { HTTP_INTERCEPTORS } from "@angular/common/http";
import { AuthInterceptor } from "./auth.interceptor";

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
        MessageService,
        UserService,
        { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
    ]
  })
  export class AuthModule { }