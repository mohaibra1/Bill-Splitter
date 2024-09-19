# write your code here
import random
print('Enter the number of friends joining (including you):')
number_of_invitees = int(input())
invited_friends = {}
friends_list = []
if number_of_invitees <= 0:
    print('No one is joining for the party')
else:
    for invited in range(0, number_of_invitees):
        name_invited = input()
        friends_list.append(name_invited)
        invited_friends[name_invited] = 0
    print('Enter the total bill value:')
    total_bill = int(input())
    split_the_bill = total_bill/len(invited_friends)
    for split in invited_friends.keys():
        invited_friends[split] = round(split_the_bill,2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input().lower()
    if choice == 'yes':
        random.seed()
        generate_num = random.randrange(0, len(friends_list))
        lucky_one = friends_list[generate_num]
        print(f'{lucky_one} is the lucky one!')
        recalculate_dict = {key:round(total_bill/(len(invited_friends)-1)) for key in invited_friends}
        recalculate_dict[lucky_one] = 0
        print(recalculate_dict)
    else:
        print('No one is going to be lucky')
        print(invited_friends)