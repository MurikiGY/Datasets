# Federal Real Property Profile (FRPP) Public Dataset 
1. [Source data.gov](https://catalog.data.gov/dataset/fy-2024-federal-real-property-profile-frpp-public-dataset)
2. [Data Dictionary](https://www.gsa.gov/policy-regulations/policy/real-property-policy-division-overview/asset-management/federal-real-property-council/frpc-guidance-library)

## Structure
- `data`: Compressed data
- `dictionary_docs`: Official documentation for the dataset
- `rules`: Extracted rules from official documentation
    - `interpreting.json`: Mapping from documentation sentences to rules;
    - `constraints.json`: Human interpreted constraints. (FD, CFD, DC, tuple-level DC)


## Load data in DuckDB
Unzip the data and load in memory DuckDB.
```sql
$ unzip data/frpp_public_dataset.zip

D CREATE TABLE estate AS
  SELECT * FROM read_csv('frpp_public_dataset_fy24_07022025.csv',
                         types={'Acres': 'VARCHAR', 'Asset Height': 'VARCHAR', 'Number of Federal Contractors': 'VARCHAR','Number of Federal Employees': 'VARCHAR'});
```


## Mapping from CFD's to CDC's
Mapeamento do tableau (Considerando a RHS com apenas um atributo)
1. Cada atributo da RHS gera um "conjunto" de CDC's de tamanho igual ao numero de linhas do tableau 
2. Cada linha do tableau vira uma CDC incluida em cada conjunto de #1
3. Quando o tableau especifica uma constante no atributo A na LHS, o atributo A nao deve ser incluido no predicado pois eh redundante
4. Uma CDC é single tuple level se, e somente se, possua apenas predicados com constantes;


## General Notes

1. Real Property Use Tableau

```sql
-- OK FD: "Real Property Use" -> "Real Property Use Code"
SELECT
    "Real Property Use",
    COUNT(DISTINCT "Real Property Use Code") AS "Real Property Use Code Distincs"
FROM estate
GROUP BY "Real Property Use"
HAVING COUNT(DISTINCT "Real Property Use Code") > 1;

-- NOT OK FD "Real Property Use Code" -/> "Real Property Use" (Does not work)
SELECT
    "Real Property Use Code",
    COUNT(DISTINCT "Real Property Use") AS "Distincs"
FROM estate
GROUP BY "Real Property Use Code"
HAVING COUNT(DISTINCT "Real Property Use") > 1;

-- CFD: "Real Property Type Code" = 20 AND "Real Property Use Code" -> "Real Property Use"
SELECT
    "Real Property Use Code",
    COUNT(DISTINCT "Real Property Use") AS "Distincs"
FROM estate
WHERE "Real Property Type Code" = 20 
GROUP BY "Real Property Use Code"
HAVING COUNT(DISTINCT "Real Property Use") > 1;
```
