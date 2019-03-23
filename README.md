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

You can run the API in `DEV` or `PROD` mode:

```bash
[ENV=DEV/PROD] python run.py
```

### Testing the API

To test the API works, you can either use [postman](https://www.getpostman.com/) or from
command line using [curl](https://curl.haxx.se/)

```bash
curl -F 'file=@bank-full.csv' -XPOST http://localhost:5000/upload/csv
```


## TODO

* Add tests



