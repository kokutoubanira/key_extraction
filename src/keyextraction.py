import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import neologdn
import re
import string
from statistics import StatisticsError
from tqdm import tqdm

import textacy
from textacy.extract.keyterms import yake, sgrank, textrank, scake
from rake_ja import Tokenizer, JapaneseRake
from pke.unsupervised import MultipartiteRank, PositionRank, TopicRank


class YAKE():
    def __init__(self):
        self.ja = textacy.load_spacy_lang("ja_ginza_electra")
    # 前処理
    def _preprocess(self, x):
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "]+",
            flags=re.UNICODE,
        )
        x = emoji_pattern.sub(r"", x)

        x = neologdn.normalize(x)
        x = re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "", x)
        x = re.sub(r"[!-/:-@[-`{-~]", r" ", x)
        x = re.sub("[■-♯]", " ", x)
        x = re.sub(r"(\d)([,.])(\d+)", "\1\3", x)
        x = re.sub(r"\d+", "0", x)
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)

        return x

    def extract_phrases(self, data) :
        doc = textacy.make_spacy_doc(self._preprocess(data), lang=self.ja)
        try:
            keywords_with_score = [
                (kps, score) for kps, score in yake(doc, normalize="lemma", topn=15)
            ]

            keywords = [
                keywords_with_score[i][0] for i in range(len(keywords_with_score))
            ]
            # YAKEで計算されるスコアは数字が小さいほど順位が高い
            scores = [
                -keywords_with_score[i][1] for i in range(len(keywords_with_score))
            ]
        except StatisticsError:
            keywords = []
            scores = []

        return scores, keywords

class TopicRank_():
    def __init__(self):
        self.extractor = TopicRank()
    def extract_phrases(self, data):
        self.extractor.load_document(
            input=data, language="ja", normalization=None
        )
        self.extractor.candidate_selection(pos={"NOUN", "PROPN", "ADJ", "NUM"})
        self.extractor.candidate_weighting()

        kwds_scrs = self.extractor.get_n_best(n=15)

        if len(kwds_scrs) > 0:
            return [x[1] for x in kwds_scrs], [x[0] for x in kwds_scrs]
        else:
            return [], []


ya = YAKE()
TR = TopicRank_()
input_text=st.text_input('テキストを入力', 'Japan')
algo = st.radio("アルゴリズム選択", ("YAKE", "TopicRank", "PositionRank"), horizontal=True)
if st.button("実行", key=0):
    if algo == "YAKE":
        s, k = ya.extract_phrases(input_text)
        # score, key = 
        # st.write("", "".join([str(i) for i in score]))
        # st.write("", " ,".join([str(i) for i in key]))
        text = input_text
        for i, ks in enumerate(s):
            keyword = k[i]
            score = ks
            if 3*i < len(s):     # 上位　1/3　は赤色のマーカー
                color = "#ffcccc"
            elif 3*i < 2*len(s):     # 中位　1/3　は橙色のマーカー
                color = "#ffcc99"
            else:     # 下位　1/3　は黄色のマーカー
                color = "#ffffcc"
            edited_keyword = re.sub(r"\s+", "", keyword)
            text =  re.sub(edited_keyword, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + edited_keyword + "</mark>", text)
        html = """
        <html>
            <head>
                <title>キーフレーズ抽出</title>
            <head>

            <body>
                <h1 style="padding: 1rem 2rem;  color: #fff;  border-radius: 10px;  background-image: -webkit-gradient(linear, left top, right top, from(#f83600), to(#f9d423));background-image: -webkit-linear-gradient(left, #f83600 0%, #f9d423 100%);background-image: linear-gradient(to right, #f83600 0%, #f9d423 100%);">キーフレーズ抽出</h1>
        """
        html += text
        html += """
            </body>
        </html>
        """
        stc.html(html, height=500)
    if algo == "TopicRank":
        print("tr")
        s, k = TR.extract_phrases(input_text)
        # score, key = 
        # st.write("", "".join([str(i) for i in score]))
        # st.write("", " ,".join([str(i) for i in key]))
        print(TR.extract_phrases(input_text))
        text = input_text
        for i, ks in enumerate(s):
            keyword = k[i]
            score = ks
            if 3*i < len(s):     # 上位　1/3　は赤色のマーカー
                color = "#ffcccc"
            elif 3*i < 2*len(s):     # 中位　1/3　は橙色のマーカー
                color = "#ffcc99"
            else:     # 下位　1/3　は黄色のマーカー
                color = "#ffffcc"
            edited_keyword = re.sub(r"\s+", "", keyword)
            text =  re.sub(edited_keyword, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + edited_keyword + "</mark>", text)
        html = """
        <html>
            <head>
                <title>キーフレーズ抽出</title>
            <head>

            <body>
                <h1 style="padding: 1rem 2rem;  color: #fff;  border-radius: 10px;  background-image: -webkit-gradient(linear, left top, right top, from(#f83600), to(#f9d423));background-image: -webkit-linear-gradient(left, #f83600 0%, #f9d423 100%);background-image: linear-gradient(to right, #f83600 0%, #f9d423 100%);">キーフレーズ抽出</h1>
        """
        html += text
        html += """
            </body>
        </html>
        """
        stc.html(html, height=500)

