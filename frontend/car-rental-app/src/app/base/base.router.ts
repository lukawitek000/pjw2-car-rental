import { Router } from "@angular/router";

export class BaseRouter  {
    constructor(
        protected readonly router: Router
    ) {}

    redirectToOffers() {
        this.router.navigate(['/offers']);
    }
    
    redirectToOffersAdd() {
        this.router.navigate(['/offers/add']);
    }

    redirectToOwnerCars() {
        this.router.navigate(['/cars']);
    }

    redirectToOwnerCarsAdd() {
        this.router.navigate(['/cars/add']);
    }
}