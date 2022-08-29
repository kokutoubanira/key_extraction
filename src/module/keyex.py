import re
import textacy
from textacy.extract.keyterms import yake, sgrank, textrank, scake
# pip install git+https://github.com/boudinfl/pke.git
from pke.unsupervised import MultipartiteRank, PositionRank, TopicRank
import neologdn
from statistics import StatisticsError

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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)

        return x

    def extract_phrases(self, data) :
        doc = textacy.make_spacy_doc(self._preprocess(data), lang=self.ja)
        try:
            keywords_with_score = [
                (kps, score) for kps, score in yake(doc, normalize="lemma", topn=9)
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

class SGRank():
    def __init__(self):
        self.ja = textacy.load_spacy_lang("ja_ginza_electra")
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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)

        return x


    def extract_phrases(self, data):
        doc = textacy.make_spacy_doc(self._preprocess(data), lang=self.ja)
        keywords_with_score = [
            (kps, score) for kps, score in sgrank(doc, normalize="lemma", topn=9)
        ]

        keywords = [keywords_with_score[i][0] for i in range(len(keywords_with_score))]
        scores = [keywords_with_score[i][1] for i in range(len(keywords_with_score))]

        return scores, keywords


class TextRank():
    def __init__(self):
        super().__init__()

        self.ja = textacy.load_spacy_lang("ja_ginza_electra")
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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)

        return x
    def extract_phrases(self, data):
        doc = textacy.make_spacy_doc(self._preprocess(data), lang=self.ja)
        keywords_with_score = [
            (kps, score) for kps, score in textrank(doc, normalize="lemma", topn=9)
        ]

        keywords = [keywords_with_score[i][0] for i in range(len(keywords_with_score))]
        scores = [keywords_with_score[i][1] for i in range(len(keywords_with_score))]

        return scores, keywords

class sCAKE():
    def __init__(self):
        super().__init__()

        self.ja = textacy.load_spacy_lang("ja_ginza_electra")
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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)

        return x
    def extract_phrases(self, data):
        doc = textacy.make_spacy_doc(self._preprocess(data), lang=self.ja)
        keywords_with_score = [
            (kps, score) for kps, score in scake(doc, normalize="lemma", topn=9)
        ]

        keywords = [keywords_with_score[i][0] for i in range(len(keywords_with_score))]
        scores = [keywords_with_score[i][1] for i in range(len(keywords_with_score))]

        return scores, keywords

class TopicRank_():
    def __init__(self):
        self.extractor = TopicRank()
    
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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)
        return x

    def extract_phrases(self, data):
        self.extractor.load_document(
            input=self._preprocess(data), language="ja", normalization=None
        )
        self.extractor.candidate_selection(pos={"NOUN", "PROPN", "ADJ", "NUM"})
        self.extractor.candidate_weighting()

        kwds_scrs = self.extractor.get_n_best(n=9)

        if len(kwds_scrs) > 0:
            return kwds_scrs
        else:
            return kwds_scrs

class PositionRank_():
    def __init__(self):
        self.extractor = PositionRank()

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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)
        return x

    def extract_phrases(self, data):
        self.extractor.load_document(
            input=self._preprocess(data), language="ja", normalization=None
        )
        self.extractor.candidate_selection()
        self.extractor.candidate_weighting()
        kwds_scrs = self.extractor.get_n_best(n=9)

        if len(kwds_scrs) > 0:
            return kwds_scrs
        else:
            return kwds_scrs

class MultipartiteRank_():
    def __init__(self):
        self.extractor = MultipartiteRank()
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
        x = re.sub(r"・", ", ", x)
        x = re.sub(r"[\(\)「」【】]", "", x)
        return x
    def extract_phrases(self, data):
        self.extractor.load_document(
            input=self._preprocess(data), language="ja", normalization=None
        )
        self.extractor.candidate_selection(pos={"NOUN", "PROPN", "ADJ", "NUM"})
        self.extractor.candidate_weighting()

        kwds_scrs = self.extractor.get_n_best(n=9)

        if len(kwds_scrs) > 0:
            return kwds_scrs
        else:
            return kwds_scrs

def output_html(text, word):
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
        <tr>
        <li><mark style='background:linear-gradient(transparent 50%, #ffcccc 0%)'>上位1/3は赤色</mark></li>
        <li><mark style='background:linear-gradient(transparent 50%, #ffcc99 0%)'>中位1/3は橙色</mark></li>
        <li><mark style='background:linear-gradient(transparent 50%, #ffffcc 0%)'>下位1/3は黄色</mark></li>
        </tr>
    """

    html += """
        <br>
        最大9単語抽出
        <br>
        """

    for i, w in enumerate(word):
        html += "<li>" +  str(i + 1) + ":" + w + "</li>"

    html += """
        </body>
        </html>
        """
    return html