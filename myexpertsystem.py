from tkinter import *
from tkinter import messagebox 
from experta import *

age = ""
gender = ""
polyuria = ""
polydipsia = ""
sudden_weight_loss = ""
weakness = ""
polyphagia = ""
genital_thrush = ""
visual_blurring = ""
itching = ""
irritability = ""
delayed_healing = ""
partial_paresis = ""
muscle_stiffness = ""
alopecia = ""
obesity = ""
result = ""
  
class Diabetes(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find")

    @Rule(Fact(action=L('find')),
        NOT(Fact(Age=W())),salience = 1000)
    def askAge(self):
        self.declare(Fact(Age=age))
       
    @Rule(Fact(action=L('find')),
        NOT(Fact(Gender=W())),salience = 995)
    def askGender(self):
        self.declare(Fact(Gender=gender))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Polyuria=W())),salience = 990)
    def askPolyuria(self):
        self.declare(Fact(Polyuria=polyuria))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Polydipsia=W())),salience = 985)
    def askPolydipsia(self):
        self.declare(Fact(Polydipsia=polydipsia))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Sudden_weight_loss=W())),salience = 980)
    def askSuddenWeightLoss(self):
        self.declare(Fact(Sudden_weight_loss=sudden_weight_loss))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Weakness=W())),salience = 975)
    def askWeakness(self):
        self.declare(Fact(Weakness=weakness))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Polyphagia=W())),salience = 970)
    def askPolyphagia(self):
        self.declare(Fact(Polyphagia=polyphagia))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Genital_Thrush=W())),salience = 965)
    def askGenitalThrush(self):
        self.declare(Fact(Genital_Thrush=genital_thrush))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Visual_Blurring=W())),salience = 960)
    def askVisualBlurring(self):
        self.declare(Fact(Visual_Blurring=visual_blurring))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Itching=W())),salience = 955)
    def askItching(self):
        self.declare(Fact(Itching=itching))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Irritability=W())),salience = 950)
    def askIrritability(self):
        self.declare(Fact(Irritability=irritability))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Delayed_Healing=W())),salience = 945)
    def askDelayedHealing(self):
        self.declare(Fact(Delayed_Healing=delayed_healing))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Partial_Paresis=W())),salience = 940)
    def askPartialParesis(self):
        self.declare(Fact(Partial_Paresis=partial_paresis))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Muscle_Stiffness=W())),salience = 935)
    def askMuscleStiffness(self):
        self.declare(Fact(Muscle_Stiffness=muscle_stiffness))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Alopecia=W())),salience = 930)
    def askAlopecia(self):
        self.declare(Fact(Alopecia=alopecia))

    @Rule(Fact(action=L('find')),
        NOT(Fact(Obesity=W())),salience = 925)
    def askObesity(self):
        self.declare(Fact(Obesity=obesity))

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Muscle_Stiffness=L("NO"))),salience = 920)
    def ruleOne(self, Age):
        global result
        if float(Age) <= 34.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Muscle_Stiffness=L("YES"))),salience = 915)
    def ruleTwo(self, Age):
        global result
        if float(Age) <= 34.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Irritability=L("NO"))),salience = 910)
    def ruleThree(self, Age):
        global result
        if float(Age) > 34.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Irritability=L("YES")),
          Fact(Polydipsia=L("NO"))),salience = 905)
    def ruleFour(self,Age):
        global result
        if float(Age) > 34.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Irritability=L("YES")),
          Fact(Polydipsia=L("YES"))),salience = 900)
    def ruleFive(self, Age):
        global result
        if float(Age) > 34.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("YES")),
          Fact(Delayed_Healing=L("NO"))),salience = 895)
    def ruleSix(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Positive"))
        result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Female")),
          Fact(Alopecia=L("YES")),
          Fact(Delayed_Healing=L("YES"))),salience = 890)
    def ruleSeven(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Negative"))
        result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Delayed_Healing=L("NO"))),salience = 885)
    def ruleEight(self, Age):
        global result
        if float(Age) <= 65.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Delayed_Healing=L("YES"))),salience = 880)
    def ruleNine(self, Age):
        global result
        if float(Age) <= 65.5:
            if float(Age) <= 40.0:
                self.declare(Fact(action="stop"))
                self.declare(Fact(disease="Positive"))
                result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Delayed_Healing=L("YES")),
          Fact(Alopecia=L("NO")),
          Fact(Muscle_Stiffness=L("NO"))),salience = 875)
    def ruleTen(self, Age):
        global result
        if float(Age) <= 65.5:
            if float(Age) > 40.0:
                self.declare(Fact(action="stop"))
                self.declare(Fact(disease="Positive"))
                result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Delayed_Healing=L("YES")),
          Fact(Alopecia=L("NO")),
          Fact(Muscle_Stiffness=L("YES"))),salience = 870)
    def ruleEleven(self, Age):
        global result
        if float(Age) <= 65.5:
            if float(Age) > 40.0:
                self.declare(Fact(action="stop"))
                self.declare(Fact(disease="Negative"))
                result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Delayed_Healing=L("YES")),
          Fact(Alopecia=L("YES"))),salience = 865)
    def ruleTwelve(self, Age):
        global result
        if float(Age) <= 65.5:
            if float(Age) > 40.0:
                self.declare(Fact(action="stop"))
                self.declare(Fact(disease="Negative"))
                result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Muscle_Stiffness=L("NO")),
          Fact(Delayed_Healing=L("NO"))),salience = 860)
    def ruleThirteen(self, Age):
        global result
        if float(Age) > 65.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Muscle_Stiffness=L("NO")),
          Fact(Delayed_Healing=L("YES"))),salience = 855)
    def ruleFourteen(self, Age):
        global result
        if float(Age) > 65.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Muscle_Stiffness=L("YES"))),salience = 850)
    def ruleFifteen(self, Age):
        global result
        if float(Age) > 65.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("YES")),
          Fact(Genital_Thrush=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Polyphagia=L("NO"))),salience = 845)
    def ruleSixteen(self, Age):
        global result
        if float(Age) <= 42.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("YES")),
          Fact(Genital_Thrush=L("NO")),
          Fact(Age=MATCH.Age),
          Fact(Polyphagia=L("YES"))),salience = 840)
    def ruleSeventeen(self, Age):
        global result
        if float(Age) <= 42.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("YES")),
          Fact(Genital_Thrush=L("NO")),
          Fact(Age=MATCH.Age)),salience = 835)
    def ruleEighteen(self, Age):
        global result
        if float(Age) > 42.5:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("NO")),
          Fact(Irritability=L("YES")),
          Fact(Genital_Thrush=L("YES"))),salience = 830)
    def ruleNineteen(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Positive"))
        result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("YES")),
          Fact(Muscle_Stiffness=L("NO")),
          Fact(Partial_Paresis=L("NO"))),salience = 825)
    def ruleTwenty(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Positive"))
        result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("YES")),
          Fact(Muscle_Stiffness=L("NO")),
          Fact(Partial_Paresis=L("YES")),
          Fact(Sudden_Weight_Loss=L("NO"))),salience = 820)
    def ruleTwentyone(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Negative"))
        result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("YES")),
          Fact(Muscle_Stiffness=L("NO")),
          Fact(Partial_Paresis=L("YES")),
          Fact(Sudden_Weight_Loss=L("YES"))),salience = 815)
    def ruleTwentytwo(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Positive"))
        result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("YES")),
          Fact(Muscle_Stiffness=L("YES")),
          Fact(Obesity=L("NO"))),salience = 810)
    def ruleTwentythree(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Negative"))
        result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("NO")),
          Fact(Gender=L("Male")),
          Fact(Polydipsia=L("YES")),
          Fact(Muscle_Stiffness=L("YES")),
          Fact(Obesity=L("YES"))),salience = 805)
    def ruleTwentyfour(self):
        global result
        self.declare(Fact(action="stop"))
        self.declare(Fact(disease="Positive"))
        result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Polydipsia=L("NO")),
          Fact(Obesity=L("NO"))),salience = 800)
    def ruleTwentyfive(self, Age):
        global result
        if float(Age) <= 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Polydipsia=L("NO")),
          Fact(Obesity=L("YES")),
          Fact(Alopecia=L("NO"))),salience = 795)
    def ruleTwentysix(self, Age):
        global result
        if float(Age) <= 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Polydipsia=L("NO")),
          Fact(Obesity=L("YES")),
          Fact(Alopecia=L("YES")),
          Fact(Delayed_Healing=L("NO"))),salience = 790)
    def ruleTwentyseven(self, Age):
        global result
        if float(Age) <= 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Polydipsia=L("NO")),
          Fact(Obesity=L("YES")),
          Fact(Alopecia=L("YES")),
          Fact(Delayed_Healing=L("YES"))),salience = 785)
    def ruleTwentyeight(self, Age):
        global result
        if float(Age) <= 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Polydipsia=L("YES"))),salience = 780)
    def ruleTwentynine(self, Age):
        global result
        if float(Age) <= 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Weakness=L("NO"))),salience = 775)
    def ruleThirty(self, Age):
        global result
        if float(Age) > 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Negative"))
            result = "Result is negative, you seem good."

    @Rule(AND(Fact(action=L('find')),
          Fact(Polyuria=L("YES")),
          Fact(Age=MATCH.Age),
          Fact(Weakness=L("YES"))),salience = 770)
    def ruleThirtyone(self, Age):
        global result
        if float(Age) > 71.0:
            self.declare(Fact(action="stop"))
            self.declare(Fact(disease="Positive"))
            result = "Result is positive, you should see a doctor!"

    @Rule(AND(Fact(action=L('find')),
          NOT(Fact(disease=W()))),salience = -1)
    def unmatched(self):
        global result
        result = "Result is unknown."


