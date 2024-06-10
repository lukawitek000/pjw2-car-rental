import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, tap } from "rxjs";
import { environment } from "src/environments/environment";

@Injectable() 
export class OfferService {
    constructor(
        private http: HttpClient
    ) {}
    
    private readonly url = environment.apiUrl;

    getAllOffers(request: { search: string, fromDate: any, toDate: any }) {
        const params = new HttpParams()
        .set('start_date_time', request.fromDate)
        .set('end_date_time', request.toDate)
        .set('pickup_location', request.search)
        .set('return_location', request.search)

        return this.http.get(`${this.url}/get_all_offers`, { params });
    }

    getAllOwnedOffers() {
        return this.http.get(`${this.url}/get_all_owned_offers`);
    }

    addOffer(request: any) {
        return this.http.post(`${this.url}/add_offer`, request);
    }

    getSuggestedLocations(location: string) : Observable<any> {
        return this.http.get(`${this.url}/autocomplete?query=${location}`);
    }
}