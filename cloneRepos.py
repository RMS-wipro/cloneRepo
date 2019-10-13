import os
import sys
import csv
import getpass


def makeDirectory(year, repository, student, destination):
    try:
        os.mkdir(year)
        try:
            os.mkdir(year + "/" + repository)
            try:
                os.mkdir(year + "/" + repository + "/" + student["student"])
                try:
                    os.mkdir(
                        year
                        + "/"
                        + repository
                        + "/"
                        + student["student"]
                        + "/"
                        + repository
                    )
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass

    command = (
        'git clone  "' + url + "/" + repository + '.git"' + ' "' + destination + '"'
    )
    return command


year = "2019-2020"
group = "grupa1.csv"

group = []
with open("grupa1.csv") as file:
    csv_reader = csv.reader(file, delimiter=",")
    for row in csv_reader:
        group.append({"student": row[0], "url": row[1]})

repository = input("Repository name: ")
username = input("Username: ")
password = getpass.getpass()


for student in group:
    url = student["url"].replace("//", "//" + username + ":" + password + "@")
    destination = (
        "./" + year + "/" + repository + "/" + student["student"] + "/" + repository
    )
    command = makeDirectory(year, repository, student, destination)
    try:
        os.system(command + ">null 2>&1")
        folderPath = "./" + year + "/" + repository + "/" + student["student"]
        folders = os.listdir(os.path.realpath(folderPath))
        if len(folders) == 0:
            os.rmdir(os.path.realpath(folderPath))
    except:
        print("Repository does not exist!")

