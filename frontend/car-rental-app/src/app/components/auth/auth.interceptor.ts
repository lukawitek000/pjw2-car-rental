import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserService } from './user.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
    constructor(
        private readonly userService: UserService
    ) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QxIiwiZXhwIjoxNzE3OTM4MjcyfQ.d6rZYeZgaPhs21j4G9DXB4l-z2e9Ga-mDNbdrfaxEWI";
    //this.userService.getToken();
    console.log('intercepting', token)

    if (token) {
      const cloned = req.clone({
        headers: req.headers.set('Authorization', `Bearer ${token}`)
      });
      
      return next.handle(cloned);
    } else {
      return next.handle(req);
    }
  }
}
