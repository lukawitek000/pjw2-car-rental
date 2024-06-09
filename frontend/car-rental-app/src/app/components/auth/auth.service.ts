import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from "rxjs";
import { environment } from "src/environments/environment";
import { UserService } from "./user.service";
import { Router } from "@angular/router";

@Injectable() 
export class AuthService {
    constructor(
        private http: HttpClient,
        private readonly userService: UserService,
        private readonly router: Router
    ) {}
    
    private readonly url = environment.apiUrl;

    public login(credentials: {username: any, password: any }) : Observable<any> {
        const params = {
            username: credentials.username,
            password: credentials.password,
        }

        return this.http.post(`${this.url}/login`, params)
        .pipe(
            tap((x: any) => {
                this.userService.authorize(x.role, x.username, x.token);
            })
        );
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

    public logout() {
        this.userService.authorize(null, null, null);
        this.router.navigate(['/']);
    }
}
