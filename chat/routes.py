from flask import Flask, render_template, request, session, redirect, url_for, flash
from chat import app
from chat.models import *
from chat.models import *
from chat.forms import *
from sqlalchemy import and_

class ans_id:
    id = 0

a_id = ans_id()


@app.route("/")
def home(id = 1):
    a_id.id = 1
    ans = db.session.query(Ans).filter(Ans.id == "1")
    sub = db.session.query(Sub_ques).filter(Sub_ques.perv_ans_id == 1)
    return render_template("index.html" , init_ans = ans , sub = sub)

@app.route("/get")
def get_bot_response():
    response = ""
    flag = 1
    userText = request.args.get('msg')
    sub = db.session.query(Sub_ques).filter(and_(Sub_ques.perv_ans_id == a_id.id , Sub_ques.sub_ques_id == int(userText))).first()
    a_id.id = sub.next_ans_id
    ans = db.session.query(Ans).filter(Ans.id == sub.next_ans_id).first()
    sub = db.session.query(Sub_ques).filter(Sub_ques.perv_ans_id == a_id.id).all()
    response += ans.ans_desc
    response += "<br>"
    for ques in sub:
        response += "<b>" + str(flag) + " " + ques.sub_ques_desc + "<br>" + "</b>"
        flag += 1
        print(response)
    return response

@app.route("/admin" , methods = ["GET" ,"POST"])
def admin_login():
    form = AdminLogin()
    if form.validate_on_submit():
        if form.email.data == "admin@gchat.com" and form.password.data == "admin":
            return redirect(url_for('adminrights'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
   
    return render_template("admin.html" , form = form)


@app.route("/adminrights")
def adminrights():
    return render_template("adminright.html")


@app.route("/registerques" , methods = ["GET" ,"POST"])
def addques():
    form = RegisterQues()
    if form.validate_on_submit():
        sub = Sub_ques(
        sub_ques_id = int(form.sub_ques_id.data),
        perv_ans_id = int(form.perv_ans_id.data),
        next_ans_id = int(form.next_ans_id.data),
        sub_ques_desc = str(form.sub_ques_desc.data))
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('adminrights'))
    return render_template("registerques.html" , form = form)

@app.route("/registerans" ,methods = ["GET" ,"POST"])
def addans():
    form = RegisterAns()
    if form.validate_on_submit():
        ans = Ans(
        ans_desc = form.ans_desc.data)
        db.session.add(ans)
        db.session.commit()  
        return redirect(url_for('adminrights'))
    return render_template("registerans.html" , form = form)