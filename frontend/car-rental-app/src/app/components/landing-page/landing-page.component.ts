import { Component } from '@angular/core';
import { MessageService } from 'primeng/api';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent {


  constructor(
    private readonly messageService: MessageService,
    ) {}

    onKchaw() {
      this.messageService.add({severity:'error', summary: 'KCHOW!!!'});
    }
}
