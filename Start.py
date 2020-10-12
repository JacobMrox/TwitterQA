# This imports arguments from config.py as defined below and passes them
from chatbot import chatbot
from chatbot_twitter import chatbot_twitter
from config import *
import nltk
nltk.download('punkt')

if default_option == 1:
    # Load the class with variables imported from config
    print("Training bot with default options")

else:
    print("Select an option:")
    print("1 : Train with default options (e.g. provided datasets Cornell, etc...)")
    print("2 : Train with a Twitter user tweets")
    print("3 : Run specific bot model (offline)")

while True:
    in_pick = float(input("Select an option: "))

    if in_pick == 1:
        answer = str(input("Would you like to provide a name for your bot model? "))
        if answer == "Yes, Y, yes":
            bot = main_default (self, args.modelTag == model_name)
            bot.run()
            break
        else:
            if __name__ == "__main__":
                chatbot = chatbot.Chatbot()
            chatbot.main()
            break

    elif in_pick == 2:
        print("Function not implemented yet!!")
        continue
		#bot = program_y_class(channel_name, bot_token)
		#bot.run()
		#break

    elif in_pick == 3:
        print("Function not implemented yet!!")
        continue
        #bot = tensorflow_class(channel_name, bot_token)
        #bot.run()

    else:
        print("That's not an option.")
        continue

        p.wait()
