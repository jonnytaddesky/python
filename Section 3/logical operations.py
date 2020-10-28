if True:
    print('Indeed, true.')


if 3 > 2:
    print('3 is greater than 2')


if 3 < 2:
    print('3 is less than 2')


is_admin = True
if is_admin :
    print("It's admin, look at him!")


selected_character = input()

if selected_character == "Protos":
    print('Protos is the most powerful race')
elif selected_character == "Zerg":
    print('Zerg is the most weak race but it spreads like a plague')
elif selected_character == "Terrain":
    print('Terrain is the race balance between Zerg and Protos')
else:
    print('Hmm... it seems we have a new race.')
