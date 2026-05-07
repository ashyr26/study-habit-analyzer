print("STUDY HABIT ANALYZER")

study=int(input("Enter your study hours: "))
#study feedback
if study==0:
    print("No study time detected today.\nA little progress is better than none, try creating a balanced study rotuine!")
elif 0<study<2:
    print("Good efforts!")
elif 2<=study<=5:
    print("Locked in!") 
elif study>9:
    print("Overstudying will cause you stress!")


sleep=int(input("Enter your sleep hours: "))
#sleep feedback
if sleep>10:
    sleep=10
    print("Oversleeping may reduce energy level.")
elif sleep<6:
    print("Insufficient amount of sleep can affect productivity.")
    
p=int(input("Enter procrastination level (1-10): "))
#procrastination feedback
if p>10:
    p=10
    print("High procrastination! Try breaking tasks into smaller parts.")

score=(study*2)+(sleep*2.5)-(p*3)
score=(score/30)*10  #in order to get score out of 10

#final score
print()
if score<0:
    score=0
    print("Your habits are weak. Consider improving sleep, focus, and study consistency")
elif score>10:
    score=0
    print("Your habits are very intense. Make sure you're balancing work with rest.\nRemember, consistency matters more than pushing yourself too hard!")
    
print("your score is: ",round(score),"/10")
