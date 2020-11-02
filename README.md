# Gensim FastText Service

An example repository to build the Docker container that exposes the `most_similar` API.

## Build

```bash
> docker build -t gensim_fasttext_service .
```

## Run

```bash
> docker run -d -p 8080:80 -it gensim_fasttext_service
```

## APIs

### `/most-similar`

```bash
> curl -X POST -F "word=toys" -F "topn=5"  localhost:8080/most-similar
["and","spinner","sand","initial","negelected"]
```

### `/health-check`

```bash
> curl -X GET "http://localhost:8080/health-check"
YES
```
