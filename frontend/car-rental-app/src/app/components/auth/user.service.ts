import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";

@Injectable() 
export class UserService {
    constructor(  
    ) {}
    private role = new BehaviorSubject<string|null>(null);
    private username = new BehaviorSubject<string|null>(null);
    private token = new BehaviorSubject<string|null>(null);

    public authorize(role, username, token) {
        this.role.next(role);
        this.username.next(username);
        this.token.next(token);
    }

    public getToken() {
        return this.token.value;
    }
}