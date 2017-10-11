from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import incl
import random


# Instance of chatbot
chatbot = ChatBot(
    'Charlie',      # Name of bot

    # Logical Adapters
    logic_adapters=[

        # Low Confidence Threshold
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.30,
            'default_response': 'I am sorry but I don\'t understand'
        },
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'
    ],

)

# chatbot.set_trainer(ListTrainer)
#
# chatbot.train([
#     "Hello!",
#     "Hi there! How are you?",
#     "I am quite well, thanks for asking. How about you?",
#     "That is so nice to hear! :)"
# ])

while True:

    # User Input
    user_input = str(input('> ')).lower()

    # Loop Exit
    for i in incl.goodbye:
        if i in user_input:
            print(incl.goodbye[random.randint(0, len(incl.goodbye) - 1)])
            incl.db.close()
            quit()

    # Store chatbot response to user_input in variable called 'response'
    response = chatbot.get_response(user_input)

    print(response)

    # Insert user message and bot response into table
    incl.cursor.execute('''INSERT INTO log_table(user_message, bot_response)
                  VALUES(?, ?)''', (user_input, str(response)))

    # Commit changes to database
    incl.db.commit()


