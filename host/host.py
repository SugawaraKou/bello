from tools import config, connections

username = config.get_username()
print "Welcome to Bello %s" % username

connections.listen(username)






