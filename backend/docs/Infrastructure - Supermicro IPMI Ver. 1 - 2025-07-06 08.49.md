## Supermicro IPMI Ver. 1 

# IPMI CFG. Password reset 

In order to reset the password on a Super micro brand server you will need to use an outside utility. The guide on super micro site no longer works on their new version of ipmicfg I have a premade utility on USB. Will be making a new one at a later date. For now this works. It is red and hanging on the cabinet key hooks. Please return there. USB is bootable. Once in you will see the following screen. -Select -"No Return to DOS once it drops you down to the prompt navigate to the folder containing the IPMI.CFG.EXE file Run "cd \FDOS-X86\FREEDOS\DOS" to list the folder contents Run "dir" You may see the following and as in image below shows the IPMICFG.EXE file. 

### 1. 

## Core Assets/Documentation/Knowledge Base/Colo General/Common Issues 1 

## Global IP Networks (1850) | Infrastructure | Jul 06, 2025 08:49am 


 Now we will need to list the users and grab the user ID Run "IPMICFG.EXE user list" This will display the users. make note of the ADMIN username as its generally the one we change unless requested other wise. In addition make note of the capitilzation. 

### 2. 

 Since in this case we will be changing the ADMIN password user id is 2 Run "IPMICFG.EXE -user setpwd 2 ADMINADMIN" This will reset the password to ADMINADMIN you can change that as you wish. 

### 3. 

## Core Assets/Documentation/Knowledge Base/Colo General/Common Issues 2 

## Global IP Networks (1850) | Infrastructure | Jul 06, 2025 08:49am 


