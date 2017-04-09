import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { WebService } from '../../providers/web-service';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html',
  providers: [WebService]
})
export class HomePage {
  brailleDots: Array<string>;
  imageUrl: string;

  constructor(public navCtrl: NavController, public service: WebService) {
    this.brailleDots = [];
    this.imageUrl = '';
  }

  translateText() {
    console.log('imageUrl');
    console.log(this.imageUrl);
    if (this.imageUrl != '') {
      this.getTranslation();
    }
    console.log('translated dots');
    console.log(this.brailleDots);
  }

  getTranslation() {
    this.service.getTranslation().subscribe(
      data => {
        this.brailleDots = data.json();
      },
      err => console.log(err),
      () => console.log('getTranslation completed')
    );
  }
}
