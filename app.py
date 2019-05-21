import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'wildlife_globe'
app.config["MONGO_URI"] = 'mongodb+srv://User63:admin3Lobe90@myfirstcluster-maf2n.mongodb.net/wildlife_globe?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_spotlist')
def get_spotlist():
    return render_template("spotlist.html", 
                          spotlist=mongo.db.spotlist.find())
                          
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)