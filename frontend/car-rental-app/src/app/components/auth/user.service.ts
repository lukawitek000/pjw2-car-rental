import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";
import { Role } from "./register/register.component";

@Injectable() 
export class UserService {
    constructor(  
    ) {}
    private role = new BehaviorSubject<string|null>(null);
    private username = new BehaviorSubject<string|null>(null);
    private token = new BehaviorSubject<string|null>(null);

    authorize(role, username, token) {
        this.role.next(role);
        this.username.next(username);
        this.token.next(token);
    }

    getToken() {
        return this.token.value;
    }

    isOwner() {
        return this.role.value === Role.CAR_OWNER;
    }
}