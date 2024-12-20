registered_user={"user1@gmai.com","user2@gmai.com","user3@gmai.com"}
active_user={"user2@gmai.com","user3@gmai.com","user4@gmai.com"}
print('registered_user',registered_user)
print('active_user',active_user)
common_user=registered_user&active_user
print('common user(both registered and active):',common_user)
inactiveRegistered=registered_user-active_user
print('inactive Registered user:',inactiveRegistered)
unregisteredActive=active_user-registered_user
print('active but not registered:',unregisteredActive)
