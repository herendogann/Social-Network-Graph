import sys
smn_argv = sys.argv[1]
commands_argv = sys.argv[2]

smn_dict = {}
common_friends = {}

with open(smn_argv, "r", encoding="utf-8") as smn:
    smn_lines = smn.read().splitlines()
    for line in smn_lines:
        line = line.rstrip()
        user, friends_str = line.split(":")
        friends_list = friends_str.split(" ")
        smn_dict[user] = friends_list
        common_friends[user] = 0

    with open("output.txt", "w", encoding="utf-8") as output:
        output.write("Welcome to Assignment 3\n-------------------------------------------------------------\n")
        with open(commands_argv, "r", encoding="utf-8") as commands:
            command = commands.read().splitlines()
            for a in range(len(command)):
                next_command = command[a].rstrip()

                if next_command.startswith("ANU"):
                    anu, username = next_command.split(" ")
                    if username in smn_dict:
                        output.write("ERROR: Wrong input type for ANU! -- User '" + username + "' already exists.\n")
                    elif username not in smn_dict:
                        smn_dict[username] = []
                        common_friends[username] = 0
                        output.write("User '" + username + "' has been added to the social network successfully.\n")

                if next_command.startswith("DEU"):
                    deu, username = next_command.split(" ")
                    if username in smn_dict:
                        smn_dict.pop(username)
                        common_friends.pop(username)
                        for user in smn_dict:
                            if username in smn_dict[user]:
                                smn_dict[user].remove(username)
                        output.write("User '" + username +
                                     "' and his/her all relations have been deleted successfully.\n")
                    elif username not in smn_dict:
                        output.write("ERROR: Wrong input type for DEU! -- There is no user named '" + username + "'.\n")

                if next_command.startswith("ANF"):
                    anf, username1, username2 = next_command.split(" ")
                    if username1 and username2 not in smn_dict:
                        output.write("ERROR: Wrong input type for ANF! -- No user named '"
                                     + username1 + "' and '" + username2 + "' found.\n")
                    elif username1 not in smn_dict:
                        output.write("ERROR: Wrong input type for ANF! -- No user named '" + username1 + "' found.\n")
                    elif username2 not in smn_dict:
                        output.write("ERROR: Wrong input type for ANF! -- No user named '" + username2 + "' found.\n")

                    elif username1 and username2 in smn_dict:
                        if username1 in smn_dict[username2] and username2 in smn_dict[username1]:
                            output.write("ERROR: A relation between '" + username1 +
                                         "' and '" + username2 + "' already exists.\n")
                        else:
                            smn_dict[username1].append(username2)
                            smn_dict[username2].append(username1)
                            output.write("Relation between '" + username1 + "' and '"
                                         + username2 + "' has been added successfully.\n")

                if next_command.startswith("DEF"):
                    df, username1, username2 = next_command.split(" ")
                    if username1 and username2 not in smn_dict:
                        output.write("ERROR: Wrong input type for DEF! -- No user named '"
                                     + username1 + "' and '" + username2 + "' found.\n")
                    elif username1 not in smn_dict:
                        output.write("ERROR: Wrong input type for DEF! -- No user named '" + username1 + "' found.\n")
                    elif username2 not in smn_dict:
                        output.write("ERROR: Wrong input type for DEF! -- No user named '" + username2 + "' found.\n")

                    elif username1 and username2 in smn_dict:
                        if username1 in smn_dict[username2] and username2 in smn_dict[username1]:
                            smn_dict[username1].remove(username2)
                            smn_dict[username2].remove(username1)
                            output.write("Relation between '" + username1 + "' and '" +
                                         username2 + "' has been deleted successfully.\n")
                        else:
                            output.write("ERROR: No relation between '"
                                         + username1 + "' and '" + username2 + "' found.\n")

                if next_command.startswith("CF"):
                    cf, username = next_command.split(" ")
                    if username not in smn_dict:
                        output.write("ERROR: Wrong input type for CF! -- No user named '" + username + "' found.\n")
                    else:
                        output.write("User '" + username + "' has " + str(len(smn_dict[username])) + " friends.\n")

                if next_command.startswith("FPF"):
                    fpf, username, max_distance = next_command.split(" ")
                    possible_friends_list = []
                    if username not in smn_dict:
                        output.write("ERROR: Wrong input type for FPF! -- No user named '" + username + "' found.\n")
                    else:
                        if not 1 <= int(max_distance) <= 3:
                            output.write("ERROR: Wrong input type for FPF! -- "
                                         "Max distance is out of range. Must be between 1 and 3.\n")
                        elif int(max_distance) == 1:
                            for friend in smn_dict[username]:
                                possible_friends_list.append(friend)
                                possible_friends_set = set(possible_friends_list)
                            output.write("User '" + username + "' has " + str(len(possible_friends_set)) +
                                         " possible friends when maximum distance is " + max_distance + ".\n")
                            output.write("These possible friends: {" +
                                         ", ".join("'" + x + "'" for x in sorted(possible_friends_set)) + "}\n")

                        elif int(max_distance) == 2:
                            for friend in smn_dict[username]:
                                possible_friends_list.append(friend)
                                possible_friends_list.sort()
                                for friend2 in smn_dict[friend]:
                                    possible_friends_list.append(friend2)
                                    if username in possible_friends_list:
                                        possible_friends_list.remove(username)
                                    possible_friends_set = set(possible_friends_list)
                            output.write("User '" + username + "' has " + str(len(possible_friends_set)) +
                                         " possible friends when maximum distance is " + max_distance + ".\n")
                            output.write("These possible friends: {" +
                                         ", ".join("'" + x + "'" for x in sorted(possible_friends_set)) + "}\n")

                        elif int(max_distance) == 3:
                            for friend in smn_dict[username]:
                                possible_friends_list.append(friend)
                                possible_friends_list.sort()
                                for friend2 in smn_dict[friend]:
                                    possible_friends_list.append(friend2)
                                    if username in possible_friends_list:
                                        possible_friends_list.remove(username)
                                    possible_friends_set = set(possible_friends_list)
                                    for friend3 in smn_dict[friend2]:
                                        possible_friends_list.append(friend3)
                                        if username in possible_friends_list:
                                            possible_friends_list.remove(username)
                                        possible_friends_set = set(possible_friends_list)
                            output.write("User '" + username + "' has " + str(len(possible_friends_set)) +
                                         " possible friends when maximum distance is " + max_distance + ".\n")
                            output.write("These possible friends: {" +
                                         ", ".join("'" + x + "'" for x in sorted(possible_friends_set)) + "}\n")

                if next_command.startswith("SF"):
                    sf, username, MD = next_command.split(" ")
                    if username not in smn_dict:
                        output.write("ERROR: Wrong input type for SF! -- No user named '" + username + "' found.\n")
                    elif not 2 <= int(MD) <= 3:
                        output.write("ERROR: Wrong input type for SF! -- MD is out of range, must be 2 or 3.\n")
                    elif username in smn_dict:
                        if int(MD) == 2:
                            suggested_friends1 = []
                            output.write("Suggestion List for '" + username + "' (When MD is 2):\n")
                            for friend in smn_dict[username]:
                                for user in smn_dict.keys():
                                    if friend in smn_dict[user]:
                                        common_friends[user] += 1
                            for user in common_friends:
                                if common_friends[user] == 2 and user != username:
                                    suggested_friends1.append(user)
                                    output.write("'" + username + "' has 2 mutual friends with '" + user + "'.\n")
                            for user in common_friends:
                                if common_friends[user] == 3 and user != username:
                                    suggested_friends1.append(user)
                                    output.write("'" + username + "' has 3 mutual friends with '" + user + "'.\n")
                            output.write("The suggested friends for '" + username + "': " +
                                         ",".join("'" + a + "'" for a in suggested_friends1) + "\n")
                            for user in common_friends:
                                common_friends[user] = 0

                        if int(MD) == 3:
                            suggested_friends2 = []
                            output.write("Suggestion List for '" + username + "' (When MD is 3):\n")
                            for friend in smn_dict[username]:
                                for user in smn_dict.keys():
                                    if friend in smn_dict[user]:
                                        common_friends[user] += 1
                            for user in common_friends:
                                if common_friends[user] == 3 and user != username:
                                    suggested_friends2.append(user)
                                    output.write("'" + username + "' has 3 mutual friends with '" + user + "'.\n")
                            output.write("The suggested friends for '" + username + "': " +
                                         ",".join("'" + a + "'" for a in suggested_friends2) + "\n")
                            for user in common_friends:
                                common_friends[user] = 0
