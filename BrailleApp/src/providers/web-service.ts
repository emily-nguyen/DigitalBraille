import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class WebService {
  constructor(public http: Http) {
  }

  getTranslation() {
    let translation = this.http.get('http://localhost:5000/braille/image');

    return translation;
  }
}
