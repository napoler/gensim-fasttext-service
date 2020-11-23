#!/bin/sh

DIST="gensim-fasttext-service"

echo "gensim==3.8.3
flask==1.1.2
gunicorn[gevent]==20.0.4" > requirements.txt

mkdir -p $DIST

cp -r script $DIST/
cp -r service $DIST/
cp gunicorn.py $DIST/
cp requirements.txt $DIST/

pandoc -s README.md -t html -o doc.html
cp doc.html $DIST/

tar czvf gensim-fasttext-service.tar.gz --exclude="*__pycache__*" $DIST/

rm -f requirements.txt
rm -rf $DIST
rm *.html