frame = Tk()
frame.title("Diabetes Risk")
width = 600
height = 300
screen_width = frame.winfo_screenwidth()
screen_height = frame.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
frame.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl = Label(frame, text = "Hello, what is your name?")
lbl.pack()

lblquestion = Label(frame, text = "")

inputtxt = Text(frame, height = 2, width = 20)
inputtxt.pack()
inputage = Text(frame, height = 2, width = 20)

def resultQuestion():
    global result
    engine = Diabetes()
    engine.reset()
    engine.run()
    lblquestion.config(text = result)

def getObesityInput():
    global obesity
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        obesity = "YES"
        continueButton.destroy()
        C1.destroy()
        C2.destroy()
        resultQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        obesity = "NO"
        continueButton.destroy()
        C1.destroy()
        C2.destroy()
        resultQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def obesityQuestion():
    lblquestion.config(text = "Do you have obesity? ")
    continueButton.config(command=getObesityInput)

def getAlopeciaInput():
    global alopecia
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        alopecia = "YES"
        C1.deselect()
        obesityQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        alopecia = "NO"
        C2.deselect()
        obesityQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def alopeciaQuestion():
    lblquestion.config(text = "Do you have alopecia (hair loss)? ")
    continueButton.config(command=getAlopeciaInput)

