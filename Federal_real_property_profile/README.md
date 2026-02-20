# Federal Real Property Profile (FRPP) Public Dataset 
1. [Source data.gov](https://catalog.data.gov/dataset/fy-2024-federal-real-property-profile-frpp-public-dataset)
2. [Data Dictionary](https://www.gsa.gov/policy-regulations/policy/real-property-policy-division-overview/asset-management/federal-real-property-council/frpc-guidance-library)


## Load data in DuckDB
Unzip the data and load in memory DuckDB.
```sql
unzip data/frpp_public_dataset.zip

D CREATE TABLE estate AS
  SELECT * FROM read_csv('frpp_public_dataset_fy24_07022025.csv',
                         types={'Acres': 'VARCHAR', 'Asset Height': 'VARCHAR', 'Number of Federal Contractors': 'VARCHAR','Number of Federal Employees': 'VARCHAR'});
```
