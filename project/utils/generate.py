from faker import Faker
import random
import pickle
f = Faker(locale = "zh_CN")

# 6个班级
# 3个系部
# 职称 【讲师，教授，副教授】中的其中一个
bots = ["讲师","教授","副教授"]
depart = ["市营","公管","计算机科学与技术", "信息管理与系统设计"]
teacherset = []
typeset = []
classset = []
def generate_student(n):
    global f, bots,depart,teacherset,typeset,classset
    dataset = []
    for i in range(n):
        name = f.name()
        no = "".join([str(random.randint(0, 9)) for i in range(10)])
        # password is static
        password = "123456"
        
        email = f.email()
        mclass = random.randint(0, len(classset)-1)
        dataset.append((no, name, password, email, mclass))
    return dataset
        
def generate_teacher(n):
    global f, bots,depart,teacherset,classset
    
    dataset = []
    for i in range(n):
        name = f.name()
        no = "".join([str(random.randint(0, 8)) for i in range(5)])
        teacherset.append(no)
        # password is static
        password = "123456"
        email = f.email()
        botany = bots[random.randint(0,2)]
        department = depart[random.randint(0,3)]
        dataset.append((no, name, botany, password, email,department))
    return dataset
def generate_depart():
    global f, bots,depart
    dataset = []
    for i in range(4):
        dno = i
        dname = depart[i]
        dataset.append((dno, dname))
    return dataset

def generate_course(n):
    global f, bots,depart,teacherset
    dataset = []
    for i in range(n):
        name = f.pystr()
        tno = random.choice(teacherset)
        dataset.append((name, tno))
    return dataset
def generate_source(n):
    global source, f, bots, teacherset,typeset
    s = set()
    dataset = []
    for i in range(n):
        s.add(f.file_extension())
    s = list(s)
    typeset = s[:]
    return typeset


def generate_file(n):
    global f, bots,depart,teacherset,typeset
    dataset = []
    for i in range(n):
        name = f.file_name().split(".")[0] + "." + random.choice(typeset) 
        descri = f.paragraph()
        time = f.past_datetime()
        path = f.file_path()
        title = f.word() + f.word()
        tno = random.choice(teacherset)
        dataset.append((name, descri, time, path, title, tno))
    return dataset

def generate_class(n):
    global f, bots,depart,teacherset,typeset, classset
    dataset = []
    for i in range(n):
        cname = random.randint(0,6) + 1
        grade = random.choice([2019, 2018, 2017, 2016])
        dep = depart[random.randint(0,len(depart)-1)]
        dataset.append((cname, grade, dep))
    classset = dataset[:]
    return dataset
    
def write_data_to_pickle(dataset, fname = "data.txt"): 
    with open(fname, "wb") as f:
        pickle.dump(dataset, f)

def read_data_from_pickle(fname):
    with open(fname, "rb") as f:
        dataset = pickle.load(f)
    print(dataset.keys())
    return dataset
def main_gen(teacher_num = 10, student_num = 100, file_num = 100, course_num = 50, class_num = 30):
    global f, bots,depart,teacherset,classset
    dataset = {}
    dataset["class"] = generate_class(class_num)
    dataset["source"] = generate_source(10)
    dataset["teacher"] = generate_teacher(teacher_num)
    dataset["course"] = generate_course(course_num)
    dataset["file"] = generate_file(file_num)
    dataset["student"] = generate_student(student_num)
    write_data_to_pickle(dataset, "dataset.txt")

