import { TypedService } from "./TypedService";
import { AuthenticationRequest } from "~/platform/models/authentication/api/AuthenticationRequest";

import { Candidate } from "../models/candidate/Candidate";
import { JsonConvert } from "json2typescript";

export class CandidatesService extends TypedService {
  readonly candidatesUrl = "/management/cohort/{}/candidates/";
  private jsonConvert: JsonConvert = new JsonConvert();

  async fetchCandidatesInCohort(cohortId: Number): Promise<Candidate[]> {
    return this.get(this.candidatesUrl.replace("{}", cohortId.toString())).then(response => {
      return this.jsonConvert.deserializeArray(
        response.data.map(obj => JSON.parse(obj)),
        Candidate
      );
    }).catch(error => {
      console.error(error)
      return []
    });
  }

  async addCandidate(cohortId: Number, publicId: string): Promise<Boolean> {
    return this.post(this.candidatesUrl.replace("{}", cohortId.toString()), { public_id: publicId }).then(response => {
      return true;
    });
  }
}
