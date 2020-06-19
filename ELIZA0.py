#My purpose is to vaguely reverse engineered the ELIZA chatbot. The point of the program is not to help solve the clients'problems
#but to keep prolonging the conversation, keep the clients talking (Like an actual counsellor). It should best imitate an actual human
# https://dl.acm.org/doi/10.1145/357980.357991#:~:text=Abstract,appearing%20in%20the%20input%20text
#Weizenbaum, Joseph "ELIZA – A Computer Program For the Study of Natural Language Communication Between Man and Machine"
#in: Communications of the ACM; Volume 9 , Issue 1 (January 1966): p 36-45
import numpy as np

class ELIZA:
    def __init__(self, ver):
        self.ver = ver
        self.repository = list() #A global repository of words the patient has input
        self.pathindex = 0
        self.listIllness = ["anxiety", "stress", "anorexia", \
            "bulimia", "depression", "PTSD", "OCD"] 
        self.currentTokens = list() #A temporary repository of words, gets emptied after every loop
        self.listFamily = ["mom", "mother", "dad", "father", "son", "daughter", "grandfather",\
                           "granddad", "grandmother", "grandma", "sister", "sis", "brother", "bro",\
                           "uncle", "aunt"]
        self.dictFamily = {"mother": ["she", "her", "her", "hers"],
                           "father": ["he" , "him", "his", "his" ],
                           "son"   : ["he" , "him", "his", "his" ],
                           "brother":["he" , "him", "his", "his" ],
                           "sister": ["she", "her", "her", "hers"],
                           "daughter":["she", "her", "her", "hers"],
                           "grandmother":["she", "her", "her", "hers"],
                           "grandfather":["he" , "him", "his", "his" ],
            }
        self.negatives = ["shouldn't", "not", "never", "didn't", "doesn't",\
            "won't", "wasn't", "hasn't", "haven't", "aren't", "isn't"]
        self.asksPhrases = ["what", "when", "where", "why", "who", "whom","is", "does", "will", "was", "have", "has"]
        self.delimiters = [',', '.', ';', ':',' ', '&', '?', '!']

    def initializeTheConvo(self): #Initializing the conversation. First, without the original user input
        i = np.random.randint(0,2)
        if(i == 0):
            print("ELIZA: Hi, I'm Eliza. How can I help you?")
        elif(i == 1):
            print("ELIZA: Hello, I'm Eliza, and I will be your therapist today. Tell me something about yourself?")
        else:
            print("ELIZA: Hello, I'm Eliza, and I'm here to help you however I can. What do you need my help with?")

    def endTheConvo(self):
        print("ELIZA: Thank you for your time. I hope this session is productive for you.")
        print("ELIZA: I recommend that you drink more water and exercise more.")

    def listen(self):   #Inputing the answer from the user
        self.clientsinput = ""
        self.clientsinput = input()

    def tokenize(self):
        str = self.clientsinput
        index = -1
        for i in range(len(str)):
            if(str[i] in self.delimiters):
                self.currentTokens.append(str[index+1:i].lower())
                index = i
                #Adding the word into the temp repository
         #else: 
           # self.currentTokens.append(str.lower())
            #If there is only one or zero characters in the sentences, add them in anyway
        self.currentTokens.append(str[index+1:len(str)].lower()) #Adding the last word
        print("Tokenize: The currentTokens: ", self.currentTokens)
        
    def basicStemming(self):
        for i in range(len(self.currentTokens)):
            if (len(self.currentTokens[i]) != 0):
                if(self.currentTokens[i][-1] == 's'):
                    self.currentTokens[i] = self.currentTokens[i][:-1]
            if (len(self.currentTokens[i]) != 0):
                if(self.currentTokens[i][-1] == '\''):
                    self.currentTokens[i] = self.currentTokens[i][:-1]
            if(self.currentTokens[i] == 'mom'):
                self.currentTokens[i] = "mother"
            if(self.currentTokens[i] == 'dad'):
                self.currentTokens[i] = "father"
            if(self.currentTokens[i] == 'granddad'):
                self.currentTokens[i] = "grandfather"
            if(self.currentTokens[i] == 'grandma' or self.currentTokens[i] == 'grandmom'):
                self.currentTokens[i] = "grandmother"
            if(self.currentTokens[i] == 'si'):
                self.currentTokens[i] = "sister"
            if(self.currentTokens[i] == 'bro'):
                self.currentTokens[i] = "brother"
            self.repository.append(self.currentTokens[i]) #Add the stemmed into the main repository
        print("basicStemming: The currentTokens: ", self.currentTokens)

    def analyze(self):  #Encoding each path the conversation would take
        for i in range(len(self.currentTokens)):
            #for x in range(len(self.listFamily)):
            if(self.currentTokens[i] in self.listFamily):
                self.pathindex = 2  #Family path
            #for y in range(len(self.listIllness)):
            if(self.currentTokens[i] in self.listIllness):
                self.pathindex = 3 #Illness path
            if(self.currentTokens[i] in self.negatives):
                self.pathindex = 1 #Do not engage in any path, cannot detect context of a negative answer
            #If not, goes to random answer
            self.pathindex = 0

        if (len(self.currentTokens[i]) != 0):
            if(self.currentTokens[0] in self.asksPhrases):
                if("you" in self.currentTokens):
                    self.pathindex = 4 #When the user ask ELIZA about her
                else:
                    self.pathindex = 5 #When the user ask a random question

        for i in range(len(self.currentTokens)):
            if(self.currentTokens[i] == "suicide" or self.currentTokens[i] == "suicide" or self.currentTokens[i] == "pain" or self.currentTokens[i] == "kill" or \
                self.currentTokens[i] == "suicide" or self.currentTokens[i] == "suicide" or self.currentTokens[i] == "suicide" or self.currentTokens[i] == "suicide" or ):

        print("The path index is: ", self.pathindex)


    def answer(self):
        #If the person keeps saying "Hi"
        if("hi" in self.clientsinput or "hello" in self.clientsinput):
            print("ELIZA: Can you tell me a bit about yourself?")

        if(self.pathindex == 0):
        #random responses, works an answer with previous context
            print("That's interesting. Tell me")
            print("By the way, please understand that I can't always give you an attuned response.\n\
                    -- But, please go on.")

        elif(self.pathindex == 1):
            #random responses, works an answer with previous context
            i = np.random.randint(0,3)
            if(i == 0):
                print("ELIZA: What does that suggest to you?")
            elif(i == 1):
                print("ELIZA: Can you please elaborate on that?")
            elif(i == 1):
                print("ELIZA: Really? Tell me more?")
            else:
                print("ELIZA: I'm not sure I understand you fully.")

        elif(self.pathindex == 4):
            #User asked ELIZA about herself
            i = np.random.randint(0,3)
            if(i == 0):
                print("ELIZA: We're discussing you, not me.")
            elif(i == 1):
                print("ELIZA: It depends a lot about the details. Tell me more")
            elif(i == 2):
                print("ELIZA: You're not asking me, are you?")

        elif(self.pathindex == 5):
            #User asked ELIZA about a random question
            i = np.random.randint(0,3)
            if(i == 0):
                print("ELIZA: Have you tried asking someone else?")
            elif(i == 1):
                print("ELIZA: It depends a lot about the details. Tell me more")
            elif(i == 2):
                print("ELIZA: I've not read about this yet. I'll let you know next session. But what do you think?")
            else:
                print("ELIZA: What do you think?")

        self.currentTokens.clear()

    def run(self):
        self.initializeTheConvo()
        self.listen()
        while (self.clientsinput != "Bye" and self.clientsinput != "bye"):
            self.tokenize()
            self.basicStemming()
            self.analyze()
            self.answer()
            self.listen()
        self.endTheConvo()


        

print("Instruction: ELIZA will be speaking to you soon. Please say bye to quit the session.")
       
ELIZA1 = ELIZA(0)
ELIZA1.run()


