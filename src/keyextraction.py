import streamlit as st
import streamlit.components.v1 as stc
import re
import string
from statistics import StatisticsError
from tqdm import tqdm

from module.keyex import YAKE, TopicRank_, PositionRank_, SGRank, TextRank, sCAKE, MultipartiteRank_, output_html
from module.keyex import output_html 

YA = YAKE()
TR = TopicRank_()
SRG = SGRank()
TXTR = TextRank()
sC = sCAKE()
PR = PositionRank_()
MR = MultipartiteRank_()

input_text=st.text_area(label='テキストを入力', value='', max_chars=1000)
algo = st.radio("アルゴリズム選択", ("YAKE", "TopicRank","SGRank","TextRank","sCAKE","MultipartiteRank","PositionRank",), horizontal=True)

if st.button("実行", key=0):
    if algo == "YAKE":
        word = []
        s, k = YA.extract_phrases(input_text.lower())
        text = YA._preprocess(input_text.lower())
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
            word.append(edited_keyword.lower())
            for t in edited_keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)
        html = output_html(text, word)
        stc.html(html, height=1000)

    if algo == "TopicRank":
        word = []
        kwds_scrs = TR.extract_phrases(input_text.lower())
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
            word.append(edited_keyword.lower())
            for t in edited_keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)      
        html = output_html(text, word)
        stc.html(html, height=1000)


    if algo == "SGRank":
        word = []
        s, k = SRG.extract_phrases(input_text.lower())
        text = SRG._preprocess(input_text.lower())
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
            word.append(edited_keyword.lower())
            for t in edited_keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)    
        html = output_html(text, word)
        stc.html(html, height=1000)

    
    if algo == "TextRank":
        word = []
        s, k = TXTR.extract_phrases(input_text.lower())
        text = TXTR._preprocess(input_text.lower())
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
            word.append(keyword.lower())
            for t in keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)   
        html = output_html(text, word)
        stc.html(html, height=1000)


    if algo == "sCAKE":
        word = []
        s, k = sC.extract_phrases(input_text.lower())
        text = sC._preprocess(input_text.lower())
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
            word.append(edited_keyword.lower())
            for t in edited_keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)  
        html = output_html(text, word)
        stc.html(html, height=1000)


    if algo == "PositionRank":
        word = []
        kwds_scrs = PR.extract_phrases(input_text.lower())
        text = PR._preprocess(input_text.lower())
        for i, ks in enumerate(kwds_scrs):
            keyword,score = ks
            if 3*i < len(kwds_scrs):     # 上位　1/3　は赤色のマーカー
                color = "#ffcccc"
            elif 3*i < 2*len(kwds_scrs):     # 中位　1/3　は橙色のマーカー
                color = "#ffcc99"
            else:     # 下位　1/3　は黄色のマーカー
                color = "#ffffcc"
            edited_keyword = re.sub(r"\s+", "", keyword)
            word.append(edited_keyword.lower())
            for t in edited_keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)  
        html = output_html(text, word)
        stc.html(html, height=1000)

    if algo == "MultipartiteRank":
        word = []
        kwds_scrs = MR.extract_phrases(input_text.lower())
        text = MR._preprocess(input_text.lower())
        for i, ks in enumerate(kwds_scrs):
            keyword,score = ks
            if 3*i < len(kwds_scrs):     # 上位　1/3　は赤色のマーカー
                color = "#ffcccc"
            elif 3*i < 2*len(kwds_scrs):     # 中位　1/3　は橙色のマーカー
                color = "#ffcc99"
            else:     # 下位　1/3　は黄色のマーカー
                color = "#ffffcc"
            edited_keyword = re.sub(r"\s+", "", keyword)
            word.append(edited_keyword.lower())
            for t in edited_keyword.split():
                text =  re.sub(t, f"<mark style='background:linear-gradient(transparent 50%, {color} 0%)'>" + t.lower() + "</mark>", text)  
        html = output_html(text, word)
        stc.html(html, height=1000)
