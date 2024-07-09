import os

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self,line):
        self.line = line
        self.message = f'Bad line detected in file'
        super().__init__(self.message)


class FileEmpty(StudentsDataException):
    def __init__(self,file):
        self.file = file
        self.message = f'{file} exists but is empty. No content'
        super().__init__(self.message)

def aggregate_marks(data):
    marks = {}
    for line in data:
        parts = line.strip().split()
        if len(parts)!=3:
            raise BadLine(line)
        name, points = ' '.join(parts[:2]),parts[2]
        try:
            points = float(points)
        except:
            raise BadLine(line)
        if name in marks:
            marks[name]+=points
        else:
            marks[name] = points
    return marks

def read_student_data(path,filename):
    try:
        with open(path+'\\'+filename,'r') as f:
            data = f.readlines()
            if not data:
                raise FileEmpty(filename)      #handles empty files being read.
            student_data = aggregate_marks(data)
            return student_data
    except FileNotFoundError:
        print('File doesn\'t exist')
     




def display_sorted_student_report(student_data):
    with open(path + '\\' + 'sorted_student_marks.txt','w') as f:    
        for item in sorted(student_data.items(),key = lambda i: i[0]):
            # f.write(item)
            data = item[0] + ' ' + str(item[1]) + '\n'
            f.write(data)





def main():
    global path
    path = os.path.dirname(__file__)
    filename = input('Enter the professors filename: ')
    student_data = read_student_data(path,filename)
    display_sorted_student_report(student_data)

if __name__ == '__main__':
    main()