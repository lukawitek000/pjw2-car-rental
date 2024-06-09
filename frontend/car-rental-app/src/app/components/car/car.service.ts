import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { environment } from "src/environments/environment";

@Injectable() 
export class CarService {
    constructor(
        private http: HttpClient
    ) {}
    
    private readonly url = environment.apiUrl;

    public addCar(request: any ) {
        return this.http.post(`${this.url}/add_car`, request);
    }

    public gatCarModels() {
        return this.http.get(`${this.url}/car_models`);
    }

    public getAllOwnerOffers() {
        return this.http.get(`${this.url}/get_all_owned_cars`);
    }

    public deleteCar(carId: number) {
        return this.http.delete(`${this.url}/delete/${carId}`)
    }
}