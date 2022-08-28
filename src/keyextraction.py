import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd

import re
import string
from statistics import StatisticsError
from tqdm import tqdm

from module.keyex import YAKE, TopicRank_


ya = YAKE()
TR = TopicRank_()
input_text=st.text_input('テキストを入力', 'Japan')
algo = st.radio("アルゴリズム選択", ("YAKE", "TopicRank", "PositionRank"), horizontal=True)
if st.button("実行", key=0):
    if algo == "YAKE":
        s, k = ya.extract_phrases(input_text.lower())
        text = ya._preprocess(input_text.lower())
        print(k)
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
        kwds_scrs = TR.extract_phrases(input_text.lower())
        print(kwds_scrs)
        text = TR._preprocess(input_text.lower())
        for i, ks in enumerate(kwds_scrs):
            keyword,score = ks
            if 3*i < len(kwds_scrs):     # 上位　1/3　は赤色のマーカー
                color = "#ffcccc"
            elif 3*i < 2*len(kwds_scrs):     # 中位　1/3　は橙色のマーカー
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

