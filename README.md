# Gensim FastText Service

A web service wrapping up Gensim's FastText model and similarity query based on [lee_background corpus](https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/test/test_data/lee_background.cor).

## Install

Install all dependencies by the given `requirements.txt`.

```bash
> python install -r requirements.txt
```

**Using a virtual environment is highly recommended.**

Before starting the web service, build the FastText model by running:

```bash
> python -m script.build_model
```

## Start the web service

```bash
> gunicorn service.app:app -c ./gunicorn.py --worker-connections 100
```

Users can configure the way of how to start the service in `gunicorn.py`. Currently, the default setup is:

```python
bind = "0.0.0.0:8080"
workers = 1
timeout = 30
worker_class = "gevent"
```

For more details of deplyoing Gunicorn, please visit [here](https://docs.gunicorn.org/en/latest/deploy.html).

## APIs

### `/most-similar`

A **POST** method that exposes Gensim's [similarity query functionality](https://radimrehurek.com/gensim/auto_examples/core/run_similarity_queries.html#sphx-glr-auto-examples-core-run-similarity-queries-py).

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

A helper API to check service's availability.

```bash
> curl -X GET "http://localhost:8080/health-check"
YES
```
