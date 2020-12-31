import { JsonObject, JsonProperty } from "json2typescript";
import { Organization } from "~/platform/models/cohort/Cohort";

@JsonObject("LinkInformation")
export class LinkInformation {
    @JsonProperty("name", String)
    name: string = "";

    @JsonProperty("url", String)
    url: string = "";
}

@JsonObject("JobInformation")
export class JobInformation {
    @JsonProperty("name", String)
    name: string = "";

    @JsonProperty("picture", [Organization])
    organizations: Organization[] = [];
}

@JsonObject("Candidate")
export class Candidate {
    @JsonProperty("username", String)
    username: string = "";

    @JsonProperty("country", String)
    country: string = "";

    @JsonProperty("platform_name", String)
    platformName: string = "";

    @JsonProperty("public_id", String)
    publicId: string = "";

    @JsonProperty("bio", String)
    bio: string = "";

    @JsonProperty("strengths", [String])
    strengths: string[] = [];

    @JsonProperty("interests", [String])
    interests: string[] = [];

    @JsonProperty("jobs", [JobInformation])
    jobs: JobInformation[] = [];

    @JsonProperty("links", [LinkInformation])
    links: LinkInformation[] = [];

    @JsonProperty("cohort_id", Number)
    cohort_id: Number = 0;

    @JsonProperty("number_of_strengths", Number)
    numberOfStrengths: Number = 0;
    
    @JsonProperty("number_of_jobs", Number)
    numberOfJobs: Number = 0;

    @JsonProperty("number_of_awards", Number)
    numberOfAwards: Number = 0;

    @JsonProperty("number_of_projects", Number)
    numberOfProjects: Number = 0;

    @JsonProperty("number_of_interests", Number)
    numberOfInterests: Number = 0;
}