def getMuscleStiffnessInput():
    global muscle_stiffness
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        muscle_stiffness = "YES"
        C1.deselect()
        alopeciaQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        muscle_stiffness = "NO"
        C2.deselect()
        alopeciaQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def muscleStiffnessQuestion():
    lblquestion.config(text = "Do you have muscle stiffness? ")
    continueButton.config(command=getMuscleStiffnessInput)

def getPartialParesisInput():
    global partial_paresis
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        partial_paresis = "YES"
        C1.deselect()
        muscleStiffnessQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        partial_paresis = "NO"
        C2.deselect()
        muscleStiffnessQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def partialParesisQuestion():
    lblquestion.config(text = "Do you have partial paresis (weakened muscle movement)? ")
    continueButton.config(command=getPartialParesisInput)

def getDelayedHealingInput():
    global delayed_healing
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        delayed_healing = "YES"
        C1.deselect()
        partialParesisQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        delayed_healing = "NO"
        C2.deselect()
        partialParesisQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def delayedHealingQuestion():
    lblquestion.config(text = "Do you have delayed healing? ")
    continueButton.config(command=getDelayedHealingInput)

def getIrritabilityInput():
    global irritability
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        irritability = "YES"
        C1.deselect()
        delayedHealingQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        irritability = "NO"
        C2.deselect()
        delayedHealingQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def irritabilityQuestion():
    lblquestion.config(text = "Do you have irritability? ")
    continueButton.config(command=getIrritabilityInput)

def getItchingInput():
    global itching
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        itching = "YES"
        C1.deselect()
        irritabilityQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        itching = "NO"
        C2.deselect()
        irritabilityQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def itchingQuestion():
    lblquestion.config(text = "Do you have itching? ")
    continueButton.config(command=getItchingInput)

