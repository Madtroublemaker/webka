import { Component } from '@angular/core';
import { Company } from '../company';
import { CompaniesService } from '../companies.service';
import { NgFor } from '@angular/common';
import { RouterOutlet, RouterModule } from '@angular/router';

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [NgFor, RouterOutlet, RouterModule],
  templateUrl: './company-list.component.html',
  styleUrl: './company-list.component.css'
})
export class CompanyListComponent {
  companies: Company[] = [];

  constructor(private CompaniesSer: CompaniesService){}


  ngOnInit(): void{
    this.refreshCompanies()
  }

  refreshCompanies() {
    this.CompaniesSer.fetchCompanies().subscribe(data=>{
      this.companies = data;
    });
  }
}
