import time
import json
import smtplib

import datetime


rotation1workout={"Bench Press 3x10":"",
                  "Dumbell Shoulder Press 3x10":"",
                  "Dip 2x12":"",
                  "Low to high V Cable 3x15":"",
                  "Dumbell Skull crusher 3x12":"",
                  "Dumbell Lat Raise 3x20":"",
                  "Plank":""}

rotation2workout={"Squat 3x8":"",
                  "Romanian Deadlift 2x10":"",
                  "Cable pull through 2x12":"",
                  "Dumbell Walking Lunge 2x20":"",
                  "Leg Extension 2x15":"",
                  "Leg Curl 2x15":"",
                  "Standing Calf Raise 3x10":"",

                  }
rotation3workout={"Lat Pulldown 2x20":"",
                  "Pull Up Assisted 2x8":"",
                  "Pendlay Row 3x10":"",
                  "Dumbell Row  3x10":"",
                  "Facepull 3x20":"",
                  "Ez bar reverse and normal curve superset 3x15":"",
                  "Preacher Curl 3x12":""}
rotation4workout={"Bench Press Close Grip 3x10":"",
                  "Incline Dumbell Press 3x10":"",
                  "Standing Shoulder Press 3x10":"",
                  "Chest Pec Deck 2x15":"",
                  "Triceps Rope 2x15":"",
                  "Cable Lat Raise 3x15":"",
                  }
rotation5workout={"Neutral Grip Pulldown 4x10":"",
                  "Cable Row 3x10":"",
                  "Cable Row Elbows Out 3x10":"",
                  "Straight Arm Cable Pullover 3x15":"",
                  "Snatch Grip Barbell Shrug 3x15":"",
                  "Cable Reverse Fly 3x20":"",
                  "Cable Curl 3x12":"",
                  "Hammer Curl 3x8":"",
                 }

now = datetime.datetime.now()



