def gradingStudents(grades):
    ans = []
    for grade in grades:
        if grade<38:
            ans.append(grade)
        elif grade%5>2:
            grade = (grade//5 +1)*5
            ans.append(grade)
        else:
            ans.append(grade)
    return ans        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
