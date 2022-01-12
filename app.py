from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('login.html')


# 회원가입
@app.route('/signup')
def sing_up_page():
    return render_template('registe.html')


@app.route('/signup', methods=['POST'])
def sign_up():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']

    doc = {
        'id': id_receive,
        'pw': pw_receive,
        'name': name_receive
    }
    db.signup.insert_one(doc)
    return jsonify({'msg': '회원가입되었습니다.'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.signup.find_one({"id": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


# 로그인
@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    user = db.signup.find_one({'id': id_receive, 'pw': pw_receive})
    if user is None:
        return jsonify({'msg': '아이디나 비밀번호를 확인해주세요.'})
    else:
        return jsonify({'msg': '로그인되었습니다.'})




# 메인페이지
@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/main_page', methods=['GET'])
def show_card():
    category_card = list(db.prac.find({}, {'_id': False}))
    return jsonify({'all_card': category_card})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
