DIST="gensim-fasttext-service"

echo "gensim==3.8.3
flask==1.1.2
gunicorn[gevent]==20.0.4" > requirements.txt

mkdir -p $DIST

cp -r script $DIST/
cp -r service $DIST/
cp gunicorn.py $DIST/
cp requirements.txt $DIST/

zip -r gensim-fasttext-service.zip $DIST/ -x "*__pycache__*"

rm -f requirements.txt
rm -rf $DIST
