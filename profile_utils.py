import json

def load_profiles(filename):
    try:
        with open(filename, "r") as file:
            profiles = json.load(file)
            return profiles
    except FileNotFoundError:
        return {}

def save_profiles(profiles, filename):
    with open(filename, "w") as file:
        json.dump(profiles, file)

def add_profile(profile_name, profile_data, profiles):
    profiles[profile_name] = profile_data

def get_profile(profile_name, profiles):
    return profiles.get(profile_name, None)

