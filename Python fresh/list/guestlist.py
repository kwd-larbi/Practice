# create a list of three people for this dinner invitation
guest_list = ['Pope', 'Bishop', 'Father']
# print each item in the list inviting everyone for dinner
print('Hello', guest_list[0], 'you are being invited to dinner this evening')
print('Hello', guest_list[1], 'you are being invited to dinner this evening')
print('Hello', guest_list[2], 'you are being invited to dinner this evening')
print('Pope cannot make it') # one cannot make it

# modify guest_list with a new person
guest_list[0] = 'City Kings'
# second invitation
print('\nHello', guest_list[0], 'you are being invited to dinner this evening')
print('Hello', guest_list[1], 'you are being invited to dinner this evening')
print('Hello', guest_list[2], 'you are being invited to dinner this evening')

# more guest on a  bigger table info
print('\nHey we have a bigger table this time around!')

guest_list.insert(0, 'Cardinals')# beginning
guest_list.insert(2, 'Deacons')#middle
guest_list.append('Ushers') # end
# test print(guest_list) output was ['Cardinals', 'City Kings', 'Deacons', 'Bishop', 'Priest', 'Ushers']
print('Hello', guest_list[0] + ',you are being invited to dinner this evening')
print('Hello', guest_list[1] + ',you are being invited to dinner this evening')
print('Hello', guest_list[2] + ',you are being invited to dinner this evening')
print('Hello', guest_list[3] + ',you are being invited to dinner this evening')
print('Hello', guest_list[4] + ',you are being invited to dinner this evening')
print('Hello', guest_list[5] + ',you are being invited to dinner this evening')

# shrinking guest list
