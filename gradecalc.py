'''
Jon Manczur
Grade calculator
'''
def main():
    #input
    test1 = float(input("Enter first test: "))
    test2 = float(input("Enter second test: "))
    test3 = float(input("Enter third test: "))
    proj1 = float(input("Enter first project: "))
    proj2 = float(input("Enter second project: "))
    proj3 = float(input("Enter third project: "))
    hw_avg = float(input("Enter homework average: "))
    attendance_avg = float(input("Enter attendance average: "))
    #calculations
    test_avg = (test1+test2+test3)/3
    proj_avg = (proj1+proj2+proj3)/3
    grade = test_avg*.3+proj_avg*.3+hw_avg*.3+attendance_avg*.1
    #output
    '''
    if grade >= 92:
        print("You get an A")
    elif grade >= 90:
        print("You get an A-")
    elif grade >= 88:
        print("You get an B+")
    elif grade >= 82:
        print("You get an B")
    elif grade >= 80:
        print("You get an B-")
    elif grade >= 78:
        print("You get an C+")
    elif grade >= 70:
        print("You get an C")
    elif grade >= 60:
        print("You get an D")
    else:
        print("You failed,sucker")
    '''
    if grade <= 60:
        print("You get an F")
    elif grade <= 70:
        print("You get an D")
    elif grade <= 78:
        print("You get an C")
    elif grade <= 80:
        print("You get an C+")
    elif grade <= 82:
        print("You get an B-")
    elif grade <= 88:
        print("You get an B")
    elif grade <= 90:
        print("You get an B+")
    elif grade <= 92:
        print("You get an A-")
    else:
        print("You get an A")

main()