def rotation1input():
    print("Enter notes for today's moves:")
    a = input("Bench Press 3x10: ")
    b = input("Dumbell Shoulder Press 3x10: ")
    c = input("Dip 2x12: ")
    d = input("Low to high V Cable 3x15: ")
    e = input("Dumbell Skull crusher 3x12: ")
    f = input("Dumbell Lat Raise 3x20: ")
    g = input("Plank: ")


    rotation1workout.update({"Bench Press 3x10":a,
                  "Dumbell Shoulder Press 3x10":b,
                  "Dip 2x12":c,
                  "Low to high V Cable 3x15":d,
                  "Dumbell Skull crusher 3x12":e,
                  "Dumbell Lat Raise 3x20":f,
                  "Plank":g,
                  })

    print(rotation1workout)
    f = open("archive.txt", "a")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation1workout.keys():
        f.write(F"{k}: {rotation1workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
    f = open("dict.txt", "w")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation1workout.keys():
        f.write(F"{k}: {rotation1workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
def rotation2input():
    print("Enter notes for today's moves:")
    a=input("Squat 3x8: ")
    b = input("Romanian Deadlift 2x10: ")
    c = input("Cable pull through 2x12: ")
    d = input("Dumbell Walking Lunge 2x20: ")
    e = input("Leg Extension 2x15: ")
    f = input("Leg Curl 2x15: ")
    g = input("Standing Calf Raise 3x10:")

    rotation2workout.update({"Squat 3x8":a,
                  "Romanian Deadlift 2x10":b,
                  "Cable pull through 2x12":c,
                  "Dumbell Walking Lunge 2x20:":d,
                  "Leg Extension 2x15":e,
                  "Leg Curl 2x15":f,
                  "Standing Calf Raise 3x10":g,

                  })
    print(rotation2workout)
    f = open("archive.txt", "a")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation2workout.keys():
        f.write(F"{k}: {rotation2workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
    f = open("dict.txt", "w")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation2workout.keys():
        f.write(F"{k}: {rotation2workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
def rotation3input():
    print("Enter notes for today's moves:")
    a=input("Lat Pulldown 2x20: ")
    b = input("Pull Up Assisted 2x8: ")
    c = input("Pendlay Row 3x10: ")
    d = input("Dumbell Row  3x10: ")
    e = input("Facepull 3x20: ")
    g = input("Ez bar reverse and normal curve superset 3x15: ")
    h = input("Preacher Curl 3x12: ")
    rotation3workout.update({"Lat Pulldown 2x20":a,
                  "Pull Up Assisted 2x8":b,
                  "Pendlay Row 3x10":c,
                  "Dumbell Row  3x10":d,
                  "Facepull 3x20":e,

                  "Ez bar reverse and normal curve superset 3x15":g,
                  "Preacher Curl 3x12":h})
    print(rotation3workout)
    f = open("archive.txt", "a")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation3workout.keys():
        f.write(F"{k}: {rotation3workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
    f = open("dict.txt", "w")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation3workout.keys():
        f.write(F"{k}: {rotation3workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
def rotation4input():
    print("Enter notes for today's moves:")
    a=input("Bench Press Close Grip 3x10: ")
    b = input("Incline Dumbell Press 3x10: ")
    c = input("Standing Shoulder Press 3x10: ")
    d = input("Chest Pec Deck 2x15: ")
    e = input("Triceps Rope 2x15: ")
    f = input("Cable Lat Raise 3x15: ")

    rotation4workout.update({"Bench Press Close Grip 3x10":a,
                  "Incline Dumbell Press 3x10":b,
                  "Standing Shoulder Press 3x10":c,
                  "Chest Pec Deck 2x15":d,
                  "Triceps Rope 2x15":e,
                  "Cable Lat Raise 3x15":f,})

    print(rotation4workout)

    f = open("archive.txt", "a")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation4workout.keys():
        f.write(F"{k}: {rotation4workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
    f = open("dict.txt", "w")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation4workout.keys():
        f.write(F"{k}: {rotation4workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
def rotation5input():
    print("Enter notes for today's moves:")
    a=input("Neutral Grip Pulldown 4x10: ")
    b = input("Cable Row 3x10: ")
    c = input("Cable Row Elbows Out 3x10: ")
    d = input("Straight Arm Cable Pullover 3x15: ")
    e = input("Snatch Grip Barbell Shrug 3x15: ")
    f = input("Cable Reverse Fly 3x20: ")
    g = input("Cable Curl 3x12: ")
    h = input("Hammer Curl 3x8: ")


    rotation5workout.update({"Neutral Grip Pulldown 4x10":a,
                  "Cable Row 3x10":b,
                  "Cable Row Elbows Out 3x10":c,
                  "Straight Arm Cable Pullover 3x15":d,
                  "Snatch Grip Barbell Shrug 3x15":e,
                  "Cable Reverse Fly 3x20":f,
                  "Cable Curl 3x12":g,
                  "Hammer Curl 3x8":h,
                  })
    print(rotation5workout)
    f = open("archive.txt", "a")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation5workout.keys():
        f.write(F"{k}: {rotation5workout[k]}\n")  # add comma at end of line
    f.write("\n")
    f.close()
    f = open("dict.txt", "w")
    f.write(f"------------------------\n{now.date()} {now.strftime('%A')}\n")
    for k in rotation5workout.keys():
        f.write(F"{k}: {rotation5workout[k]}\n")  # add comma at end of line
    f.write("\n One step closer to our domination ! \n")
    f.close()


rotationinput=int(input("What rotation workout did you do today?: "))
if rotationinput==1:
    rotation1input()
elif rotationinput==2:
    rotation2input()
elif rotationinput==3:
    rotation3input()
elif rotationinput==4:
    rotation4input()
elif rotationinput==5:
    rotation5input()

f = open("dict.txt", "r")
x=f.read()
print(x)
my_email="breakdown460@gmail.com" # this is where you wnt
password="vmeo lqrp rwjv spjs"
connection=smtplib.SMTP_SSL("smtp.gmail.com")


connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="mehmetefekasar34@icloud.com",msg=f"Subject:Rotation {rotationinput} report\n\n{x} ")
connection.close()
