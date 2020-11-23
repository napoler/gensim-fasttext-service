"""
File: build_model.py
Created Date: Monday, 2nd November 2020 9:30:11 am
Author: Tianyu Gu (gty@franz.com)
"""

import logging
from pathlib import Path

from gensim import utils
from gensim.models import FastText
from gensim.test.utils import datapath

logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
)


class LeeBackgroundCorpus:
    def __iter__(self):
        with open(datapath("lee_background.cor")) as f:
            for line in f:
                yield utils.simple_preprocess(line)


def train_and_save_model(outdir: Path = Path(__file__).parent.parent.joinpath("data")):
    model = FastText(size=100, window=5, min_count=1)

    logging.info("Building Vocabulary")
    model.build_vocab(sentences=LeeBackgroundCorpus())

    logging.info("Training the FastText Model")
    model.train(
        sentences=LeeBackgroundCorpus(), total_words=model.corpus_total_words, epochs=5
    )

    if not outdir.exists():
        outdir.mkdir()
    model.wv.save(str(outdir.joinpath("fasttext.wv")))
    logging.info(
        "The trained model has been saved to %s", str(outdir.joinpath("fasttext.wv"))
    )


if __name__ == "__main__":
    train_and_save_model()
