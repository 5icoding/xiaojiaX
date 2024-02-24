from app.extensions import db

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    author = db.Column(db.String(30))
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    createTime = db.Column(db.DateTime)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    blogs = db.relationship('Blog', secondary='blog_category', backref='categories')    

class BlogCategory(db.Model):
    __tablename__ = 'blog_category'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))



class BlogTag(db.Model):
    __tablename__ = 'blog_tag'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    blogs = db.relationship('Blog', secondary='blog_tag', backref='tags')

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.Text)
    createTime = db.Column(db.DateTime)
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    parent = db.relationship('Comment', remote_side=[id])


