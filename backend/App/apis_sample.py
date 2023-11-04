from flask import jsonify
from flask_restful import Resource,fields,marshal_with,reqparse
from .models import *
# 類視圖 : CBV Class Based View
# 視圖函數: FBV Function Based View
# HelloResouse 可以自己命名
class HelloResouse(Resource):
    def get(self):
        return jsonify({'msg':'get請求'})
    
    def post(self):
        return jsonify({'msg':'post請求'})
    
# Flask-Restful
# 字段格式化:定義回給前端的格式
ret_fields = {
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.String,
    # 'like':fields.String(default='ball'),
    # 'like':fields.String(),
    # 'data2':fields.String(attribute='data')
}

class UserRescourse(Resource):
    @marshal_with(ret_fields)
    def get(self):
        return {
            'status':1,
            'msg':'ok',
            'data':'fields.String'
        }
#
user_fields = {
    # 'id':fields.Integer,
    'name':fields.String,
    'age':fields.Integer
}
ret_fields2 = {
    'status':fields.Integer,
    'msg':fields.String,
    # user 對象 Nested 嵌套
    'data':fields.Nested(user_fields),
}
class UserRescourse2(Resource):
    @marshal_with(ret_fields2)
    def get(self):
        user = User.query.first()
        print(user)
        return {
            'status':1,
            'msg':'ok',
            'data':user
        }
    
#---------------------------------------
user_field3 = {
    'name':fields.String,
    'age':fields.Integer
}
ret_fields3 = {
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(user_field3))
}
class UserRescourse3(Resource):
    @marshal_with(ret_fields3)
    def get(self):
        user = User.query.all()
        print(user)
        return {
            'status':1,
            'msg':'ok',
            'data':user
        }
    
#-------------參數解析-----------
parser = reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help='name是必須的參數')
parser.add_argument('age',type=int,action='append') # 可以有多個age
parser.add_argument('key',type=str,location='cookies')

class UserRescourse4(Resource):
    def post(self):
        #獲取參數
        args = parser.parse_args()
        name = args.get('name')
        age = args.get('age')
        key = args.get('key')

        return jsonify({'name':name,'age':age,'key':key})