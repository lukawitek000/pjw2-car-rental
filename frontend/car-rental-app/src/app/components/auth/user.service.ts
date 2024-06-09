import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";

@Injectable() 
export class UserService {
    constructor(  
    ) {}
    private role = new BehaviorSubject<string|null>(null);
    private username = new BehaviorSubject<string|null>(null);

    public authorize(role, username) {
        this.role.next(role);
        this.username.next(username);
    }
}