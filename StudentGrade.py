name = input("Enter student name: ");
math = int(input("Enter Math marks: "));
english = int(input("Enter English marks: "));
python = int(input("Enter Python marks: "));

average = ((math+english+python)/3);

print("Student Name: ",name)

print("Average Marks: ",average);

if average>79 and average<=100:
    print("Final Grade: A+");
elif average>=70 and average<=79:
    print("Final Grade: A");
elif average>=60 and average<=69:
    print("Final Grade: A-");
elif average>=50 and average<=59:
    print("Final Grade: B");
elif average>=40 and average<=49:
    print("Final Grade: C");
elif average<40:
    print("Final Grade: F");
else:
    print("You enter the wrong number")