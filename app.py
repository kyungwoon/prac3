from flask import Flask, render_template, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


# 회원가입

# 로그인

# 메인페이지

# 메인 페이지 지역 클릭 시 지역별 카드출력
@app.route('/main', methods=['GET'])
def show_card():
    category_card = list(db.prac.find({}, {'_id': False}))
    return jsonify({'all_card': category_card})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
