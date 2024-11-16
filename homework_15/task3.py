friends = {}

while True:
    friendship_input = input("Enter friendship or 'FINISH' to stop: ")
    if friendship_input == "FINISH":
        break
    person1, person2 = friendship_input.split(" – ")
    if person1 not in friends:
        friends[person1] = []
    if person2 not in friends:
        friends[person2] = []
    friends[person1].append(person2)
    friends[person2].append(person1)


for person, friends_list in friends.items():
    print(f"{person} – {', '.join(friends_list)}")
