import loops as f#imports our docs that we defined, and we can define a library to import. The as keyword renames it for this file.
from functionz import average, x #imports only the average function and variable x in functionz document
print(average(1,2))#yu can directly call average function now.
print(x)

import platform#a pre-defined python module from someone else. platform is a module that is relating to the user's os, system, etc.
print(f.listVar2)#calls our functionz factorial method. You can also use the same format to call variables
print(platform.system())#calls the platform system method, which tells us which system te user is using.
