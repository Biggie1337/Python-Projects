def analyze_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    even_numbers = [evenNumbers for evenNumbers in numbers if evenNumbers % 2 == 0]
    return {
        "sum": total,
        "average": average,
        "evenNumbers": even_numbers
    }

def show_student(**info):
    for key,value in info.items():
        print(f"{key}: {value}")

print(analyze_numbers(5,10,15,20,25,30))
show_student(name = "Dimitar", age = 20, language = "Python", level = "Beginner")

