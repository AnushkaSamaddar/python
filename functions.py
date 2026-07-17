# def greet_again(v1):
#     def get_message():
#         return "Hello "
#     s1 = get_message() + v1
#     print(s1)

# greet_again("John")
# def add(*n):
#     sum = 0
#     for i in n:
#         sum += i

#     return sum

# print(add(2, 3, 4, 3, 34, 89, 600))

students = [
    ("701", "std1", 57), 
    ("702", "std2", 51), 
    ("703", "std3", 28), 
    ("704", "std4", 33), 
    ("705", "std5", 30), 
    ("706", "std6", 12)
]


def is_eligible(students,n=0):
    if n==6:
        return
    students[n][2] < 30
    is_eligible(students,n+1)


eligible = list(filter(is_eligible, students))
print(eligible)

updated_marks = list(map(lambda x:x[2]+5, eligible))
print(updated_marks)