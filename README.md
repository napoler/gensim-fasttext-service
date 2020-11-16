# Gensim FastText Service

A demo web service wrapping up Gensim's FastText model and similarity query.

## Install

Simply run:

```bash
> python install -r requirements.txt
```

**Using a virtual environment is highly recommended.**

Before starting the web service, build the FastText model by running:

```bash
> python -m script.build_model
```

## Start the server

```bash
> gunicorn service.app:app -c ./gunicorn.py --worker-connections 100
```

Users can configure the way of how to start the service in `gunicorn.py`.

## APIs

### `/most-similar`

```bash
> curl -X POST -F "word=toys" -F "topn=5"  localhost:8080/most-similar
["and","spinner","sand","initial","negelected"]
```

The `topn` is set to be `10` by default:

```bash
> curl -X POST -F "word=toys" "localhost:8080/most-similar"
["and","spinner","hijacked","initial","sand","negelected","land","hand","december","hijackings"]
```

### `/health-check`

```bash
> curl -X GET "http://localhost:8080/health-check"
YES
```
