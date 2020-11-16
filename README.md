# Gensim FastText Service

An example repository to build the Docker container that exposes the `most_similar` API.

## Install

It depends on [pipenv](https://pipenv.pypa.io/en/latest/) to install packages.

```bash
pipenv install
```

## Build Model

```bash
> python -m script.build_model
```

## Run

```bash
> gunicorn service.app:app -c ./gunicorn.py --worker-connections 100
```

## APIs

### `/most-similar`

```bash
> curl -X POST -F "word=toys" -F "topn=5"  localhost:8080/most-similar
["and","spinner","sand","initial","negelected"]
```

The `topn` is set to be `10` by default:

```bash
> curl -X POST -F "word=toys"  localhost:8080/most-similar
["and","spinner","hijacked","initial","sand","negelected","land","hand","december","hijackings"]
```

### `/health-check`

```bash
> curl -X GET "http://localhost:8080/health-check"
YES
```
