# Import
# import module_name
#import printing_functions

# from module_name import function_name
#from printing_functions import print_models
#from printing_functions import show_completed_models

# from module_name import function_name as fn
#from printing_functions import print_models as pm
#from printing_functions import show_completed_models as cm

# import module_name as mn
#import printing_functions as pf

# from module_name import *
from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#printing_functions.print_models(unprinted_designs, completed_models)
#printing_functions.show_completed_models(completed_models)

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

#pm(unprinted_designs, completed_models)
#cm(completed_models)

#pf.print_models(unprinted_designs, completed_models)
#pf.show_completed_models(completed_models)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)