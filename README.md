# Artifical Labs ML Challenge 

## Getting started

To run the API, create a `python3` virtual environment using [mkvirtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

```bash
mkvirtualenv venv -p python3 -r requirements.txt
```

or [pyenv](https://github.com/pyenv/pyenv):

```bash
pyenv virtualenv 3.7.2 venv -r requirements.txt
```


### API Endpdoints

You can run the API as follows:

```bash
python run.py
```

The API exposes the following endpoints 

1. CSV upload - `/upload/csv`
1. Customer endpont - `/customer/<customer_id>` e.g. `/customer/1` - **This is purely to show that the csv upload endpoint 
woks, it should only be called after the CSV file has been uploaded otherwise it will return an error message.**
1. Model prediction endpoint -`/bank_marketing/v1/predict` 


#### CSV Upload 

To test the upload endpoints works, you can either use [postman](https://www.getpostman.com/) or from
command line using [curl](https://curl.haxx.se/)

```bash
curl -F 'file=@data/bank-full.csv' -XPOST http://localhost:5000/upload/csv
```

The API is developed using [flask](http://flask.pocoo.org/) and writes the csv files to in memory
[SQLite](https://www.sqlite.org/index.html) database.

To verify the the data is saved to database, a `/customer/<customer_id>` endpoint is also exposed, run:

```bash
curl -XGET http://localhost:5000/customer/100
``` 

which will return the 100<sup>th</sup> customer detail in the csv file

```json
{
  "message": {
    "age": 46,
    "balance": 229,
    "campaign": 1,
    "contact": "unknown",
    "day": 5,
    "default": "no",
    "duration": 197,
    "education": "tertiary",
    "housing": "yes",
    "job": "management",
    "loan": "no",
    "marital": "married",
    "month": "may",
    "pdays": -1,
    "poutcome": "unknown",
    "previous": 0,
    "y": "no"
  },
  "status": "success"
}
```


#### Model Prediction

To test the model prediction endpoints, run the API as instructed above and use the sample json data in [data](./data).

Running

```bash
curl -XPOST -H 'Content-type: application/json' -d @data/sample_predict_data_success.json http://localhost:5000/bank_marketing/v1/predict
```

will return a response with status `success` as follows.


```json
{
  "message": "Likelihood of subscribing to product: 2.140 %.",
  "probability": 2.14,
  "status": "success"
}
```

Running 

```bash
curl -XPOST -H 'Content-type: application/json' -d @data/sample_predict_data_invalid_month.json http://localhost:5000/bank_marketing/v1/predict
```

will return a response with status `error` as follows.


```json
{
  "message": {
    "month": [
      "Not a valid choice."
    ]
  },
  "status": "error"
}
```
 

## Model Build

Model build code and notebooks are in [models](./models). To run the [Jupyter notebooks](https://jupyter.org/), create
an ipython kernel:

```bash
ipython kernel install --user --name=artificial_ml
```


## TODO

Additional work that needs to be done if 

* Add tests
* Add docstrings to functions
* Better documentation
* Swagger UI for endpoints
* Better error handling and messages
* Tune model and perhaps exclude `duration` as the feature causes leakage according to [here](https://archive.ics.uci.edu/ml/datasets/bank+marketing)


