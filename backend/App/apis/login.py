from flask import jsonify, request
from flask_restful import Resource, fields, marshal_with, reqparse
from App.models import *
from sqlalchemy import text

class Login(Resource):
    def post(self):
        req = request.get_json()
        account = req.get('account')
        password = req.get('password')
        _sql = text('select * from tb_members where account = :account and password = :password')
        user = db.session.execute(_sql, {"account":account, "password":password}).fetchone() # 單查詢
        if user:
            return jsonify({"message": "登陸成功", "status": 200,"success":"true"})
        else:
            return jsonify({"message": "登陸失敗", "status": 401,"success":"true"})