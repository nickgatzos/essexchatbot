import aiml
import os
import incl
import random

quit_list = ['goodbye', 'bye', 'see you', 'see you soon', 'cya', 'bb', 'ttyl', 'got to go', 'to go']

kernel = aiml.Kernel()


if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:

    # User input (transformed to lowercase)
    user_input = raw_input("> ").lower()

    # Exit loop
    for i in quit_list:
        if user_input in quit_list:
            print(quit_list[random.randint(0, len(quit_list) - 1)])
            quit()

    # Bot response to user input
    response = kernel.respond(user_input)
    print response

    # Insert user message and bot response into table
    incl.cursor.execute('''INSERT INTO log_table(user_message, bot_response)
                      VALUES(?, ?)''', (user_input, str(response)))

    # Commit changes to database
    incl.db.commit()
