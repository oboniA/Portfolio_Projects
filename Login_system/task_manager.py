# ====Login Section====
# open and read user.txt file
# split the contains where comma+1space present
import os

global username_input

with open('user.txt', 'r+') as user_text:
    text_lines = user_text.readlines()

# adding text file data into a dictionary
# remove whitespace using .strip()
user_dict = {}  # dictionary
for each_line in text_lines:
    data = each_line.split(',')
    keys = data[0].strip()
    values = data[1].strip()
    user_dict[keys] = values

login = False
while not login:
    username_input = input("USERNAME: ")
    password_input = input("PASSWORD: ")

    # login is true only when both username and password match with user.txt
    if username_input in user_dict:
        if user_dict[username_input] == password_input:
            print("LOGIN SUCCESSFUL")
            login = True
        else:
            print("PASSWORD INCORRECT! TRY AGAIN\n")
            login = False
    else:
        print("USERNAME OR PASSWORD IS NOT VALID. TRY AGAIN\n")
        login = False


# Register user
def reg_user():
    # user input for registration details
    # open user.txt to write the new user info
    # written in the file when password re-entering is correct
    with open('user.txt', 'a+') as user_txt:
        while True:
            user_input = input("Enter a new username: ")
            if user_input in user_dict.keys():
                print("User name already exists, Try again with a different username!")
            else:
                pass_word_input = input("Enter a password: ")
                pass_confirm = input("re-enter your password: ")
                if pass_word_input != pass_confirm:
                    print("Password did not match!\nTry again\n")
                else:
                    user_txt.write('\n' + user_input)
                    user_txt.write(', ')
                    user_txt.write(pass_word_input)
                    print("USER REGISTRATION SUCCESSFUL\n")
                    print("\n-----BACK TO MAIN MENU-----\n")
                    break


# Adding a task
def add_task():
    with open('tasks.txt', 'a+') as task_file1:
        name_user = input("The task is assigned to ")
        task_title = input("Title of the task is ")
        description = input("Description: ")
        assign_date = input("enter assigned date: ")
        due_date = input("Enter the due date: ")
        complete = input("Completed?(Yes/No): ")

        # write user input to tasks.txt file
        task_file1.write('\n' + name_user)
        task_file1.write(
            ", " + task_title + ", " + description + ", " + assign_date + ", " + due_date + ", " + complete)


# View all tasks
def view_all():
    # open tasks.txt to read its data
    # lines of text made into a list
    # each line stripped to separate list items
    with open('tasks.txt', 'r') as task_file2:

        # items of each task_list item is split where comma+space present
        task_list = [line.strip() for line in task_file2]
        for item in range(len(task_list)):
            item_split = task_list[item].split(', ')

            print(f"\nTask:                 {item_split[1]}"
                  f"\nAssigned to:          {item_split[0]}"
                  f"\nDate assigned:        {item_split[3]}"
                  f"\nDue date:             {item_split[4]}"
                  f"\nTask complete:        {item_split[5]}"
                  f"\nTask Description:"
                  f"\n\t{item_split[2]}")

        print("\n-----BACK TO MAIN MENU-----\n")


