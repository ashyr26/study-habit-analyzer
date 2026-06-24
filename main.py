from datetime import date

print("STUDY HABIT ANALYZER")

def save_data(study,sleep,p,score):
    today=date.today()

    f=open("study_log.txt","a")
    f.write("Date: "+str(today))
    f.write(" | Study Hours: "+str(study))
    f.write(" | Sleep Hours: "+str(sleep))
    f.write(" | Procrastination Level: "+str(p))
    f.write(" | Score: "+str(round(score,2))+"/10")
    f.write("\n")
    f.close()


goal=int(input("Enter your study goal for today (hours): "))

study=int(input("Enter your study hours: "))
#study feedback
if study==0:
    print("No study time detected today.\nA little progress is better than none, try creating a balanced study routine!")
elif 0<study<=2:
    print("Good efforts!")
elif 2<study<=5:
    print("Locked in!")
elif 6<=study<=9:
    print("Excellent consistency! Keep maintaining balance.")
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

score=(study*2)+(sleep*2.5)-(p*1.5)
score=(score/45)*10

#final score
print()

if score<0:
    score=0
    print("Your habits are weak. Consider improving sleep, focus, and study consistency")

elif score>10:
    score=10
    print("Your habits are very intense. Make sure you're balancing work with rest."'\n'"Remember, consistency matters more than pushing yourself too hard!")

#badges
if score>=8:
    print("🏆 Badge Earned: Productive Day!")
elif score>=6:
    print("⭐ Good Progress!")

print()

#goal feedback
if study>=goal:
    print("🎯 Goal achieved!")
else:
    print("You studied",goal-study,"hour(s) less than your goal.")

print()
print("Your score is:",round(score),"/10")

#suggestions
print("\nSuggestions:")
suggestion=False

if study<4:
    print("- Try increasing study time.")
    suggestion=True
if sleep<7:
    print("- Aim for at least 7-8 hours of sleep.")
    suggestion=True
if p>=6:
    print("- Break tasks into smaller chunks to reduce procrastination.")
    suggestion=True
if suggestion==False:
    print("- Maintain your current habits and strive for consistency!")

save_data(study,sleep,p,score)
print("\nToday's data has been saved successfully!")
