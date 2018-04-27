import csv

def score():
    pass

def main():
    students = {}
    with open('students.csv', 'r') as f:
      for line in f:
          splitted_line = line.rstrip('\n').split(',')
          students[splitted_line[0]] = splitted_line[1:]

    for student, preferences in students.iteritems():
        print(student, preferences)
    
#      reader = csv.reader(f)
#      your_list = list(reader)

if __name__ == "__main__":
    main()
