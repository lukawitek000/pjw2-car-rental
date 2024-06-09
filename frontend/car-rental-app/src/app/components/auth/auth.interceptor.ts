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
    const token = this.userService.getToken();
    // "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QxIiwiZXhwIjoxNzE3OTQwMjA3fQ.cg6dzBdCBznbQMHEMwuvBqZvF9DmXLQX8US1Ota9B2s";
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
