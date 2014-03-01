"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb
from google.appengine.ext import db
import datetime


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
	name = db.StringProperty(required=True)
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

if(Department.all().count() == 0):
    cs = Department(prefix="COMP",name="Computer Science")
    cs.put()
    cs124 = Course(department=cs,number="124",name="Object-Oriented Programming and Data Structure", description="""
This course introduces the principles of software design and development using the object-oriented paradigm (OOP) and the Java programming language. Students will learn to use data structures such as lists, trees and hash tables and they will compare the efficiency of these data structures for a particular application. Students will learn to decompose a project using OOP principles. They will work with integrated development environments (IDEs) and version control systems. Students will practice their skills by creating applications in areas such as graphics, games, simulations, and natural language processing. There is a required 1.5 hour laboratory section associated with this course.
""")
    cs124.put()
    cs124_01_start = datetime.time(10,50,0,0)
    cs124_01_end = datetime.time(11,50,0,0)
    cs124_01 = Section(
        course=cs124,number="01",
        year="2014",
        instructor="Shilad Sen",
        days = "MWF",
        start_time=cs124_01_start,
        end_time=cs124_01_end,
        room="Olin-Rice 256",
        available_spots=11,
        total_spots=20
    )
    cs124_01.put()
    cs124_02 = Section(
        course=cs124,number="02",
        year="2014",
        instructor="Shilad Sen",
        days = "MWF",
        start_time = datetime.time(13,10,0,0),
        end_time = datetime.time(14,10,0,0),
        room="Olin-Rice 256",
        available_spots=2,
        total_spots=20
    )
    cs124_02.put()

    cs240 = Course(department=cs,number="240",name="Computer Systems Organization",
description = """
This course familiarizes the student with the internal design and organization of computers. Topics include number systems, internal data representations, logic design, microarchitectures, the functional units of a computer system, memory, processor, and input/output structures, instruction sets and assembly language, addressing techniques, system software, and non-traditional computer architectures.
""")
    cs240.put()
    cs240_01 = Section(
        course=cs240,number="01",
        year="2014",
        instructor="Elizabeth Shoop",
        days = "TR",
        start_time = datetime.time(9,40,0,0),
        end_time = datetime.time(11,10,0,0),
        room="Olin-Rice 245",
        available_spots=10,
        total_spots=24
    )
    cs240_01.put()

    cs325 = Course(department=cs,number="325",name="Compilers, Interpreters, and Programming Languages",description = """
This course will examine the techniques that underlie compiler and interpreter creation, including lexical analysis, parsing, and compiler generators. These tools will serve as a framework for examining programming language design issues across a range of language types (procedural, object-oriented, modern programming languages with an eye to understanding the underlying philosophy of each language, and how it influences and is influenced by the needs of a compiler or interpreter for the language. "Back-end" issues, including intermediate representations, code generation, and optimization will be included as they relate to specific programming languages.
""")
    cs325.put()
    cs325.put()
    cs325_01 = Section(
        course=cs325,number="01",
        year="2014",
        instructor="Elizabeth Shoop",
        days = "MWF",
        start_time = datetime.time(10,50,0,0),
        end_time = datetime.time(11,50,0,0),
        room="Olin-Rice 245",
        available_spots=20,
        total_spots=24
    )
    cs325_01.put()


    econ = Department(prefix="ECON",name="Economics")
    econ.put()
    econ119 = Course(department=econ,number="119",name="Principles of Economics")
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

    cs124instance=RequirementInstance(requirement=math_et_al, section=cs124_01)
    cs124instance.put()
    econ119instance=RequirementInstance(requirement=social_science, section=econ119_01)
    econ119instance.put()

