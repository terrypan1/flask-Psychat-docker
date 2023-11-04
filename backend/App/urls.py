#urls.py 路由文件

from .exts import api
from App.apis import chatbot,register_add,login
# 路由
api.add_resource(chatbot.HelloResource,'/hello/')
api.add_resource(chatbot.Get_returnvoiceapi,'/voiceapi/')
api.add_resource(chatbot.Get_openAI,'/openai/')
api.add_resource(register_add.Register_add,'/register_add/')
api.add_resource(login.Login,'/login/')