#Magic8Ball.py
#Name: Olivia Sulzle
#Date: 2/1/26
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  responses = ["It is certain", "Yes definitely", "Without a doubt", "Ask again later", "Cannot predict now", "Sources say no", "Very doubtful", "Don't count on it"]
  #Prompt the user for their question.
  input("What is your question? ")

  #Answer question randomly with one of the options from your earlier list.
  print(random.choice(responses))


if __name__ == '__main__':
  main()
