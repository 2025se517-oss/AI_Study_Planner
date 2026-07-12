##Class
import datetime
import random
import inspect
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  

original_print = print
colors = [Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.CYAN]
color_index = 0
function_colors = {}

def print(*args, **kwargs):
    global color_index
    if len(args) == 1 and args[0] in colors:
        return
    function_name = inspect.currentframe().f_back.f_code.co_name
    if function_name not in function_colors:
        function_colors[function_name] = colors[color_index % len(colors)]
        color_index += 1
    color = function_colors[function_name]
    end = kwargs.pop("end", "\n")
    original_print(color, end="", file=kwargs.get("file"))
    original_print(*args, end=Color.RESET + end, **kwargs)

class Planner:
    
    def __init__(self):
        self.subjects={}
        self.quotes = [
            
            "Push yourself, because no one else is going to do it for you.",
            "Success is not final; failure is not fatal: It is the courage to continue that counts.",
            "Hard work beats talent when talent doesn't work hard.",
            "Dream it. Wish it. Do it.",
            "Stay focused and never give up!"
        ]
        print(f"{Color.RED}")
        print(" AI Study Planner Started Successfully!")
        print(f"{Color.CYAN}")
    
    def add_subjects(self):
        subject_name=input("Enter the Subject Name:").strip().title()
        if not subject_name :
            print("You not entered any subject:")
            return 
        if subject_name in self.subjects:
            print("Subject Already Exist:")
            return 
        try:
            goal_hours=int(input("Enter the Goal Hours:"))
            if goal_hours<=-1:
                print("Please Put the correct number:")
                return 
            total_topics=int(input("Enter the total topics:"))
            if total_topics<=-1:
                print("Please put the correct data:")
                return 
        except:
            print("Only Numbers Allowed!")
            return 
        self.subjects[subject_name]={
            "Hours":0,
            "Goal Hours":goal_hours,
            "Total Topics":total_topics,
            "Topics Completed":0,
            "Status":" In Progress",
            "Last Study":"No Studied yet"
        }
        print("Subject Added Successfully:")

    def show_subjects(self):
     if not self.subjects:
        print("No Subject Added Yet!")
        return
     print("=========================")
     print("    AI Study Planner")
     print("=========================")
     for key,value in self.subjects.items():
        print(f"\nSubject : {key}")
        print(f"Hours : {value['Hours']}")
        print(f"Goal Hours : {value['Goal Hours']}")
        print(f"Total Topics : {value['Total Topics']}")
        print(f"Topics Completed : {value['Topics Completed']}")
        print(f"Status : {value['Status']}")
        print(f"Last Study:{value['Last Study']}")

    def search_subjects(self):
       subject_name = input("Enter the Subject Name: ").strip().title()

       if not subject_name:
          print("You did not enter any subject.")
          return

       if subject_name not in self.subjects:
          print("Subject Not Found!")
          return

       print("\n===== Subject Found =====")

       value = self.subjects[subject_name]

       print(f"Subject : {subject_name}")
       print(f"Hours : {value['Hours']}")
       print(f"Goal Hours : {value['Goal Hours']}")
       print(f"Total Topics : {value['Total Topics']}")
       print(f"Topics Completed : {value['Topics Completed']}")
       print(f"Status : {value['Status']}")
       print(f"Last Study:{value['Last Study']}")
        
    def update_progress(self):
        subject_name=input("Enter the subject name:").strip().title()
        if  subject_name not in self.subjects:
            print("Subject Not found:")
            return
        if subject_name in self.subjects:
            print("Please update Your Data:")
            try:
                new_hours=int(input("Enter the  hours:"))
                if new_hours<0:
                    print("Time never be negative:")
                    return
                
                new_topic=int(input("Enter the new topics:"))
                if new_topic<0:
                    print("Please put the correct data:")
                    return
                self.subjects[subject_name]["Hours"]+=new_hours

                updated_hour=self.subjects[subject_name]["Hours"]

                goal_hours=self.subjects[subject_name]["Goal Hours"]

                self.subjects[subject_name]["Topics Completed"]+=new_topic

                updated_topics=self.subjects[subject_name]["Topics Completed"]

                total_topics=self.subjects[subject_name]["Total Topics"]
                if updated_hour>=goal_hours or updated_topics>=total_topics:
                    print("Status Completed:")
                    self.subjects[subject_name]["Status"]="Completed"
                else:
                    
                    self.subjects[subject_name]["Status"] = "In Progress"
                now=datetime.datetime.now()
                simple_date=f"{now.day}-{now.month}-{now.year}"
                self.subjects[subject_name]["Last Study"]=simple_date

                
            except:
                print("Only integers Allowed!")
                return

    
    def delete_subjects(self):
        subject_name=input("Enter the subject name:").strip().title()
        if subject_name not in self.subjects:
            print("Subject Not found!")
            return 
        del self.subjects[subject_name]
        print("Subject Deleted:")


    def report(self):

     if not self.subjects:
        print("No Subject Added Yet!")
        return

     print("======================")
     print(" Study Report ")
     print("======================")
     for subject, data in self.subjects.items():

        current_hours = data["Hours"]
        goal_hours = data["Goal Hours"]

        if goal_hours == 0:
            percentage = 0
        else:
            percentage = (current_hours / goal_hours) * 100

        print(f"\nSubject : {subject}")
        print(f"Hours : {current_hours}")
        print(f"Goal Hours : {goal_hours}")
        print(f"Progress : {percentage:.2f}%")
        print(f"Status : {data['Status']}")

    def highest_subject(self):
        if not self.subjects:
            print("No Subject Added yet")
            return
        
        max_hour=-1
        best_subject=""
        for key,value in self.subjects.items():
            current_hours=value["Hours"]
            if current_hours>max_hour:
                max_hour=current_hours
                best_subject=key
        print("=======================")
        print("Winner Subject      ")
        print(f"Subject: {best_subject}")
        print(f"Total Time: {max_hour}")



    def save_data(self):
        try:
            with open("study_data.txt","w") as file:
                for key,value in self.subjects.items():
                    hours=value["Hours"]
                    goal=value["Goal Hours"]
                    total_topics=value["Total Topics"]
                    topics_completed=value["Topics Completed"]
                    status=value["Status"]
                    last_study=value["Last Study"]
                    line=f"{key}:{hours},{goal},{total_topics},{topics_completed},{status},{last_study}\n"
                    file.write(line)    
            print("===============Data Saved==============")  
                  
        except:
            print("Data is Not Saved!")
    def load_data(self):
        try:
            with open("study_data.txt","r") as file:
               self.subjects={}
               for line in file:
                 line.strip()
                 if line!="":
                    parts=line.split(":")
                    name=parts[0]
                    data=parts[1]
                    values=data.split(",")
                    self.subjects[name]={
                        "Hours":int(values[0]),
                        "Goal Hours":int(values[1]),
                        "Total Topics":int(values[2]),
                        "Topics Completed":int(values[3]),
                        "Status":values[4],
                        "Last Study":values[5]
                    }
            print("Data Loaded Successfully:")
        except:
            print("No Previous Data found!")

    def statistics(self):
        if not self.subjects:
            print("No subject Added")
        total_subjects=len(self.subjects)
        completed_subject=0
        progress_subject=0
        total_hours=0
        for key,value in self.subjects.items():
            if value["Status"]=="Completed":
                completed_subject=completed_subject+1
            if value["Status"]==" In Progress":
                progress_subject=progress_subject+1
            total_hours=total_hours+value["Hours"]
        
        print("=======================")
        print("   Statistics           ")
        print("Total Subjects:",total_subjects)
        print("Completed Subjects:",completed_subject)
        print("In Progress Subject:",progress_subject)
        print("Total Study Hours:",total_hours)

    def run(self):
        running=True
        while running:
            self.menu()
            try:
                choice=int(input("Enter the choice (1-11):"))
                if choice==1:
                    self.add_subjects()
                elif choice==2:
                    self.show_subjects()
                elif choice==3:
                    self.search_subjects()
                elif choice==4:
                    self.update_progress()
                elif choice==5:
                    self.delete_subjects()
                elif choice==6:
                    self.report()
                elif choice==7:
                    self.highest_subject()
                elif choice==8:
                    self.save_data()
                    break
                elif choice==9:
                    self.load_data()
                elif choice==10:
                    self.statistics()
                elif choice==11:
                    self.exitt()
                    running=False
                else:
                    print("Invalid Number!")
                    
            except  ValueError:
                print("Only Numbers Allowed:")
                continue
    def exitt(self):
        print("Program Exit Successfully:")


    #####  Menu
    def menu(self):
      """
      Display Menu
      """
      daily_quote=random.choice(self.quotes)
      print(f"Today Quotes: {daily_quote}")
      print("===========================")
      print("***** AI Study Planner ****")
      print("===========================") 
      print("       ")
      print("1.Add Subject:")
      print("2.Show Subject")
      print("3.Search Subject")
      print("4.Update Progress:")
      print("5.Delete Subject:")
      print("6.Report:")
      print("7.Highest Subject:")
      print("8.Save Data:")
      print("9.Load Data")
      print("10.Statistics")
      print("11.Exit")

planner=Planner()
planner.run()

