import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { environment } from "src/environments/environment";

@Injectable() 
export class OfferService {
    constructor(
        private http: HttpClient
    ) {}
    
    private readonly url = environment.apiUrl;

    public getAllOffers(request: { search: string, fromDate: any, toDate: any }) : Observable<any> {
        const params = new HttpParams()
        .set('filter', request.search)
        .set('start_date_time', request.fromDate)
        .set('end_date_time', request.toDate);

        const httpOptions = {
            headers: new HttpHeaders({'Content-Type': 'application/json'})
          }

        console.log('getting')
        return this.http.get(`${this.url}/get_all_offers`, { params, headers: httpOptions.headers });
    }

    public addOffer(request: any) : Observable<any> {
        return this.http.post(`${this.url}/add_offer`, request);
    }
}