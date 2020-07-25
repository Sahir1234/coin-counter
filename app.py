
import json
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import url_for

VALUES = {"q": 0.25, "d": 0.10, "n": 0.05, "p": 0.01}

app = Flask(__name__)

counts = {}
with open('./counts.json') as f:
    counts = json.load(f)

def update_json(counts):
    with open('./counts.json', 'w') as json_file:
        json_file.seek(0)  # rewind
        json.dump(counts, json_file)
        json_file.truncate()
        
def create_copy_without_history(counts):
    hist = counts["history"]
    del counts["history"]
    new_counts = counts.copy()
    counts["history"] = hist
    return new_counts

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/get')
def get():
    return jsonify(create_copy_without_history(counts))

@app.route('/update/<c>')
def update(c):

    counts[c] += 1
    counts["coins"] += 1
    counts["total"] += VALUES[c]
    counts["history"].append(c)
    
    update_json(counts)
    return jsonify(create_copy_without_history(counts))
    

@app.route('/undo')
def undo():

    if (not len(counts["history"]) == 0):
        c = counts["history"][-1]
        counts["history"].pop()
        counts["coins"] -= 1
        counts[c] -= 1
        counts["total"] -= VALUES[c]
        
    update_json(counts)
    return jsonify(create_copy_without_history(counts))
    

if __name__ == '__main__':
    app.run()
