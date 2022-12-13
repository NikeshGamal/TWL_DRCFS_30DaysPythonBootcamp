# import constants 
# importing module directly

#if we want to import variable  from module 
from constants import CURRENT_MENTOR_COUNT,CURRENT_STUDENT_COUNT

# print(f"There are currently {constants.CURRENT_STUDENT_COUNT} number of participaints")
# print(f"There are currently {constants.CURRENT_MENTOR_COUNT} number of mentos")


#existing python module ko name hamile create gareko module ko name narakhni python will be confused-->najik ko lai rakhdinxa 
print(f"There are currently {CURRENT_STUDENT_COUNT} number of participaints")
print(f"There are currently {CURRENT_MENTOR_COUNT} number of mentos")