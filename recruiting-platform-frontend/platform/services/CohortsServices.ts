import { TypedService } from "./TypedService";
import { AuthenticationRequest } from "~/platform/models/authentication/api/AuthenticationRequest";

import { Some, None, Option } from "space-lift";
import { Cohort } from "../models/cohort/Cohort";
import { JsonConvert } from "json2typescript";

export class CohortsService extends TypedService {
  readonly cohortsUrl = "/management/cohorts/";
  private jsonConvert: JsonConvert = new JsonConvert();

  async fetchCohorts(): Promise<Cohort[]> {
    return this.get(this.cohortsUrl).then(response => {
      return this.jsonConvert.deserializeArray(
        response.data.map(obj => JSON.parse(obj)),
        Cohort
      );
    });
  }

  async addCohort(opportunityId: string): Promise<Cohort> {
    return this.post(this.cohortsUrl, { opportunity_id: opportunityId }).then(response => {
      return this.jsonConvert.deserializeObject(
        JSON.parse(response.data),
        Cohort
      );
    }).catch(error => {
      console.error(error)
      return new Cohort();
    });
  }
}
