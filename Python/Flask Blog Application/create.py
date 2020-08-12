
from application import db
from application.models import Posts, Users
#import the 'Posts' table schem (above) and use the schema to create the table (below)a

db.drop_all()
db.create_all()
