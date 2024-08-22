Quiz = {
    "Questiono 1": {
    "Question" : "What is the capital of France?",
    "answer" : "Paris"
    },
    "Questiono 2": {
    "Question" : "What is the capital of Germany?",
    "answer" : "Berlin"
    },
    "Questiono 3": {
    "Question" : "What is the capital of Italy?",
    "answer" : "Rome"
    },
    "Questiono 4": {
    "Question" : "What is the capital of Spain?",
    "answer" : "Madrid"
    },
    "Questiono 5": {
    "Question" : "What is the capital of Portugal?",
    "answer": "Lisbon"
    },
    "Questiono 6": {
    "Question" : "What is the capital of Australia?",
    "answer": "Vienna"
    }
}

score = 0

for key,value in Quiz.items():
    print(value["Question"])
    answer = input("Answer ->")

    if (answer.lower()==value["answer"].lower()):
        print("Correct")
        score = score+1
        print("Your Score is ::"+ str(score))
        print("")
        print("")

    else:
        print("Wrong Answer")
        print("The Answer is ::"+value["answer"])
        print("Your Score is::"+str(score))
        print("")

print("You got"+str(score)+"out of 7 Question correctly")
print("YOur Percentage is :"+str(int(score/7*100))+"%")