import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.scss']
})
export class CarComponent implements OnInit {

  public offers$: Observable<any> | undefined;

  private today = new Date();
  private twoWeeksFromToday = new Date(this.today.getTime() + (14 * 24 * 60 * 60 * 1000));

  public utilForm = this.fb.group({
    search: [''],
    fromDate: [this.today],
    toDate: [this.twoWeeksFromToday]
  })
  

  constructor(
    private readonly fb: FormBuilder,
    private readonly datePipe: DatePipe
  ) { }

  ngOnInit(): void {
    const timeFormat = 'yyyy-MM-ddTHH:mm:ss';

    const filters = {
      search: this.utilForm.value.search,
      fromDate: this.datePipe.transform(this.utilForm.value.fromDate, timeFormat),
      toDate: this.datePipe.transform(this.utilForm.value.toDate, timeFormat)
    };
  }
}
