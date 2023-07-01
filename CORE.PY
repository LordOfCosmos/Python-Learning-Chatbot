import json
import profile_utils

# Load prompts and answers from a file
def load_data():
    try:
        with open("chatbot_data.json", "r") as file:
            data = json.load(file)
            prompts = data["prompts"]
            answers = data["answers"]
            return prompts, answers
    except FileNotFoundError:
        return [], []

# Save prompts and answers to a file
def save_data(prompts, answers):
    data = {"prompts": prompts, "answers": answers}
    with open("chatbot_data.json", "w") as file:
        json.dump(data, file)

# Reset prompts and answers
def reset_data():
    global prompts, answers
    prompts = []
    answers = []
    save_data(prompts, answers)

# Load user profiles from a file
def load_profiles():
    try:
        with open("user_profiles.json", "r") as file:
            profiles = json.load(file)
            return profiles
    except FileNotFoundError:
        return {}

# Save user profiles to a file
def save_profiles(profiles):
    with open("user_profiles.json", "w") as file:
        json.dump(profiles, file)

# Load existing prompts, answers, and user profiles
prompts, answers = load_data()
profiles = load_profiles()

def save_data_to_file(prompts, answers, filename):
    data = {"prompts": prompts, "answers": answers}
    with open(filename, "w") as file:
        json.dump(data, file)

def save_profiles_to_file(profiles, filename):
    with open(filename, "w") as file:
        json.dump(profiles, file)



# Example usage
save_data_to_file(prompts, answers, "data_output.json")

# Initialize conversation context
context = {
    "user_inputs": [],
    "bot_responses": [],
    "user_profile": {}
}

# Chat loop
while True:
    user_input = input("User: ")

    # Add user input to conversation history
    context["user_inputs"].append(user_input)

    # Check if the user input is in prompts
    if user_input in prompts:
        # Get the corresponding answer
        index = prompts.index(user_input)
        response = answers[index]
        print("ChatBot: " + response)
        context["bot_responses"].append(response)

    elif user_input.lower() == "reset":
        reset_data()
        print("ChatBot: Conversation data has been reset.")
        context["user_inputs"] = []
        context["bot_responses"] = []
        context["user_profile"] = {}

    elif user_input.lower() == "add":
        print("ChatBot: Enter a new question:")
        new_question = input("User: ")
        print("ChatBot: Enter the answer to the question:")
        new_answer = input("User: ")
        prompts.append(new_question)
        answers.append(new_answer)
        save_data(prompts, answers)
        print("ChatBot: New question and answer have been added.")
        context["bot_responses"].append("ChatBot: New question and answer have been added.")

    elif user_input.lower() == "profile":
        profile_name = input("Enter profile name: ")
        profile_data = input("Enter profile data: ")
        profile_utils.add_profile(profile_name, profile_data, profiles)

    elif user_input.lower() == "get_profile":
        profile_name = input("Enter profile name: ")
        profile = profile_utils.get_profile(profile_name, profiles)
        if profile:
            print("Profile data: {}".format(profile))
        else:
            print("ChatBot: I don't have your name in the profile.")
            context["bot_responses"].append("ChatBot: I don't have your name in the profile.")
    else:
        print("ChatBot: Sorry, I'm not sure what you mean. Can you please rephrase or provide more information?")
        context["bot_responses"].append("ChatBot: Sorry, I'm not sure what you mean. Can you please rephrase or provide more information?")

    # Update context with conversation history
    context["user_inputs"] = context["user_inputs"][-5:]  # Keep only the last 5 user inputs
    context["bot_responses"] = context["bot_responses"][-5:]  # Keep only the last 5 bot responses
