import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './components/auth/register/register.component';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { OfferComponent } from './components/offer/offer.component';
import { OfferAddComponent } from './components/offer/components/offer-add/offer-add.component';
import { CarComponent } from './components/car/car.component';
import { CarAddComponent } from './components/car/components/car-add/car-add.component';
import { ReservationComponent } from './components/reservation/reservation.component';

const routes: Routes = [
  { 
    path: '', 
    component: LandingPageComponent 
  },
  { 
    path: 'register', 
    component: RegisterComponent 
  },
  {
    path: 'offers',
    children: [
      {
        path: '',
        component: OfferComponent,
      },
      {
        path: 'add',
        component: OfferAddComponent
      }
    ]
  },
  {
    path: 'cars',
    children: [
      {
        path: '',
        component: CarComponent,
      },
      {
        path: 'add',
        component: CarAddComponent
      }
    ]
  },
  {
    path: 'reservations',
    component: ReservationComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
