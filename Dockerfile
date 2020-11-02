FROM python:3.8.5

# python env
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install --no-cache-dir pipenv
WORKDIR /usr/src/gensim-fasttext-service
COPY . .
RUN pipenv install

# train and save the FastText model
RUN pipenv run python3 script/build_model.py

# Start the server
EXPOSE 80
CMD pipenv run gunicorn service.app:app -c gunicorn.py --worker-connections 100
