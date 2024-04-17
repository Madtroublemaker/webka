import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vacancy } from './vacancy';

@Injectable({
  providedIn: 'root'
})
export class VacanciesService {

  constructor(private http: HttpClient) { }

  fetchVacancies(): Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>("http://127.0.0.1:8000/api/vacancies/");
  }
}
