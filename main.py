import os
import logging
import time
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_ERROR_VERBOSITY"] = "NONE"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"



logging.getLogger("absl").setLevel(logging.ERROR)



from specs import get_system_specs
from gemini_client import ask_gemini

def run_chatbot():
    print("System Assistant Chatbot (type 'exit' to quit)\n")

    last_topic = None

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "exit!", "quit!"]:
            print("Bot: Goodbye! 👋")
            break

        specs, current_topic = get_system_specs(user_input, last_topic)
        last_topic = current_topic or last_topic  # update last topic

        answer = ask_gemini(user_input, specs)
        print("Bot:", answer)

if __name__ == "__main__":
    run_chatbot()
