# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, n =','):
    participants_list1 = participants1.split(n)
    participants_list2 = participants2.split(n)

    common_participants = list(set(participants_list1).intersection(participants_list2))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, n ='|')
print("Общие участники:", participants)
