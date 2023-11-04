from flask import jsonify, request
from flask_restful import Resource, fields, marshal_with, reqparse
from App.models import *
import os
from ..common import voice_helper


class HelloResource(Resource):
    def get(self):
        return jsonify({"msg": "get請求"})

#     def post(self):
#         # 獲取 JSON 資料
#         data = request.get_json()
#         # 從資料中取得 'name' 和 'age'
#         name = data.get("name")
#         age = data.get("age")
#         print(name, age)
#         return jsonify({"msg": "post請求"})

class Get_textapi(Resource):
    def get(self):
        return jsonify({"msg": "get請求"})

    def post(self):
        # 獲取 JSON 資料
        data = request.get_json()
        # 從資料中取得 'name' 和 'age'
        name = data.get("name")
        age = data.get("age")
        print(name, age)
        return jsonify({"msg": "post請求"})


class Get_returnvoiceapi(Resource):
    def post(self):
        audio_file = request.files.get("audio")
        try:
            if audio_file:
                # 確保目錄存在
                directory = os.path.join("static", "uploads")
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # 儲存檔案
                file_path = os.path.join(directory, audio_file.filename)
                audio_file.save(file_path)
                voice = voice_helper.VoiceToText()
                data = voice.voice_to_text()
                return jsonify({"message": "success", "status": 200, "data": data})
        except Exception as e:
            print(e)
            return jsonify({"message": e,"status": 500,})


# 設定你的 OpenAI API 密鑰
import openai

openai.api_key =""


class Get_openAI(Resource):
    def post(self):
        question = request.json.get("question")

        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=150,
                temperature=0.2,
            )
            print(response)
            data = response["choices"][0]["message"]["content"]
            return jsonify({"message": "success", "status": 200, "data": data.strip()})

        except Exception as e:
            return jsonify({"message": e,"status": 500,})


