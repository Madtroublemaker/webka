import { Routes } from '@angular/router';
import { CompanyListComponent } from './company-list/company-list.component';
import { CompanyVacanciesComponent } from './company-vacancies/company-vacancies.component';

export const routes: Routes = [
    { path: 'companies', component: CompanyListComponent, data: { title: 'Companies Page' }},
    { path: ':companyId', component: CompanyVacanciesComponent, data: { title: 'Company vacancies Page' }},
    { path: '', redirectTo: '/companies', pathMatch: 'full' },
];
