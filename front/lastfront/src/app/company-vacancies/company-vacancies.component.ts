import { NgFor, NgIf } from '@angular/common';
import { ChangeDetectorRef, Component, OnInit } from '@angular/core';

import { ActivatedRoute, RouterModule } from '@angular/router';

import { CompanyListComponent } from '../company-list/company-list.component';
import { Company } from '../company';

import { VacanciesService } from '../vacancies.service';
import { Vacancy } from '../vacancy';

@Component({
  selector: 'app-company-vacancies',
  standalone: true,
  imports: [NgIf, RouterModule, NgFor],
  templateUrl: './company-vacancies.component.html',
  styleUrl: './company-vacancies.component.css'
})
export class CompanyVacanciesComponent implements OnInit{
  
  // company: Company | undefined ;
  vacancies: Vacancy[]= [];
  companyId: any;


  constructor(private route: ActivatedRoute, private service: VacanciesService, private cdr: ChangeDetectorRef){
    
  }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    this.companyId = Number(routeParams.get('companyId'));
    this.refreshVacancies();
  }

  refreshVacancies() {
    console.log('Refreshing vacancies...');
    this.service.fetchVacancies().subscribe(data => {
      console.log('Data fetched:', data);
      this.vacancies = data.filter(vacancy => vacancy.company_id === this.companyId);
      console.log('Vacancies:', this.vacancies);
      this.cdr.detectChanges(); // Trigger change detection
    }, error => {
      console.error('Error fetching vacancies:', error);
    });
  }
}
