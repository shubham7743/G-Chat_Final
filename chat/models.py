from chat import db


class Ans(db.Model):
    __tablename__ = 'ans'
    id = db.Column(db.Integer , primary_key = True, autoincrement=True)
    ans_desc = db.Column(db.String(10000) , nullable = False)

    def __init__(self, ans_desc):
        self.ans_desc = ans_desc

    def __ref__(self):
        return f"chatbot_ans('{self.ans_id}' , '{self.ans_desc}')"
        


class Sub_ques(db.Model):
    __tablename__ = 'sub_ques'
    id = db.Column(db.Integer , primary_key = True, autoincrement=True)
    sub_ques_id = db.Column(db.Integer ,nullable = False)
    perv_ans_id = db.Column(db.Integer , db.ForeignKey(Ans.id), nullable = False)
    next_ans_id = db.Column(db.Integer , db.ForeignKey(Ans.id), nullable = False)
    sub_ques_desc = db.Column(db.String(1000) , nullable = False)
    
    def __init__(self,sub_ques_id, perv_ans_id, next_ans_id,sub_ques_desc):
        self.sub_ques_id = sub_ques_id
        self.perv_ans_id = perv_ans_id
        self.next_ans_id = next_ans_id
        self.sub_ques_desc = sub_ques_desc

    def __ref__(self):
        return f"chatbot_sub_ques('{self.sub_ques_id}' , '{self.perv_ans_id}' , '{self.next_ans_id}' , '{self.sub_ques_desc}')"

