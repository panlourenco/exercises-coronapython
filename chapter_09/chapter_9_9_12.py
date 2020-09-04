# 9-12. Multiple Modules:

from privileges import Privileges, Admin

admin = Admin('rodrigo','lourenco','krakow', 31)
admin.greet_user()
my_privileges = Privileges()
my_privileges.show_privileges()