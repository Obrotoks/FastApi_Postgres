# Objetive 

Try to create a postgres db and access through FastAPI. 

## Prequistes

- Docker version 23.0.5
- Postgres version 15
- Python 3.9


## Data

For this purpouse it's going to be use [this dataset](https://www.kaggle.com/datasets/sellingstories/travel-company-insurance-prediction?resource=download). In there we could find two csv:

- 1st File: Travel Company Old Clients; Number of observations: 682
- 2nd File: Travel Company New Clients; Number of observations: 1303

We are going to use only Travel Company New Clients.

## Install 

Clone it in your own directory and run:

```shell
docker compose up
```

## Uninstall

```shell
docker compose down --rmi all -v --remove-orphans
```

## Example of query 


```json
{
  "select": "num_age as Age, count(*) as Num_row",
  "group_by": "num_age",
"order_by": "count(*) desc"

}

```
