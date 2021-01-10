import json

def show_profile():
    profile_data = json.loads(open('profile.json',).read())

    print("")
    print(profile_data["username"] + ',')
    print("Current Balence: " + profile_data["current-balence"])
    print("---Portfolio---")
    print("")
    print(profile_data["having"])
