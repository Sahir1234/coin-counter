
import json
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import url_for

class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

VALUES = {"q": 25, "d": 10, "n": 5, "p": 1}

app = Flask(__name__)

counts = {}
with open('./counts.json') as f:
    counts = json.load(f)
    
counts["history"] = None

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
    node = Node(c)
    node.next = counts["history"]
    counts["history"] = node
    
    cop = create_copy_without_history(counts)
    update_json(cop)
    
    return jsonify(cop)
    

@app.route('/undo')
def undo():

    if (not counts["history"] is None):
        c = counts["history"].data
        counts["history"] = counts["history"].next
        counts["coins"] -= 1
        counts[c] -= 1
        counts["total"] -= VALUES[c]
        
    cop = create_copy_without_history(counts)
    update_json(cop)
    
    return jsonify(cop)
    

if __name__ == '__main__':
    app.run()
