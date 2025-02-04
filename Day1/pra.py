import json

def add_user():
    name = input('name:')
    skills = input('skills(split with ","):').split(',')
    user = {"name":name,"skills":skills}

    with open("user1.json") as f:
        data = json.load(f)
        data["users"].append(user)
        f.seek(0)
        json.dump(data,f,indent = 2)

def find_user():
    name = input("name:")
    with open("user1.json") as f:
        data = json.load(f)
        for user in data["user"]:
            if user["name"] == name:
                print(user)
                return
    print("NOT FOUND!")

def del_user():
    name = input("delete name:")
    with open("user1.json") as f:
        data = json.load(f)
        data["users"] = [user for user in data["users"] if user["name"] != name]
        f.seek(0)
        json.dump(data , f,indent = 2)
        f.truncate()

while True:
    print("\n1.add\n2.find\n3.del\n4.exit")
    choice = input("please choose:")
    if choice == "1":
        add_user()
    elif choice == '2':
        find_user()
    elif choice == "3":
        del_user()
    elif choice == '4':
        break