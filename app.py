# What is Text analysis?
#Text analysis, also known as text mining or text analytics, 
# refers to the process of extracting meaningful information and
# insights from textual data.

# What is Text analysis?
#Text analysis, also known as text mining or text analytics, refers to the process of extracting meaningful information and insights from textual data.

#In Part-A, you won't be getting any output as we are just storing the string and creating a class.**
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
#**In Part B, we will be calling the functions created in Part A, allowing the functions to execute and generate output.**

analyzed = TextAnalyzer(givenstring)
#print("Formatted Text:", analyzed.fmtText)
freqMap = analyzed.freqAll()
#print(freqMap)
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")














# class Points(object):
#     def __init__(self, x, y):

#         self.x = x
#         self.y = y

#     def print_point(self):
#         print('x=',self.x,' y=',self.y)        
# p1 = Points(1,2)
# p1.print_point()


#_____________________________#
# for i,x in enumerate(['A','B','C']):
#     print(i+1,x)

#_____________________________#

# x = 5
# while (x!=2):
#     print(x)
#     x = x-1

#_____________________________#

# class Points(object):
#     def _init__(self, x,y):
#         self.x = x
#         self.y = y

#     def print_point(self):
#         print('x=', self.x, 'y=', self.y)

# p2=Points(1,2)
# p2.x = "A"
# p2.print_point()

#______________________________#

# def Delete(x):
#     if x ==0:
#         y=1
#     else:
#         y=0
#     return

#______________________________#

# a = 1 

# def do(x):
#     return(x+a)

# print(do(1))