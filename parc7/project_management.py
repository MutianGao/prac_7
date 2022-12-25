from parc7.project import Project
import datetime

MENU = "- (L)oad projects" \
       "- (S)ave projects" \
       "- (D)isplay projects" \
       "- (F)ilter projects by date" \
       "- (A)dd new project" \
       "- (U)pdate project " \
       "- (Q)uit"

projects = []
incomplete_projects = []
completed_projects = []

print(MENU)
choice = input(">>> ").lower()

while choice != "q":

    if choice == "d":  # X
        for Completion_level in projects:
            if Completion_level.completion >= 100:  # higher than 100% is done
                completed_projects.append(Completion_level)
            else:
                incomplete_projects.append(Completion_level)  # check Y/N done
        completed_projects.sort()
        incomplete_projects.sort()  # back

        print("Incomplete projects: ")
        for finish_n in incomplete_projects:  # （n）o part
            print(finish_n)
        print("Completed projects: ")
        for finish_y in completed_projects:  # （y）es part
            print(finish_y)

    elif choice == "f":  # X
        date_input = input("Show projects that start after date (dd/mm/yyyy): ")  # get date
        date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
        print(date.strftime("%d/%m/%Y"))

    elif choice == "a":  # X
        updata_project_name = input("Enter new project name: ")
        updata_project_date = input("Start date (dd/mm/yy):")
        updata_project_priority = input("Priority: ")
        updata_project_cost = input("Cost estimate: $")
        updata_project_complete = input("Percent complete: ")
        # get new data
        new_project = Project(updata_project_name, updata_project_date, updata_project_priority, updata_project_cost,
                              updata_project_complete)
        projects.append(new_project)  # updata

    elif choice == "u":  # X
        for i, project in enumerate(projects, 0):  # 计数器 Counters（enumerate）
            print(f"{i} {project}")

        number_choice = int(input("Project choice: "))  # get number/part and show
        print(projects[number_choice])

        new_percentage_number = int(input("New Percentage: "))  # new nuber change %/level
        new_priority_number = int(input("New Priority: "))

        projects[number_choice] = Project(projects[number_choice].name, projects[number_choice].start_date,
                                          new_priority_number, projects[number_choice].cost, new_percentage_number)
        # new number put in fild

    else:
        print("Invalid input")  # input not good
    print(MENU)
    choice = input(">>> ").lower()

print("Close, thank you")
