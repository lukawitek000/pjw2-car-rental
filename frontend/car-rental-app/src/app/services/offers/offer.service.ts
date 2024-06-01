import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { environment } from "src/environments/environment";

@Injectable() 
export class OfferService {
    constructor(
        private http: HttpClient
    ) {}
    
    private readonly url = environment.apiUrl;

    public getAllOffers() : Observable<any> {
        const params = {
        }

        return this.http.get(`${this.url}/get_all_offers`, {
            params: params
        });
    }
}