# View my task
# reference: https://stackoverflow.com/questions/60971143/changing-the-correct-object-in-the-text-file ;
# https://stackoverflow.com/questions/62959549/how-to-read-items-in-a-text-file-and-overwrite-it-based-on-the-users-inputs
def view_mine():
    # Easy to read the user tasks
    def view_tasks():
        with open('tasks.txt', 'r') as file3:
            ck = 0
            for items in file3:
                user_task = items.strip().split(', ')
                if user_task[0] == username_input:  # split_list column 0
                    ck += 1
                    print(f"\nTask {ck}:            {user_task[1]}"
                          f"\nAssigned to:          {user_task[0]}"
                          f"\nDate assigned:        {user_task[3]}"
                          f"\nDue date:             {user_task[4]}"
                          f"\nTask complete:        {user_task[5]}"
                          f"\nTask Description:"
                          f"\n\t{user_task[2]}")

    view_tasks()

    # ---------------Operation Code---------------
    with open('tasks.txt') as f:
        i = 0
        user_tasks_list = []

        lines = f.read().splitlines()
        for db_row, line in enumerate(lines):
            assigned_to, *rest = line.split(', ')
            if assigned_to == username_input:
                # use a dictionary to easily refer to the current task field
                # i+1 = index0 turned to index1
                user_data = {k: v for k, v in zip(('User Task No', 'System task', 'Assigned to', 'Task', 'Description',
                                                   'Date assigned', 'Due date', 'Task Complete?'),
                                                  (i + 1, db_row, assigned_to, *rest))}
                user_tasks_list.append(user_data)
                i += 1
        # print(userTasks_list)

        # -------------------------------task inputs-----------------------------------
        task_operation = input('''\nEdit a task from above or return to the menu:
                          (tk) - choose task"
                          -1 - return to the menu"
                          >>''')

        # -------------------------Conditional code-------------------------
        if task_operation == 'tk':
            choose_task = int(input("Enter the task number: "))
            current_task = user_tasks_list[choose_task - 1]
            edit_complete = input('''\nmark task as complete or edit it:
                                mk - mark task
                                ed - edit task
                                >>''')
            if edit_complete == 'ed':
                if current_task['Task Complete?'] == 'No':
                    edit = input('''What would you like to edit:
                                             u - username
                                             dt - due date\n''')
                    if edit == "u":
                        current_task['Assigned to'] = input("Assign new username: ")
                        print("\nCHANGE SAVED!")
                    elif edit == 'dt':
                        current_task['Due date'] = input("Change due date: ")
                        print("\nCHANGE SAVED!")
                else:
                    print("The task is complete already. Can not be changed")
            elif edit_complete == 'mk':
                current_task['Task Complete?'] = 'Yes'
                print("\nCHANGE SAVED!")

        elif task_operation == "-1":
            print("Returning to main menu.......")
        else:
            print("Invalid selection! Try again!")

        print("\n-----BACK TO MAIN MENU-----\n")

    # ----------------------File writing----------------------------
    username_rows = [current_task['System task'] for current_task in user_tasks_list]
    with open('tasks.txt') as f, open('temp.txt', 'w') as temps:
        for db_row, line in enumerate(f):
            if db_row in username_rows:
                username_rows.remove(db_row)
                print(', '.join(v for k, v in list(user_tasks_list.pop(0).items())[2:]), file=temps)
            else:
                print(line.strip(), file=temps)

    os.remove('tasks.txt')
    os.rename('temp.txt', 'tasks.txt')


# Statistics for the admin user
def display_stats():
    print("DISPLAY STATISTICS:")
    # counts the total number of users
    with open('user.txt', 'r+') as user_file:
        read_user = user_file.readlines()
        print("Total number of users: ", len(read_user))

    # counts the total number of tasks
    with open('tasks.txt', 'r') as task_file:
        read_task = task_file.readlines()
        print("Total number of tasks: ", len(read_task))

    print("\n-----BACK TO MAIN MENU-----\n")

    '''
    with open('user_overview.txt', 'r+') as uo_file:
    read_user = uo_file.readlines()
    print('User_overview:')
    for i in read_user:
        print(i, end='')
    '''


