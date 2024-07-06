def sort_students(students):
    house_dict = {'Gryffindor': [], 'Hufflepuff': [], 'Ravenclaw': [], 'Slytherin': []}
    for student in students:
        name, house = student.split()
        house_dict[house].append(name)
    for house in house_dict:
        house_dict[house].sort()
    for house in house_dict.keys(): # house names are already sorted in order
        print(house)
        for student in house_dict[house]:
            print(student)

n = int(input())
students = [input() for _ in range(n)]
sort_students(students)
