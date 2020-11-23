"""
File: app.py
Created Date: Monday, 2nd November 2020 9:18:53 am
Author: Tianyu Gu (gty@franz.com)
"""


from pathlib import Path

from flask import Flask, abort, jsonify, request
from gensim.models.keyedvectors import FastTextKeyedVectors

_data_folder = Path(__file__).parent.parent.joinpath("data")
_fasttext_wv = FastTextKeyedVectors.load(str(_data_folder.joinpath("fasttext.wv")))

app = Flask("gensim_fasttext_service")


@app.route("/most-similar", methods=["POST"])
def similar_by_word():
    word: str = request.form.get("word")
    topn_arg = request.form.get("topn", "10")
    if not topn_arg.isdigit():
        abort(400)

    topn: int = int(topn_arg)
    res = [candidate for candidate, _ in _fasttext_wv.most_similar(word, topn=topn)]
    return jsonify(res)


@app.route("/health-check", methods=["GET"])
def health_check():
    return "YES"
