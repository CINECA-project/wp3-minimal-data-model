# CINECA WP3 Minimal Data Model
JSON Schema for minimal data model developed by WP3. 
This schema refer to the data model developed [here](https://docs.google.com/spreadsheets/d/1ZXqTMIhFtGOaodw7Fns5YghvY_pWos-RuSa2BFnO5l4/edit?pli=1#gid=0).

### Directory and file Structure
```
+-- schemas - contains source schema documents in yaml format 
+-- generated - generated files, should not edit  
|   +-- json - generated json files from yaml source
+-- yaml_to_json.py - python script to convert yaml to json
+-- README.md    
```
### Description
* `Cohort.yaml` contains the schema for cohort level attributes
* `Questionnaire.yaml` contains the survey/questionnaire data for individuals
* `AggregatedModel.yaml` contains the aggregation of both cohort and questionnaire (which might not be very useful)
* `CohortAttributes.yaml` - basic cohort attributes
* `Biosample.yaml` - biosample (NCIT:C43412)
* `LaboratoryMeasures.yaml` - laboratory measures (Laboratory Procedure NCIT:C25294)
* `SurveyAdministration.yaml` - survey administration (NCIT:C64252)
