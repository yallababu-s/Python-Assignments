class multipleFunctions():
    def Subfields():
        subFieldsinAI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for fields in subFieldsinAI:
            print(fields)
        
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
        
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=="Male" and Age>=21):
            print("ELIGIBLE")
        elif(Gender=="Female" and Age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
        
    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=(Total/500)*100
        print("Total :",Total)
        print("Percentage :",Percentage)

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        areaOfTriangle=(Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",areaOfTriangle)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        perimeterOfTriangle=Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeterOfTriangle)