class employee():

    #constructor
    def __init__(self, name = "", hours = 0, hourate = 0):
        self.name = name
        self.hours = hours
        self.hourate = hourate
        
    #setter
    def setname(self, name):
        self.name = name
    def sethours(self, hours):
        if hours > 0:
            self.hours = hours
    def sethourate(self, hourate):
        if hourate > 0:
            self.hourate = hourate

    #getters
    def gettername(self):
        return self.name
    def getterhours(self):
        return self.hours
    def getterhourate(self):
        return self.hourate

    #uses setter methods in class
    def get_input(self):
        print()
        self.setname(input("Enter a name: "))
        self.sethours(float(input("Enter hours worked: ")))
        self.sethourate(float(input("Enter hourly rate: ")))

    #print(employee) will show single employee info
    def __str__(self):
        return ("\n\nName:" + str(self.gettername()) + "\nHours Worked:" + str(self.getterhours()) + "\nHourly Rate:" + str(self.getterhourate())) 


    #calculate single employee pay
    def calc_pay(self):
        if (self.hours > 40):
            return ((40 * self.hourate) + ((self.hours - 40) * (1.5 * self.hourate)))
        else:
            return (self.hours * self.hourate)

    
print("1: Enter an employee")
print("q: Quit the application")
i = str(input(""))
if i == "q":
    print("No employees were entered")
else:
    y=0
    lst = []
    while i != "q":
        while i == "1":
            
            e = employee()
            e.get_input()
            
            lst.append(e)
            y += 1
            print()
            print("1: Enter an employee")
            print("2: Print employee list")
            print("q: Quit the application")
            
            i = input("")

        if i == "2":
            for j in lst:
                print(j)

                print()
            print("1: Enter an employee")
            print("2: Print employee list")
            print("q: Quit the application")
            i = str(input(""))

    total=0
    avg = 0
    for j in lst:
        total += j.calc_pay()
    avg = total / len(lst)

    print()
    print("The total amount to be paid is ${:.2f}".format(total))
    print("The average employee is paid ${:.2f}".format(avg))
        

       
