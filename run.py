import csv
import random

def readStudentsFromCsv(filename):
    students = {}
    with open(filename, 'r') as f:
      for line in f:
          splitted_line = line.rstrip('\n').split(',')
          students[splitted_line[0]] = splitted_line[1:]
    return students

def buildClasses(students, number_of_classes):
    # TODO: init those with number_of_classes
    classes = [[] for i in range(0, number_of_classes)]
    open_classes = [i for i in range(0, number_of_classes)]

    for student in students.keys():
        # HEREIAM if one class is already full, use the other one
        class_id = open_classes[int(random.uniform(0, len(open_classes)))]
        classes[class_id].append(student)

        if len(classes[class_id]) >= int(len(students) / number_of_classes):
            open_classes.remove(class_id)

    return classes

def calculateScore(students, classes, min_happy_count):
    total_score = 0
    for student, preferences in students.iteritems():
        class_of_student = [class_id for class_id in range(0, len(classes)) if student in classes[class_id]]
        happy_count = 0
        for preferred_student in preferences:
            if preferred_student in classes[class_of_student[0]]:
                happy_count += 1

        if(happy_count < min_happy_count):
            return 0

        total_score += happy_count

    return total_score
    
def printClass(the_class, students):
    for student in the_class:
        preferences = students[student]
        print student
        print '  :-)  ',
        print ', '.join([preference for preference in preferences if preference in the_class])
        print '  :-[  ',
        print ', '.join([preference for preference in preferences if preference not in the_class])

def main():
    wishes = 3
    number_of_classes = 2
    min_happy_count = 1
    max_iterations = 9999

    students = readStudentsFromCsv('students.csv')

    iteration = 0
    best_score = 0; best_classes = []
    while(best_score < wishes and iteration < max_iterations):
        classes = buildClasses(students, number_of_classes)
        score = calculateScore(students, classes, min_happy_count)

        if(score > best_score):
            best_score = score
            best_classes = classes
            happy_ratio = 1.0 * score / len(students) / wishes
            print iteration, happy_ratio, classes

        iteration += 1

    for the_class in best_classes:
        print "=" * 50
        printClass(the_class, students)

if __name__ == "__main__":
    main()
