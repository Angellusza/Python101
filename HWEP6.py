class School:
    schoolName = 'Satthasamut' #Attribute
    
    # Constructor
    def __init__(self,subject='Basic Computer'):
        print('ให้แสดงข้อความนี้เมื่อมีการสร้าง Instance')
        self.subject = subject
    
    #Method
    def hello(self):
        print('Wellcome to School')
    
    def teach(self):
        print(f'โรงเรียน เปิดสอนวิชา {self.subject}')
        
class Student(School):
    def __init__(self, fullname,level,scores,subject):
        super().__init__(subject)
        self.fullname = fullname
        self.level = level
        self.scores = scores
        
    def checkGrade(self):
        if self.scores >= 80:
            print(f'วิชา {self.subject} ได้เกรด A')
        elif self.scores >=70:
            print(f'วิชา {self.subject} ได้เกรด B')
        elif self.scores >=60:
            print(f'วิชา {self.subject} ได้เกรด C')
        elif self.scores >=50:
            print(f'วิชา {self.subject} ได้เกรด D')
        else:
            print(f'วิชา {self.subject} ได้เกรด F')
        
        
        
#Instance

School1 = School()
print(f'ชื่อโรงเรียน : {School1.schoolName}')
School1.hello()
School1.teach()

student01 = Student('somchai',6,75,'Math')
print(f'ชื่อโรงเรียน {student01.schoolName}')
print(f'ชื่อนักเรียน {student01.fullname}')
print(f'ระดับชั้นม. {student01.level}')
print(f'คะแนนสอบ {student01.scores}')
student01.checkGrade()
print('====================================================================')
student02 = Student('Peerapat',6,80,'Math')
print(f'ชื่อโรงเรียน {student02.schoolName}')
print(f'ชื่อนักเรียน {student02.fullname}')
print(f'ระดับชั้นม. {student02.level}')
print(f'คะแนนสอบ {student02.scores}')
student02.checkGrade()
print('====================================================================')
student03 = Student('Warayut',6,68,'Math')
print(f'ชื่อโรงเรียน {student03.schoolName}')
print(f'ชื่อนักเรียน {student03.fullname}')
print(f'ระดับชั้นม. {student03.level}')
print(f'คะแนนสอบ {student03.scores}')
student03.checkGrade()
print('====================================================================')
student04 = Student('Mahasarn',4,75,'Math')
print(f'ชื่อโรงเรียน {student04.schoolName}')
print(f'ชื่อนักเรียน {student04.fullname}')
print(f'ระดับชั้นม. {student04.level}')
print(f'คะแนนสอบ {student04.scores}')
student04.checkGrade()
print('====================================================================')
student05 = Student('Bantratai',4,99,'Math')
print(f'ชื่อโรงเรียน {student05.schoolName}')
print(f'ชื่อนักเรียน {student05.fullname}')
print(f'ระดับชั้นม. {student05.level}')
print(f'คะแนนสอบ {student05.scores}')
student05.checkGrade()
print('====================================================================')

        
        
 