import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthModule } from './components/auth/auth.module';
import { LandingPageModule } from './components/landing-page/landing-page.module';
import { HttpClientModule } from '@angular/common/http';
import { OfferModule } from './components/offer/offer.module';
import { CarModule } from './components/car/car.module';
@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    LandingPageModule,
    AuthModule,
    HttpClientModule,
    OfferModule,
    CarModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }