import os
from flask import *
from janome.tokenizer import Tokenizer
t = Tokenizer()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def Main():
    print(request.method)
    if request.method == "GET":
        return render_template("index.html")
    else:
        result="不明"
        sentence=request.form['sentence']
        cnt=0
        noun_cnt=0
        for token in t.tokenize(sentence):
            cnt+=1
            if token.part_of_speech.split(',')[0]=="名詞":
                noun_cnt+=1
        
        print(noun_cnt/cnt)
        if noun_cnt/cnt<0.35:#結構適当
            result="小説/物語"
        else:
            result="ニュース記事"
        return render_template("result.html",sentence=sentence,result=result)


if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)