# Generate Reports
def gen_report():
    from datetime import datetime

    # generates task_overview file after code termination
    def task_overview_text():
        with open('tasks.txt', 'r') as task_file:
            # total number of tasks
            read_task = task_file.readlines()

        with open('task_overview.txt', 'w+') as tsk:
            # Completed, uncompleted and overdue tasks
            today_date = datetime.today().strftime('%Y-%m-%d')
            task_list = [(line.strip().split(", ")) for line in read_task]
            complete_c = 0
            incomplete_c = 0
            overdue_c = 0
            for items in task_list:
                j_date = datetime.strptime(items[4], '%d %b %Y').strftime('%Y-%m-%d')
                if items[-1] == 'Yes':
                    complete_c += 1
                else:
                    incomplete_c += 1
                    i_percent = round((incomplete_c * 100) / len(read_task), 2)
                    if today_date > j_date:
                        overdue_c += 1
                        o_percent = round((overdue_c * 100) / len(read_task), 2)

            tsk.write('Total number of tasks: ' + str(len(read_task)))
            tsk.write('\nCompleted task: ' + str(complete_c))
            tsk.write('\nUncompleted task: ' + str(incomplete_c))
            tsk.write('\nOverdue task: ' + str(overdue_c))
            tsk.write('\nIncomplete Percentage: ' + str(i_percent) + '%')
            tsk.write('\nOverdue Percentage: ' + str(o_percent) + '%')

    # generates user_overview file after code termination
    def user_overview_text():
        with open('user.txt', 'r') as user_file:
            # total number of users
            read_user = user_file.readlines()
            user = [(u.strip().split(', ')) for u in read_user]  # users+password list

            user_list = [uu[0] for uu in user]  # list with only usernames

        with open('tasks.txt', 'r') as task_file2:
            # total number of tasks
            read_task2 = task_file2.readlines()
            task_list = [(item.strip().split(', ')) for item in read_task2]  # all the tasks 2D list

        with open('user_overview.txt', 'w+') as usr:
            usr.write('Total number of tasks: ' + str(len(read_task2)))
            usr.write('\nTotal number of users registered: ' + str(len(read_user)))
            usr.write('\n')

            for ux in user_list:
                print('\n')
                usr.write('\nUSER: ' + ux)
                count_u = 0
                for ix in sorted(task_list):
                    if ux == ix[0]:
                        count_u += 1
                usr.write('\nTotal tasks: ' + str(count_u))
                user_percent = round((count_u * 100) / len(task_list), 2)
                usr.write('\nPercentage of total task: ' + str(user_percent) + '%')

                c = [ix for ix in sorted(task_list) if ux == ix[0]]
                c_complete = 0
                c_incomplete = 0
                c_overdue = 0
                for item in c:

                    today_date = datetime.today().strftime('%Y-%m-%d')
                    d_list = datetime.strptime(item[4], '%d %b %Y').strftime('%Y-%m-%d')

                    if item[-1] == 'No':
                        c_incomplete += 1
                        incomplete_percent = round((c_incomplete * 100) / count_u, 2)

                        if today_date > d_list:
                            c_overdue += 1
                            overdue_percent = round((c_overdue * 100) / count_u, 2)

                    elif item[-1] == 'Yes':
                        c_complete += 1
                        complete_percent = round((c_complete * 100) / count_u, 2)

                # Complete
                if c_complete > 0:
                    usr.write('\nPercentage of completed tasks: ' + str(complete_percent) + '%')
                else:
                    usr.write('\nPercentage of completed tasks: 0%')

                # Incomplete
                if c_incomplete > 0:
                    usr.write('\nPercentage of uncompleted tasks: ' + str(incomplete_percent) + '%')
                else:
                    usr.write('\nPercentage of uncompleted tasks: 0%')

                # Overdue
                if c_overdue > 0:
                    usr.write('\nPercentage of Overdue tasks: ' + str(overdue_percent) + '%')
                else:
                    usr.write('\nPercentage of overdue tasks: 0%')

                usr.write('\n')

    task_overview_text()
    user_overview_text()
    print("\nThe reports will be generated after you Sign out!\nIf you wish to see the reports now, select 'e' at the main menu")
    print("\n-----BACK TO MAIN MENU-----\n")


# Main Code-Body
while True:
    # main menu list modified
    # user input is converted to lower case.
    # condition added to the username input
    if username_input == 'admin':
        menu = input('''Select one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - View my task
                gr - Generate reports
                ds - Display statistics
                e - Exit
                : ''').lower()

        # Registering a user
        if menu == 'r':
            reg_user()

        # Adding task
        elif menu == 'a':
            add_task()

        # View all tasks
        elif menu == 'va':
            view_all()

        # View my task
        elif menu == 'vm':
            view_mine()

        # Display statistics
        elif menu == 'ds':
            display_stats()

        # Generate Reports
        elif menu == 'gr':
            gen_report()

        # Exit
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # Wrong selection
        else:
            print("\nTHIS OPTION IS AVAILABLE ONLY TO THE ADMIN\n")

    else:
        menu = input('''Select one of the following Options below:
                a - Adding a task
                va - View all tasks
                vm - View my task
                gr - Generate reports
                e - Exit
                : ''').lower()
        # Adding task
        if menu == 'a':
            add_task()

        # View all tasks
        elif menu == 'va':
            view_all()

        # View Logged-in user's task
        elif menu == 'vm':
            view_mine()

        # Generate Reports
        elif menu == 'gr':
            gen_report()

        # Exit
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # Wrong selection
        else:
            print("\nTHIS OPTION IS AVAILABLE ONLY TO THE ADMIN\n")
