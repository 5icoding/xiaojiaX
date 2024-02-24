from app.extensions import db

class StudyPageActions(db.Model):
    __tablename__ = 'study_page_actions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actionTitle = db.Column(db.String(50))
    pageTitle = db.Column(db.String(50))
    createTime = db.Column(db.DateTime)