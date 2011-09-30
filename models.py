import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = db.create_engine('mysql://root:12345@localhost:3306/foobar?charset=utf8')
Session = db.orm.sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Query(object):
    @classmethod
    def objects(cls):
        return session.query(cls)


class Category(Base, Query):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.Unicode(255), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.slug

    @property
    def get_absolute_url(self):
        return '/category/%s' % self.slug


class Post(Base, Query):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), 
                            nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.Unicode(255), nullable=False)
    teaser = db.Column(db.Unicode(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    pub_date = db.Column(db.DateTime(), default=datetime.now())
    is_published = db.Column(db.Boolean(), default=True)
    
    category = db.orm.relationship("Category", 
                                   backref=db.orm.backref('category_set'), 
                                   lazy='joined')
    def __repr__(self):
        return '<Post %r>' % self.slug
    
    @property
    def get_absolute_url(self):
        return '/post/%s' % self.slug