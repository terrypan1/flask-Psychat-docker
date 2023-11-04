from flask import jsonify, request
from flask_restful import Resource, fields, marshal_with, reqparse
from App.models import *
from sqlalchemy import text

class Register_add(Resource):
    def post(self):
        req = request.get_json()
        account = req.get("account")
        password = req.get("password")
        gender = req.get("gender")
        age = req.get("age")
        phone_number = req.get("phone_number")
        print(account,password,gender,age,phone_number)
        _sql = text("insert into tb_members(account,password,gender,age,phone_number) values (:account,:password,:gender,:age,:phone_number)")
        db.session.execute(_sql, {'account': account, 'password': password,'gender': gender,'age': age,'phone_number': phone_number})
        db.session.commit()
        return jsonify({"message": "註冊成功", "status": 200,"success":"true"})
    
class Hello(Resource):
    def get(self):
        return jsonify({"msg": "get請求"})
