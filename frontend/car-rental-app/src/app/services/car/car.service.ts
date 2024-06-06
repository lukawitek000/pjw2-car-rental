import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { environment } from "src/environments/environment";

@Injectable() 
export class CarService {
    constructor(
        private http: HttpClient
    ) {}
    
    private readonly url = environment.apiUrl;

    public addCar(request: any ) : Observable<any> {
        return this.http.post(`${this.url}/add_car`, request);
    }
}