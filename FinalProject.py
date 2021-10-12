# References:
# https://www.kite.com/python/answers/how-to-convert-a-list-of-strings-to-ints-in-python
# https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
# https://www.kite.com/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python

import csv
import sys
import matplotlib.pyplot as plt

csvfile = 'COVID19.csv'
with open(csvfile,'r') as myfile_obj:
    myfile_reader = csv.reader(myfile_obj)
    header = next(myfile_reader)
    StateIndex = header.index('Province_State')
    ConfirmedIndex = header.index('Confirmed')
    DeathsIndex = header.index('Deaths')
    RecoveredIndex = header.index('Recovered')
    ActiveIndex = header.index('Active')
    FatalityIndex = header.index('Case_Fatality_Ratio')
    State = []
    State2 = []
    Confirmed = []
    Deaths = []
    Recovered = []
    Active = []
    Fatality = []
    for row in myfile_reader:
        State.append(row[StateIndex])
        Confirmed.append(row[ConfirmedIndex])
        Deaths.append(row[DeathsIndex])
        Recovered.append(row[RecoveredIndex])
        Active.append(row[ActiveIndex])
        Fatality.append(row[FatalityIndex])
        State2.append([row[StateIndex],row[ConfirmedIndex],row[DeathsIndex],row[RecoveredIndex],row[ActiveIndex],row[FatalityIndex]])
    Recovered = [0 if  i== '' else i for i in Recovered]
    Active = [0 if  i== '' else i for i in Active]
    while("" in Confirmed):
        Confirmed.remove("")
    while("" in Deaths):
        Deaths.remove("")
    Fatality = [0 if  i== '' else i for i in Fatality]
    # Converting string to ints and averaging
    Confirmed_map = map(float,Confirmed)
    Confirmedlist = list(Confirmed_map)
    Confirmedavg = round(sum(Confirmedlist)/len(Confirmedlist),3)
    Death_map = map(float,Deaths)
    Deathlist = list(Death_map)
    Deathavg = round(sum(Deathlist)/len(Deathlist),3)
    Recovered_map = map(float,Recovered)
    Recoveredlist = list(Recovered_map)
    Recoveredavg = round(sum(Recoveredlist)/len(Recoveredlist),3)
    Active_map = map(float,Active)
    Activelist = list(Active_map)
    Activeavg = round(sum(Activelist)/len(Activelist),3)
    Fatality_map = map(float,Fatality)
    Fatalitylist = list(Fatality_map)
    Fatalityavg = round(sum(Fatalitylist)/len(Fatalitylist),3)
    # Graphing the different types of plots based of user input
    def ConfirmedListPlot():
        plt.xticks(fontsize = 10, rotation = 90)
        plt.autoscale()
        plt.plot(State,Confirmedlist,color = 'red')
        plt.title('Confirmed Cases of Covid-19 in the US')
        plt.xlabel('State')
        plt.ylabel('Confirmed Cases')
        plt.grid(True)
        plt.show()
    def DeathListPlot():
        plt.xticks(fontsize = 10, rotation = 90)
        plt.autoscale()
        plt.plot(State,Deathlist,color = 'red')
        plt.title('Number of Deaths due to Covid-19 in the US')
        plt.xlabel('State')
        plt.ylabel('Deaths')
        plt.grid(True)
        plt.show()
    def RecoverdListPlot():
        plt.xticks(fontsize = 10, rotation = 90)
        plt.autoscale()
        plt.plot(State,Recoveredlist,color = 'red')
        plt.title('Number of Recovered People of Covid-19 in the US')
        plt.xlabel('State')
        plt.ylabel('Recovered People')
        plt.grid(True)
        plt.show()
    def ActiveListPlot():
        plt.xticks(fontsize = 10, rotation = 90)
        plt.autoscale()
        plt.plot(State,Activelist,color = 'red')
        plt.title('Number of Active cases of Covid-19 in the US')
        plt.xlabel('State')
        plt.ylabel('Active Cases')
        plt.grid(True)
        plt.show()
    def FatalityListPlot():
        plt.xticks(fontsize = 10, rotation = 90)
        plt.autoscale()
        plt.plot(State,Fatalitylist,color = 'red')
        plt.title('Case Fatality Ratio of Covid-19 in the US')
        plt.xlabel('State')
        plt.ylabel('Case Fatality Ratio')
        plt.grid(True)
        plt.show()
    loop = True
    while loop:
        try:
            Selectioninput = int(input("[0]-Quit [1]-Choosing a State [2]-Print Table [3]-Graphs [4]-Stats: "))
            if(Selectioninput == 1):
                Stateinput = input("Type a state in the United States: ")
                StateinputIndex = State.index(Stateinput)
                if ((Stateinput in State)):
                    menuinput = int(input("Please select one of options [0]-Quit [1]-Confirmed [2]-Deaths [3]-Recovered [4]-Active [5]-Fatality: "))
                    if (menuinput == 1):
                        print(f'The number of confirmed cases in {Stateinput} is {Confirmed[StateinputIndex]}')
                    elif (menuinput == 2):
                        print(f'The number of deaths in {Stateinput} is {Deaths[StateinputIndex]}')
                    elif (menuinput == 3):
                        print(f'The number of people who recovered in {Stateinput} is {Recovered[StateinputIndex]}')
                    elif (menuinput == 4):
                        print(f'The number of active cases in {Stateinput} is {Active[StateinputIndex]}')
                    elif (menuinput == 5):
                        print(f'The number of fatality cases in {Stateinput} is {Fatality[StateinputIndex]}')
                    elif (menuinput == 0):
                        print("Good Bye!")
                        print(" ")
                        loop = False
                    else:
                        print("Invalid Entry! Try Again!")
                        print(" ")
                        loop = True
            elif (Selectioninput == 2):
                print("                         State                         Confirmed                              Deaths                         Recovered                          Active                      Fatality \n")
                for col in State2:
                    print("%30s" %col[0],"  %30s  " %col[1],"  %30s  " %col[2],"  %30s  " %col[3],"  %30s  " %col[4],"  %30s  " %col[5])
            elif(Selectioninput == 3):
                loop1 = True
                while loop1:
                    graphmenu = int(input("Which Graph [0]-Quit [1]-Confirmed [2]-Deaths [3]-Recovered [4]-Active [5]-Fatality:"))
                    if(graphmenu == 1):
                        ConfirmedListPlot()
                        loop1 = True
                    elif(graphmenu == 2):
                        DeathListPlot()
                        loop1 = True
                    elif(graphmenu == 3):
                        RecoverdListPlot()
                        loop1 = True
                    elif(graphmenu == 4):
                        ActiveListPlot()
                        loop1 = True
                    elif(graphmenu == 5):
                        FatalityListPlot()
                        loop1 = True
                    elif(graphmenu == 0):
                        loop1 = False
                    else:
                        print("Invalid Entry! Try Again!")
                        loop = True
            elif(Selectioninput == 4):
                print(f'The average number of confirmed cases in the United States is {Confirmedavg} cases')
                print(f'The average number of deaths in the United States is {Deathavg} cases')
                print(f'The average number of recovered cases in the United States is {Recoveredavg} cases')
                print(f'The average number of active cases in the United States is {Activeavg} cases')
                print(f'The average number of case fatality ratio in the United States is {Fatalityavg} cases')
                loop = True
            elif(Selectioninput == 0):
                print("Good Bye!")
                loop = False
        except:
            print("Invalid Entry!")
