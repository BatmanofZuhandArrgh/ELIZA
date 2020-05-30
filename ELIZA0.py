#My purpose is to vaguely reverse engineered the ELIZA chatbot. The point of the program is not to help solve the clients'problems
#but to keep prolonging the conversation, keep the clients talking (Like an actual counsellor). It should best imitate an actual human
# https://dl.acm.org/doi/10.1145/357980.357991#:~:text=Abstract,appearing%20in%20the%20input%20text
#Weizenbaum, Joseph "ELIZA – A Computer Program For the Study of Natural Language Communication Between Man and Machine"
#in: Communications of the ACM; Volume 9 , Issue 1 (January 1966): p 36-45
import numpy as np

class ELIZA:
    def __init__(self, ver):
        self.ver = ver

    def initializeTheConvo():
        i = np.randint()%3
        if(i == 0):
            print("Hi, I'm Eliza. How can I help you?")
        elif(i == 1):
            print("Hello, I'm Eliza, and I will be your therapist today. Tell me something about yourself?")
        else:
            print("Hello, I'm Eliza, and I'm here to help you however I can. What do you need my help with?")

    def endTheConvo(self):
        if(self.clientsinput == "Bye"):
            print("Thank you for your time. I hope this session is productive for you.")

    def listen(self):
        self.clientsinput = input()

    def answer(self):
        print("Fuck" + self.clientsinput)





       
ELIZA1 = ELIZA(1)
ELIZA1.listen()

print("Hello World")
ELIZA1.answer()
