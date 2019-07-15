from flask import Flask,current_app,request,Request


# app=Flask(__name__)
#
# ctx=app.app_context()
# ctx.push()
# a=current_app
# print(a)
# #b=current_app.config['DEBUG']
# ctx.pop()

class A:
    def __enter__(self):
        a=1
    def __exit__(self, exc_type, exc_val, exc_tb):
        b=2
with A() as obj_a:
    pass