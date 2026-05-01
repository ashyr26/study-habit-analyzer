print("STUDY HABIT ANALYZER")

study=int(input("Enter your study hours: "))
sleep=int(input("Enter your sleep hours: "))
procrastination=int(input("Enter procastination level (1-10): "))

SHA=(study*1.5)+(sleep*2)-(procrastination*3)

print("your score is: ",SHA)
