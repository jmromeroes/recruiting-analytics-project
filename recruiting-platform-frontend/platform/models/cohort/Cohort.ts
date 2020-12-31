import { JsonObject, JsonProperty } from "json2typescript";

@JsonObject("Organization")
export class Organization {
    @JsonProperty("name", String)
    name: string = "";

    @JsonProperty("picture", String)
    picture: string = "";
}

@JsonObject("Cohort")
export class Cohort {
    @JsonProperty("id", Number)
    id: Number = 0;

    @JsonProperty("name", String)
    name: string = "";

    @JsonProperty("platform_name", String)
    platformName: string = "";

    @JsonProperty("opportunity_objective", String)
    opportunityObjective: string = "";

    @JsonProperty("opportunity_id", String)
    opportunityId: string = "";

    @JsonProperty("organizations", [Organization])
    organizations: Organization[] = [];

    @JsonProperty("slug", String)
    slug: string = "";
}
