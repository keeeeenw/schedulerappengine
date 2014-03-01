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
	prefix = db.StringProperty(required=True)
	name = db.StringProperty(required=True)

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
	days = db.StringProperty(required=True)
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

class RequirementInstance(db.Model):
	requirement = db.ReferenceProperty(Requirement,collection_name="sections")
	section = db.ReferenceProperty(Section,collection_name="requirements")

class RequirementStatus(db.Model):
	requirement = db.ReferenceProperty(Requirement,collection_name="statuses")
	student = db.ReferenceProperty(Student,collection_name="requirements")
	isComplete = db.BooleanProperty(required=True)


cs = Department(prefix="COMP",name="Computer Science")
cs.put()
cs124 = Course(department=cs,number="124",description="Object-Oriented Programming
	and Data Structure")
cs124.put()
cs124_start = datetime.time(10,50,0,0)
cs124_end = datetime.time(11,50,0,0)
cs124_01 = Section(
	course=cs124,number="01",
	year="2014",
	instructor="Shilad Sen",
	days = "MWF",
	start_time=cs124_start,
	end_time=cs124_end,
	room="Olin-Rice 256",
	available_spots=11,
	total_spots=20
)
cs124_01.put()

econ = Department(prefix="ECON",name="Economics")
econ.put()
econ119 = Course(department=econ,number="119",description="Principles of Economics")
econ119.put()
econ119_start = datetime.time(9,40,0,0)
econ119_end = datetime.time(11,10,0,0)
econ119_01 = Section(
	course=econ119,number="01",
	year="2014",
	instructor = "Paul Rice",
	days = "TR",
	start_time=econ119_start,
	end_time=econ119_end,
	room = "Olin-Rice 350",
	available_spots=2,
	total_spots=30
)
econ119_01.put()

social_science = Requirement(name="Social Sciences",description="You must take two social science courses.")
social_science.put()
math_et_al = Requirement(name="Mathematics and Natural Sciences", description="You must take two courses that fulfill the Mathematics and Natural Sciences distribution requirement")
math_et_al.put()

cs124instance=RequirementInstance(requirement=math_et_al, section=comp124_01)
cs124instance.put()
econ119instance=RequirementInstance(requirement=social_science, section=econ119_01)
econ119instance.put()

