class multiFunct():
    def Subfields():
        subfields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for field in subfields:
            print(field)
    def OddEven(number):
        if number % 2 == 0:
            print(f"{number} is a Even Number")
        #msg= "Even Number"
        else:
            print(f"{number} is a Odd Number")
    # Function to check marriage eligibility
    def EligibilityForMarriage(gender, age):
        if gender.lower() == 'male' and age >= 21:
            return "Eligible for marriage"
        elif gender.lower() == 'female' and age >= 18:
            return "Eligible for marriage"
        else:
            return "NOT ELIGIBLE"
        # Function to calculate the percentage of marks
    def FindPercent(subject1, subject2, subject3, subject4, subject5):
        total_marks = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total_marks / 5) 
        return total_marks, percentage
    def calculate_area(height, breadth):
        return (height * breadth) / 2

    def calculate_perimeter(height1, height2, breadth):
        return height1 + height2 + breadth
