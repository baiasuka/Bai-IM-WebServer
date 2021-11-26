from sqlalchemy import func

from models import db


class UserModel(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    email = db.Column(db.VARCHAR, comment='邮箱', nullable=False)
    account = db.Column(db.VARCHAR(32), comment='账号')
    password = db.Column(db.CHAR(32), comment='密码')
    nick = db.Column(db.VARCHAR(32), comment='昵称', default="")
    avatar = db.Column(db.VARCHAR(64), comment='头像地址', default="")
    create_time = db.Column(db.DATETIME, default=func.now())
    last_login_time = db.Column(db.DATETIME, default=func.now())
