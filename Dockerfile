FROM ubuntu:latest

RUN apt-get update && apt-get install -y pandoc
WORKDIR /usr/src/gensim-fasttext-service
COPY . .

# Build the release
CMD ./release.sh
