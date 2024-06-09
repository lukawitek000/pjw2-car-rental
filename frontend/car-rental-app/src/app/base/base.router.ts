import { Router } from "@angular/router";

export class BaseRouter  {
    constructor(
        protected readonly router: Router
    ) {}

    redirectToOffers() {
        this.router.navigate(['/offers']);
      }
    
    redirectToOwnerCars() {
        this.router.navigate(['/cars']);
    }
}