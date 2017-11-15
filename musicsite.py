#!/usr/bin/env python3

from flask import Flask, render_template, request
from searchlib import search, index, delete
from common import Work
import json

app = Flask(__name__)



@app.route("/")
def start():
    q = request.args.get('q', '')

    result = search(q)

    return render_template('index.html', query=q, searchresults=result)

@app.route("/new")
def new():
    return render_template("edit.html", work=Work())

@app.route("/edit", methods=['GET'])
def edit_get():

    id_ = request.args.get('id')
    res = search(id_)
    if len(res) == 0:
        return "not found"

    return render_template("edit.html", work=res[0])

@app.route("/delete", methods=['GET'])
def delme():

    id_ = request.args.get('id')
    res = search(id_)
    if len(res) == 0:
        return "not found"

    delete(id_)

    return "ok"
            

@app.route("/edit", methods=['POST'])
def edit():

    w = Work()

    ## Work ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
    w.composer = request.form['composer']
    w.title = request.form['title']
    w.catalogue = request.form['catalogue']
    w.recording_date = request.form['recording-date']
    w.tags = request.form['tags']
    w.venue = request.form['venue']
    w.id = request.form['_id']

    ## Musicians ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
    musicians = []
    instruments = []
    
    for field, value in request.form.items():
        if value == '':
            continue

        if field.startswith('musician'):
            musicians.append((field,value))

        if field.startswith('instrument'):
            instruments.append((field,value))
        
        print("%s - %s"%(field,value))

    musicians.sort()
    instruments.sort()
    combined = zip(musicians, instruments)
    w.musicians = list(map(lambda x: ((x[0][1], x[1][1])), combined))

    if 'addMusician' in request.form:
        w.musicians.append(('',''))
        
    ## Movements ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
    movements = []

    for field, value in request.form.items():
        if value == '':
            continue

        if field.startswith('movement_name'):
            movements.append((field,value))


    for field, value in request.files.items():

        if field.startswith('movement_file'):
            i = int(field.split('-')[1])
            print(value)
            w.files[i] = value.filename
            saveFile(value, w.id, i)
    
    movements.sort()
    w.movements = list(map(lambda x: x[1], movements))
    
    if 'addMovement' in request.form:
        w.movements.append('')

    index(w)

    print("FORM")
    print(request.form)

    print("FILES")
    print(request.files)

    return render_template("edit.html", work=w)

def saveFile(htmlfile, id_, index):

    htmlfile.save('/var/gwm/%s_%s.flac'%(id_, index))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

