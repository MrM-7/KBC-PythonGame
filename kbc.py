choice = input("Do you want to play KBC??\nyes or no: ")
choice = choice.lower()

questions = [
    [
        "The International Literacy Day is observed on ?", "Sep 8",
        "Nov 28", "May 2", "Sep 22"
    ],
    [
        "The language of Lakshadweep a Union Territory of India, is", "Tamil",
        "Hindi", "Malayalam", "Telugu"
    ],
    [
        "Bahubali festival is related to", "Islam", "Hinduism", "Buddhism",
        "Jainism"
    ],
    [
        "Which day is observed as the World Standards  Day?", "June 26",
        "Oct 14", "Nov 15", "Dec 2"
    ],
    [
        "Which of the following was the theme of the World Red Cross and Red Crescent Day?"
        , "'Dignity for all - focus on women'", "Dignity for all - focus on Children'"
        , "Focus on health for all", "Nourishment for all-focus on children"
    ],
    [
        "September 27 is celebrated every year as"
        , "Teachers' Day", "National Integration Day", "World Tourism Day",
        "International Literacy Day"
    ],
    [
        "Who is the author of 'Manas Ka-Hans' ?", "Khushwant Singh",
        "Prem Chand", "Jayashankar Prasad", "Amrit Lal Nagar"
    ],
    [
        "The death anniversary of which of the following leaders is observed as Martyrs' Day?",
        "Smt. Indira Gandhi", "PI. Jawaharlal Nehru", "Mahatma Gandhi", "Lal Bahadur Shastri"
    ],
    [
        "Who is the author of the epic 'Meghdoot ?",
        "Vishakadatta", "Valmiki", "Banabhatta", "Kalidas"
    ],
    [
        "Good Friday' is observed to commemorate the event of",
        "birth of Jesus Christ", "birth of' St. Peter", "crucification 'of Jesus Christ", "rebirth of Jesus Christ"
    ],
    [
        "Who is the author of the book 'Amrit Ki Ore'?",
        "Mukesh Kumar", "Narendra Mohan", "Upendra Nath", "Nirad C. Choudhary"
    ],
    [
        "Which of the following Muslim festivals is based on the 'Holy Quran' ?",
        "Id -ul-Zuha", "Id -ul-Zuha", "Bakri-id", "Moharram"
    ],
    [
        "Van Mahotsav was started by",
        "Maharshi Karve", "Bal Gangadhar Tiiak", "K.M, Munshi", "Sanjay Gandhi"
    ],
    [
        "The first month of the Indian national calendar is",
        "Magha", "Chaitra", "Ashadha", "Vaishakha"
    ],
    [
        "Which of the following is not a dance from Kerala?",
        "Kathakali", "Mohiniattam", "Ottan Thullal", "Yaksha Gana"
    ]
]

answers = ["1", "3", "4", "2", "2", "3", "4", "3", "4", "3", "2", "1", "3", "2", "4"]
price = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000,
         10000000]


def game():
    checkpoint_amount = 0

    for i in range(15):
        print(f"\nQuestion {i + 1} for Rs.{price[i]}")
        print(questions[i][0])
        print(f"1. {questions[i][1]}\t2. {questions[i][2]}")
        print(f"3. {questions[i][3]}\t4. {questions[i][4]}")
        ans = input("Ans: ")

        if ans == answers[i]:
            print("\nCorrect !!!")

            if i == 14:
                print("Congratulations You won Rs. 1,00,00,000 !!!!")
                break

            print(f"You Won Rs. {price[i]}")
            if i == 4 or i == 9:
                checkpoint_amount = price[i]

        elif ans == "Quit" or ans == "quit":
            if i == 0:
                print("Your total amount is Rs. 0")
                break
            else:
                print("Your total amount is : Rs. ", price[i - 1])
                break
        else:
            print("\nWrong Answer :(")
            print("Your total amount is : Rs. ", checkpoint_amount)
            break


def welcome():
    print("-----------Welcome-----------")
    print("There are total 15 questions in this game.")
    print("We'll start from question 1 worth Rs. 1000 till question 15 worth Rs. 1 Cr")
    print("We have checkpoints on question 5(Rs. 10,000), 10(Rs. 3,20,000)")
    print("You can quit the game on any question just write 'Quit' on the answer section of that question)")
    print("-----------------------------")
    try:
        ch = int(input("Enter 1 to start game: "))

    except Exception as e:
        print(e)
        return

    match ch:
        case 1:
            game()
        case _:
            print("Wrong Choice!!")


match choice:
    case "yes":
        welcome()
    case "no":
        print("Bye!!")
    case _:
        print("Wrong choice!!")
