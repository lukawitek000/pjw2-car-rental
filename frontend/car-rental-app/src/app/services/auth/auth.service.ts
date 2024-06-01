import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs";
import { environment } from "src/environments/environment";

@Injectable() 
export class AuthService {
    constructor(
        private http: HttpClient
    ) {}
    
    private readonly url = environment.apiUrl;

    public login(credentials: {username: any, password: any }) : Observable<any> {
        const params = {
            username: credentials.username,
            password: credentials.password,
        }

        return this.http.post(`${this.url}/login`, params);
    }

    public register(credentials: {username: any, email: any, password: any, role: any}) : Observable<any> {
        const params = {
            username: credentials.username,
            email: credentials.email,
            password: credentials.password,
            role: credentials.role
        }

        return this.http.post(`${this.url}/signup`, params);
    }
}
