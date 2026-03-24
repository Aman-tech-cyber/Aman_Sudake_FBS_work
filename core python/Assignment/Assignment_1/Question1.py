# write a program to calculate the percentage of a student based on the marks obtained in 5 subjects. 

math = int(input('Enter marks obtained in math:'))
science = int(input('Enter marks obtained in science:'))
english = int(input('Enter marks obtained in english:'))        
social = int(input('Enter marks obtained in social:'))
hindi = int(input('Enter marks obtained in hindi:'))

total_marks = math + science + english + social + hindi
percentage = (total_marks / 500) * 100
print(f"Total percentage obtained:",percentage)