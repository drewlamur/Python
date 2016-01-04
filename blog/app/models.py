import datetime, pdb, re
from app import db

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()

entry_tags = db.Table('entry_tags', \
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')))

class Entry(db.Model):
    STATUS_PUBLIC = 0
    STATUS_DRAFT = 1

    id    = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug  = db.Column(db.String(100), unique=True)
    body  = db.Column(db.Text)
    tags  = db.relationship('Tag', secondary=entry_tags, \
        backref=db.backref('entries', lazy='dynamic'))
    status = db.Column(db.SmallInteger, default=STATUS_PUBLIC)
    created_timestamp  = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_timestamp = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Entry %s>' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64), unique=True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag %s>' % self.name

## ==> usage - working with the entry db model

# (blog)$ python scripts/create_db.py 
# (blog)$ ls
# __init__.py app.pyc     config.py   main.py     model.py    models.pyc  views.py
# app.py      blog.db     config.pyc  main.pyc    models.py   scripts     views.pyc

# In [4]: Entry
# Out[4]: models.Entry

# In [5]: entry1 = Entry(title='First entry', body='This is the body of my first entry.')

# In [6]: db.session.add(entry1)

# In [7]: entry1.id is None
# Out[7]: True

# In [8]: db.session.commit()

# In [9]: entry1.id
# Out[9]: 1

# In [10]: entry1.title
# Out[10]: u'First entry'

# In [11]: entry1.body
# Out[11]: u'This is the body of my first entry.'

# In [12]: entry1.slug
# Out[12]: u'first-entry'

# In [13]: entry1.created_timestamp
# Out[13]: datetime.datetime(2016, 1, 2, 15, 31, 58, 464826)

# In [14]: entry2 = Entry(title='Second entry', body='This is the body of the second entry.')

# In [15]: db.session.add(entry2)

# In [16]: entry2.id is None
# Out[16]: True

# In [17]: db.session.commit()

# In [18]: entry2.id
# Out[18]: 2

# In [19]: entry2.title
# Out[19]: u'Second entry'

# In [20]: entry2.body
# Out[20]: u'This is the body of the second entry.'

# In [21]: entry2.slug
# Out[21]: u'second-entry'

# In [22]: entry2.created_timestamp
# Out[22]: datetime.datetime(2016, 1, 2, 15, 34, 23, 270688)

# In [23]: entry2 = Entry.query.get(2)

# In [24]: entry2.body = 'This is the second entry with some edits.'

# In [25]: db.session.commit()

# In [26]: entry2.id
# Out[26]: 2

# In [27]: entry2.title
# Out[27]: u'Second entry'

# In [28]: entry2.body
# Out[28]: u'This is the second entry with some edits.'

# In [29]: entry2.created_timestamp
# Out[29]: datetime.datetime(2016, 1, 2, 15, 34, 23, 270688)

# In [30]: entry2.modified_timestamp
# Out[30]: datetime.datetime(2016, 1, 2, 15, 36, 35, 185792)

# In [31]: entry3 = Entry(title='Third entry', body='This is the body of the third entry.')

# In [32]: db.session.add(entry3)

# In [33]: db.session.commit()

# In [34]: entry3.id
# Out[34]: 3

# In [35]: entry3.title
# Out[35]: u'Third entry'

# In [36]: entry3.body
# Out[36]: u'This is the body of the third entry.'

# In [37]: entry3.slug
# Out[37]: u'third-entry'

# In [38]: entry3.created_timestamp
# Out[38]: datetime.datetime(2016, 1, 2, 15, 38, 17, 846674)

# In [39]: entries = Entry.query.all()

# In [40]: entries
# Out[40]: [<Entry: First entry>, <Entry: Second entry>, <Entry: Third entry>]

# In [41]: Entry.query.order_by(Entry.title.asc()).all()
# Out[41]: [<Entry: First entry>, <Entry: Second entry>, <Entry: Third entry>]

# In [42]: db.session.delete(entry3)

# In [43]: db.session.commit()

# In [44]: Entry.query.order_by(Entry.title.asc()).all()
# Out[44]: [<Entry: First entry>, <Entry: Second entry>]

# In [45]: oldest_to_newest = Entry.query.order_by(Entry.modified_timestamp.desc()).all()

# In [46]: oldest_to_newest
# Out[46]: [<Entry: Second entry>, <Entry: First entry>]

# In [47]: Entry.query.filter(Entry.title == 'First entry').all()
# Out[47]: [<Entry: First entry>]

## ==> usage - working with the entry db model with tags

# In [1]: from models import *

# In [2]: db
# Out[2]: <SQLAlchemy engine='sqlite:////Users/andywallace/python_coding_projects/blog/app/blog.db'>

# In [3]: entry1 = Entry(title='python entry',body='the body python.')

# In [4]: db.session.add(entry1)

# In [5]: db.session.commit()

# In [6]: python = Tag(name='python')

# In [7]: flask = Tag(name='flask')

# In [8]: entry1.tags = [python,flask]

# In [9]: entry1
# Out[9]: <Entry python entry>

# In [10]: entry1.id
# Out[10]: 1

# In [11]: entry1.title
# Out[11]: u'python entry'

# In [12]: entry1.body
# Out[12]: u'the body python.'

# In [13]: entry1.created_timestamp
# Out[13]: datetime.datetime(2016, 1, 3, 19, 36, 3, 240984)

# In [14]: entry1.tags
# Out[14]: [<Tag python>, <Tag flask>]

# In [15]: puppies = Tag(name='puppies')

# In [16]: entry1.tags.append(puppies)

# In [17]: entry1.tags
# Out[17]: [<Tag python>, <Tag flask>, <Tag puppies>]

# In [18]: entry1.tags.remove(puppies)

# In [19]: entry1.tags
# Out[19]: [<Tag python>, <Tag flask>]

# In [20]: db.session.commit()

# In [21]: entry1.tags
# Out[21]: [<Tag python>, <Tag flask>]