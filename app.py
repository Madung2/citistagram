from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.3puso.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
   return render_template('index.html')

@app.route("/insta_comment", methods=["POST"])
def insta_comment_post():

    comment_receive = request.form['comment_give']

    doc = {'comment':comment_receive}
    db.insta_comment.insert_one(doc)
    return jsonify({'msg':'소중한 댓글 감사합니다'})


@app.route("/insta_comment", methods=["GET"])
def insta_comment_get():
    all_comment = list(db.insta_comment.find({}, {'_id': False}))
    return jsonify({'comments':all_comment})

####################두번째 코멘트창########################################
@app.route("/insta_comment2", methods=["POST"])
def insta_comment_post2():

    comment_receive = request.form['comment_give']

    doc = {'comment':comment_receive}
    db.insta_comment2.insert_one(doc)
    return jsonify({'msg':'소중한 댓글 감사합니다'})


@app.route("/insta_comment2", methods=["GET"])
def insta_comment_get2():
    all_comment = list(db.insta_comment2.find({}, {'_id': False}))
    return jsonify({'comments':all_comment})

####################세번째 코멘트창########################################
@app.route("/insta_comment3", methods=["POST"])
def insta_comment_post3():

    comment_receive = request.form['comment_give']

    doc = {'comment':comment_receive}
    db.insta_comment3.insert_one(doc)
    return jsonify({'msg':'소중한 댓글 감사합니다'})


@app.route("/insta_comment3", methods=["GET"])
def insta_comment_get3():
    all_comment = list(db.insta_comment3.find({}, {'_id': False}))
    return jsonify({'comments':all_comment})









if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

