score = int(input("score: "))

#if they graded assignments like this in Australia i would crash out
if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("grade: C")
elif score >=60:
    print("grade: D")
else:
    print("grade: F")
