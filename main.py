# ---- Suppress gRPC, TensorFlow, and absl warnings ----
import os
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_ERROR_VERBOSITY"] = "NONE"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import sys
import logging
import time

# Suppress absl logs
logging.getLogger("absl").setLevel(logging.ERROR)



from specs import get_system_specs
from gemini_client import ask_gemini


def run_chatbot(refresh_interval=30):
    print("💻 System Assistant Chatbot (type 'exit' or 'quit' or 'bye' to quit)\n")

    last_refresh = 0
    cached_specs = {}

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        if time.time() - last_refresh > refresh_interval or not cached_specs:
            cached_specs = get_system_specs()
            last_refresh = time.time()

        answer = ask_gemini(user_input, cached_specs)
        print("Bot:", answer)

if __name__ == "__main__":
    run_chatbot(refresh_interval=30)
