# TINGIMUSLAUSED / IF STATEMENTS

########age_restriction##### parooli kontroll #################

password_in_database = 'kiisuke123'
username_database = 'kiisuke'

username = input("username:\n:")
user_input_password = input("password:\n:") 

if password_in_database == user_input_password: # tingimuslause, tingimus on et paroolid oleksid samad
    print('logging in')


################# vanuse kontroll: 1 variant ##################

age_restriction = 18
user_age = input('insert age:')
if int(user_age) >= age_restriction: #  nõue et vanus oleks 18 või rohkem
    print('suur poiss')

if int(user_age) <= age_restriction: #  mis siis kui vanus on alla 18
    print('vara veel poju')

############### tingimuslause #################

if True:   # if vajab alati boolean väärtust, kas true või false.
    print('see asi prinditakse välja')

if False:
    print('seda ei prindia välja')

if True and True:   # kui on 2 tingimust, mis peavad olema täidetud
    print('seda ei prindita välja')
# nt: if username_database == username_sisestatud and pw_database == pw_sisestatud.
if True and False: 
    print('seda ei prindita välja')  # kui üks tingimus on täitmata, nt vanus või parool on vale.

    #### näide #####

if username == 'kiisuke' and user_input_password == password_in_database:
    print('logid sisse')  # prindib ainult siis kui mõlemad on õiged.

######## tingimuslause

if True or False: 
    print('see prinditakse välja')  ## Üks tingimustest peab olema täidetud ja siis OK

if False or False: 
    print('seda ei prindita välja') ### üks tingimustest peab olema täidetud, aga pole kumbki


passenger_age = int(input('sisesta reisija vanus:'))
parent_present = input('kas emme on kaasas? (jah/ei):')




if passenger_age >= age_restriction or parent_present == 'jah':
    print('tulge aga peale')
else: ### kõik eelnevad tingimused pole täidetud.
    print('ei tohi peale tulla')

min_points_4success = 51
user_course_points =int(input('sisesta oma kursuse punktid:'))

if user_course_points >= 91:
    print('hinne 5')
elif user_course_points >= 81:
    print('hinne 4')
elif user_course_points >= 71:
    print('hinne 3')
elif user_course_points >= 50:
    print('hinne 2')
elif user_course_points >= 30:
    print('hinne 1')

else:
    print('tubli poiss, jääd suvetööle')







