from flask import Flask,render_template
import requests
from flask import request as req


app= Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html",result=output)
@app.route("/summarize",method=["GET","POST"])
def summarize():
    if req.method=="POST":  
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        API_TOKEN = "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"
        headers = {"Authorization": "Bearer "+API_TOKEN}
        data=req.form["data"]
    

if __name__=="__main__":
    app.run(debug=True)
