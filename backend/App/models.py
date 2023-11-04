from sqlalchemy import DateTime, Text
from .exts import db

collect = db.Table(
    'collects',
    db.Column('member_id', db.Integer, db.ForeignKey('tb_members.id'), primary_key=True),  # 注意這裡的表名應與 Members.__tablename__ 相匹配
    db.Column('content_id', db.Integer, db.ForeignKey('tb_content.id'), primary_key=True),
    db.Column('keywords_id', db.Integer, db.ForeignKey('tb_keywords.id'), primary_key=True)  # 注意這裡的表名應與 Keywords.__tablename__ 相匹配
)
class Members(db.Model):
    # 表名
    __tablename__ = "tb_members"
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.Enum("男性", "女性", "其他"))
    age = db.Column(db.Integer, nullable=True)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)


class Content(db.Model):
    __tablename__ = "tb_content"
    id = db.Column(db.Integer, primary_key=True)
    cont = db.Column(Text,nullable=True)
    createtime = db.Column(DateTime,nullable=True)
    users = db.relationship('Members',backref='contents',lazy='dynamic',secondary=collect)

class Keywords(db.Model):
    __tablename__ = "tb_keywords"
    id = db.Column(db.Integer, primary_key=True)
    kw = db.Column(db.String(255))
    members = db.relationship('Members', backref='keywords', lazy='dynamic', secondary=collect)
