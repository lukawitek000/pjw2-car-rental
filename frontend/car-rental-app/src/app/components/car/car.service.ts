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

    addCar(request: any ) {
        return this.http.post(`${this.url}/add_car`, request);
    }

    getCarModels(): Observable<any> {
        return this.http.get(`${this.url}/car_models`);
    }

    getAllOwnerOffers() {
        return this.http.get(`${this.url}/get_all_owned_cars`);
    }

   deleteCar(carId: number) {
        return this.http.delete(`${this.url}/delete/${carId}`)
    }
}