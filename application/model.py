"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb
from google.appengine.ext import db


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class Department(db.Model):
	department_prefix = db.StringProperty(required=True)
	department_name = db.StringProperty(required=True)

class Course(db.Model):
	department = db.ReferenceProperty(Department,collection_name="courses")
	number = db.StringProperty(required=True)
	#requirements = db.ReferenceProperty(Course,collection_name="required_by")
	description = db.TextProperty()

class Section(db.Model):
	course = db.ReferenceProperty(Course,collection_name="sections")
	number = db.StringProperty(required=True)
	year = db.StringProperty(required=True)
	instructor = db.StringProperty()
	start_time = db.TimeProperty(required=True)
	end_time = db.TimeProperty(required=True)
	room = db.StringProperty()
	available_spots = db.IntegerProperty()
	total_spots = db.IntegerProperty()
	description = db.TextProperty()

class Student(db.Model):
	id = db.IntegerProperty(required=True)
	name = db.StringProperty(required=True)

class Enrollment(db.Model):
	section = db.ReferenceProperty(Section,collection_name="enrollments")
	student = db.ReferenceProperty(Student,collection_name="enrollments")
	isComplete = db.BooleanProperty(required=True)

class Requirement(db.Model):
	name = db.StringProperty()
	description = db.TextProperty()

class RequirementStatus(db.Model):
	requirement = db.ReferenceProperty(Requirement,collection_name="statuses")
	student = db.ReferenceProperty(Student,collection_name="requirements")
	isComplete = db.BooleanProperty(required=True)


