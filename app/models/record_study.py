from app.extensions import db

class RecordCurrentStudy(db.Model):
    __tablename__ = 'record_currentstudy'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    learnerId = db.Column(db.Integer)
    courseId = db.Column(db.Integer)
    unitId = db.Column(db.Integer)
    number = db.Column(db.Integer)

class StudyRecordOneLevel(db.Model):
    __tablename__ = 'study_record_one_level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    keyNumber = db.Column(db.Integer)
    codingNumber = db.Column(db.Integer)
    readNumber = db.Column(db.Integer)

class LevelOneStudyCodingRecord(db.Model):
    __tablename__ = 'level_one_study_coding_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    level = db.Column(db.Integer)
    unitId = db.Column(db.Integer)
    codeSaveURL = db.Column(db.String(50))
    createTime = db.Column(db.DateTime)

class LevelOneStudyReadRecord(db.Model):
    __tablename__ = 'level_one_study_read_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    level = db.Column(db.Integer)
    unitId = db.Column(db.Integer)
    createTime = db.Column(db.DateTime)

class LevelOneStudyKeyRecord(db.Model):
    __tablename__ = 'level_one_study_key_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    level = db.Column(db.Integer)
    createTime = db.Column(db.DateTime)

class LevelOneStudyCodingActionRecord(db.Model):
    __tablename__ = 'level_one_study_coding_action_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    actionType = db.Column(db.Integer)
    createTime = db.Column(db.DateTime)


class StudyRecordTwoLevel(db.Model):
    __tablename__ = 'study_record_two_level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    
    