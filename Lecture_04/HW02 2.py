def insert (friends, count):
    for i in range(len(friends)):
        if count > friends[i][1]:
            return i
    return len(friends)

friends = [("다현", 200), ("정연", 150), ("쯔위", 90), ("사나", 30), ("지효", 15)]

name = input("추가할 친구 : ")
count = int(input("카톡 횟수 : "))

insert_index = insert(friends, count)
friends.insert(insert_index, (name, count))

print("친구 리스트:")
for friend in friends:
    print(friend[0], ":", friend[1], "회")
