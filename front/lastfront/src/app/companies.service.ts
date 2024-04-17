import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Company } from './company';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {

  constructor(private http: HttpClient) { }

  fetchCompanies(): Observable<Company[]>{
    return this.http.get<Company[]>("http://127.0.0.1:8000/api/companies/");
  }
}
