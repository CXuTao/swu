from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
import time

# Create your models here.
#1、教师
class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(isDelete=False)
    def createTeacher(self, tno, tname, botany, password, email, department, isDelete=False):
        teacher = self.model()
        #print(type(grade))
        teacher.tno = tno
        teacher.tname = tname
        teacher.botany = botany
        teacher.password = password
        teacher.email = email
        teacher.department = department
        teacher.isDelete = isDelete
        return teacher

class Teacher(models.Model):
    teacherManage = TeacherManager()
    tno = models.CharField(max_length=10, unique=True)
    tname = models.CharField(max_length=16)
    botany = models.CharField(max_length=24)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    #所在系部
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    class Meta:
        db_table = "teacher"

#2、系部
class DepartmentManager(models.Manager):
    def get_queryset(self):
        return super(DepartmentManager, self).get_queryset().filter(isDelete=False)
    def createDepartment(self, dno, dname, isDelete=False):
        department = self.model()
        #print(type(grade))
        department.dno = dno
        department.dname = dname
        department.isDelete = isDelete
        return department

class Department(models.Model):
    departmentManage = DepartmentManager()
    dno = models.CharField(max_length=18, unique=True)
    dname = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "department"

#3、课程
class CourseManager(models.Manager):
    def get_queryset(self):
        return super(CourseManager, self).get_queryset().filter(isDelete=False)
    def createCourse(self, no, name, tno, isDelete=False):
        course = self.model()
        #print(type(grade))
        course.no = no
        course.name = name
        course.tno = tno
        course.isDelete = isDelete
        return course

class Course(models.Model):
    courseManager = CourseManager()
    no = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=39)
    isDelete = models.BooleanField(default=False)
    tno = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    class Meta:
        db_table = "course"

#4、资源表
class SourceManager(models.Manager):
    def get_queryset(self):
        return super(SourceManager, self).get_queryset().filter(isDelete=False)
    def createSource(self, sno, sname, opersonNum, npersonNum, tpersonNum, ano, isDelete=False):
        stu = self.model()
        #print(type(grade))
        stu.sno = sno
        stu.sname = sname
        stu.isDelete = isDelete
        return stu

class Source(models.Model):
    sourceManager = SourceManager()
    sno = models.CharField(max_length=10, unique=True)
    sname = models.CharField(max_length=21)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "source"

#5、资源具体内容
class FileManager(models.Manager):
    def get_queryset(self):
        return super(FileManager, self).get_queryset().filter(isDelete=False)
    def createFile(self, fno, describe, url, title, tno, sno, vtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), isDelete=False):
        stu = self.model()
        #print(type(grade))
        stu.fno = fno
        stu.describe = describe
        stu.time = vtime
        stu.url = url
        stu.title = title
        stu.tno = tno
        stu.sno = sno
        stu.isDelete = isDelete
        return stu

class File(models.Model):
    fileManager = FileManager()
    fno = models.CharField(max_length=10, unique=True)
    describe = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
    title = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    tno = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    sno = models.ForeignKey('Source', on_delete=models.CASCADE)
    class Meta:
        db_table = "file"

#6、学生表
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)
    def createStudent(self, sno, sname, password, email, mclass, isDelete=False):
        teacher = self.model()
        #print(type(grade))
        teacher.sno = sno
        teacher.sname = sname
        teacher.password = password
        teacher.email = email
        teacher.mclass = mclass
        teacher.isDelete = isDelete
        return teacher

class Student(models.Model):
    studentManager = StudentManager()
    sno = models.CharField(max_length=15, unique=True)
    sname = models.CharField(max_length=18)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    #所在系部
    mclass = models.ForeignKey('Mclass', on_delete=models.CASCADE)
    class Meta:
        db_table = "student"

#7、班级
class MclassManager(models.Manager):
    def get_queryset(self):
        return super(MclassManager, self).get_queryset().filter(isDelete=False)
    def createMclass(self, cno, cname, grade, department, isDelete=False):
        teacher = self.model()
        #print(type(grade))
        teacher.cno = cno
        teacher.cname = cname
        teacher.grade = grade
        teacher.department = department
        teacher.isDelete = isDelete
        return teacher

class Mclass(models.Model):
    mclassManager = MclassManager()
    cno = models.CharField(max_length=15, unique=True)
    cname = models.IntegerField()
    #年级
    grade = models.CharField(max_length=4)
    isDelete = models.BooleanField(default=False)
    #所在系部
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    con = models.ManyToManyField(Course)
    class Meta:
        db_table = "mclass"

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Source)
admin.site.register(File)
admin.site.register(Student)
admin.site.register(Mclass)