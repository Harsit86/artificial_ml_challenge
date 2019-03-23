# artificial_ml_challenge

## Getting started

To run the API, create a `python3` virtual environment using [mkvirtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

```bash
mkvirtualenv venv -p python3 -r requirements.txt
```

or [pyenv](https://github.com/pyenv/pyenv):

```bash
pyenv virtualenv 3.7.2 venv -r requirements.txt
```


### API

You can run the API in `DEV` or `PROD` mode:

```bash
[ENV=DEV/PROD] python run.py
```

The API exposes two endoints:

* `/upload/csv`
* `/bank_marketing/<model_version>/predict` e.g. `/bank_marketing/v1/predict`


To test the upload endpoints works, you can either use [postman](https://www.getpostman.com/) or from
command line using [curl](https://curl.haxx.se/)

```bash
curl -F 'file=@data/bank-full.csv' -XPOST http://localhost:5000/upload/csv
```

The API is developed using [flask](http://flask.pocoo.org/) and writes the csv files to in memory
[SQLite](https://www.sqlite.org/index.html) database.
 

## Model Build

Model build code and notebooks are in [models](./models). To run the [Jupyter notebooks](), create
an ipython kernel:

```bash
ipython kernel install --user --name=artificial_ml
```


## TODO

* Add tests



