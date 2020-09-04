# 9-11. Imported Admin:

from admin import Admin
from admin import Privileges

admin = Admin('rodrigo','lourenco', 'krakow', 31)
admin.greet_user()
privileges = Privileges()
privileges.show_privileges()