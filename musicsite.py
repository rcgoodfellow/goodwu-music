#!/usr/bin/env python3

from flask import Flask, render_template, request
from searchlib import search


app = Flask(__name__)

@app.route("/")
def start():
    q = request.args.get('q', '')

    result = search(q)

    return render_template('index.html', query=q, searchresults=result)

if __name__ == "__main__":
    app.run()