def getVisualBlurringInput():
    global visual_blurring
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        visual_blurring = "YES"
        C1.deselect()
        itchingQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        visual_blurring = "NO"
        C2.deselect()
        itchingQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def visualBlurringQuestion():
    lblquestion.config(text = "Do you have visual blurring? ")
    continueButton.config(command=getVisualBlurringInput)

def getGenitalThrushInput():
    global genital_thrush
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        genital_thrush = "YES"
        C1.deselect()
        visualBlurringQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        genital_thrush = "NO"
        C2.deselect()
        visualBlurringQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def genitalThrushQuestion():
    lblquestion.config(text = "Do you have genital thrush? ")
    continueButton.config(command=getGenitalThrushInput)

def getPolyphagiaInput():
    global polyphagia
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        polyphagia = "YES"
        C1.deselect()
        genitalThrushQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        polyphagia = "NO"
        C2.deselect()
        genitalThrushQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def polyphagiaQuestion():
    lblquestion.config(text = "Do you have polyphagia (excessive hunger)? ")
    continueButton.config(command=getPolyphagiaInput)

def getWeaknessInput():
    global weakness
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        weakness = "YES"
        C1.deselect()
        polyphagiaQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        weakness = "NO"
        C2.deselect()
        polyphagiaQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def weaknessQuestion():
    lblquestion.config(text = "Do you have weakness? ")
    continueButton.config(command=getWeaknessInput)

def getSuddenWeightLossInput():
    global sudden_weight_loss
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        sudden_weight_loss = "YES"
        C1.deselect()
        weaknessQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        sudden_weight_loss = "NO"
        C2.deselect()
        weaknessQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def suddenWeightLossQuestion():
    lblquestion.config(text = "Do you have sudden weight loss? ")
    continueButton.config(command=getSuddenWeightLossInput)

def getPolydipsiaInput():
    global polydipsia
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        polydipsia = "YES"
        C1.deselect()
        suddenWeightLossQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        polydipsia = "NO"
        C2.deselect()
        suddenWeightLossQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")

def polydipsiaQuestion():
    lblquestion.config(text = "Do you have polydipsia (excessive thirst)? ")
    continueButton.config(command=getPolydipsiaInput)

def getPolyuriaInput():
    global polyuria
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        polyuria = "YES"
        C1.deselect()
        polydipsiaQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        polyuria = "NO"
        C2.deselect()
        polydipsiaQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")


def polyuriaQuestion():
    lblquestion.config(text = "Do you have polyuria (excessive urine production)? ")
    C1.config(text="YES")
    C2.config(text="NO")
    continueButton.config(command=getPolyuriaInput)

def getGenderInput():
    global gender
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        gender = "Female"
        C1.deselect()
        polyuriaQuestion()
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        gender = "Male"
        C2.deselect()
        polyuriaQuestion()
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1:
        messagebox.showwarning(title="Warning", message="Please only check one box!")
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0:
        messagebox.showwarning(title="Warning", message="Please only check one of the boxes!")
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Hello, " + inp)
    inputtxt.destroy()
    continueButtonName.destroy()
    ageQuestion()

def genderQuestion():
    lblquestion.config(text = "What is your gender? ")
    C1.pack()
    C2.pack()
    continueButton.pack()
    
def getAgeInput():
    global age
    age = inputage.get(1.0, "end-1c")
    if age == "":
        messagebox.showwarning(title="Warning", message="Please enter your age!")
    elif age.isdigit() == False or int(age) == 0:
        messagebox.showwarning(title="Warning", message="Please enter a positive integer!")
    else:
        age = inputage.get(1.0, "end-1c") 
        inputage.destroy()
        continueButtonAge.destroy()
        genderQuestion()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(frame, text = "Female", variable = CheckVar1,
            height=5, width = 20)
C2 = Checkbutton(frame, text = "Male", variable = CheckVar2,
            height=5, width = 20)

continueButton = Button(frame,
                        text = "Continue", 
                        command = getGenderInput) 

continueButtonAge = Button(frame,
                        text = "Continue", 
                        command = getAgeInput) 
continueButtonName = Button(frame,
                        text = "Continue", 
                        command = printInput)
continueButtonName.pack()

def ageQuestion():
    lblquestion.config(text = "What is your age? ")
    lblquestion.pack()
    inputage.pack()
    continueButtonAge.pack()
    inputtxt.destroy()
    continueButtonName.destroy()

frame.mainloop()