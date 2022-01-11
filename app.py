from json import dumps

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

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
@app.route('/main/category', methods=['GET'])
def show_card(): # db에서 키워드로 db리스트 가져오기
    keyword = request.args.get('category')
    category_card = list(db.chabak.find({'type': {'$regex': keyword}})) # $regex -> 포함된 문자열을 리스트 가져오기
    return jsonify({'title_card': dumps(category_card)}) #dump() -> JSON문자열로 변환, id값이 $oid안에 있어서?

# @app.route('/detail')
# def title():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         userid = (payload["id"])
#
#         id_address = request.args.get('id') #url에서 파라미터값 가져오기
#         recipeData = db.recipe.find_one({'_id':ObjectId(id_address)}) #mongodb의 ID값 가져올때 ObjectID
#         user_info = db.users.find_one({'userid': userid})
#         return render_template("detail.html", user = user_info, recipe=recipeData)
#     except jwt.ExpiredSignatureError:
#         return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
#     except jwt.exceptions.DecodeError:
#         return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# //////////////////////////댓글/////////////////////////////
# @app.route('/posting', methods=['POST'])
# def posting():
#     # 클라이언트로부터 'comment_give'받아서 'comment_receive'에 넣어주기
#     comment_receive = request.form["comment_give"]
#     print(comment_receive, "댓글")
#     # 클라이언트로부터 'date_give'받아서 'date_receive'에 넣어주기
#     date_receive = request.form["date_give"]
#     # 'date_receive'를 문자열로 변환하기
#     date_receive = repr(date_receive)
#     print(date_receive, "날짜")
#     # 클라이언트로부터 'title_give' 받아서 'title_give'에 넣기
#     title_give = request.form['title_give']
#     print(title_give, "타이틀")
#     # 쿠키에서 토큰받기
#     token_receive = request.cookies.get('mytoken')
#     try:
#         # 받은 'token'에서 'id,exp'이 있는 payload 받아오기
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # payload['id']에서 userid 받아오기
#         userid = (payload["id"])
#         # db의 user에서 userid 받아와서 user_info에 넣기
#         user_info = db.users.find_one({"userid": userid})
#         print(user_info,"유저인포")
#         # user_name, comment, date, title 들을 posts라는 db에 저장
#         doc = {
#             'user_name':user_info['username'],
#             "comment": comment_receive,
#             "date": date_receive,
#             'title': title_give
#         }
#         db.posts.insert_one(doc)
#         return jsonify({"result": "success", 'msg': '포스팅 성공'})
#     # jwt에서 exp가 만료되었을 때, "show_menu"로 보내기
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("show_menu"))
#
# # 댓글 클라이언트로 보내주기 / //////////////////////
# @app.route("/get_posts", methods=['POST'])
# def get_posts():
#     # 클라이언트에서 'title_give'받기
#     title_give = request.form['title_give']
#     print(title_give, "두번째 타이틀")
#     # posts에 저장된 'user_name, comment, date, title' 중에서 'title'이 받은 'title_give'와 일치하는 db들을 list로 posts에 넣기
#     posts = list(db.posts.find({'title':title_give}, {'_id': False}))
#     print(posts,"포스트리스트")
#     # posts를 클라이언트에 주기
#     return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "posts": posts})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)