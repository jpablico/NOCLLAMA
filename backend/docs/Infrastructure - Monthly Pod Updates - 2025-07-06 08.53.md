## Monthly Pod Updates 

# Purpose 

This is to keep our cloud hosts up to date on windows updates. https://gipnetworks.itglue.com/6265874/docs/10787830 

# Timeline 

This will take place B-biweekly There will also be a ticket in Ubersmith when critical updates come out. General practice is to run updates at night for less impact. 

# Risks 

If Vm's are not moved and host are rebooted can cause downtime for client. Bogging down 1 node with too many VM's causing performance issues and alerts to pop up. 

# Identify if Updates are Needed 

RDP into either of the hosts. in this eample we will be using TXPLA1P1C6SH03 172.26.224.13 Hit you Windows key and search updates. you should see the following. Go ahead and click "Check for Updates" 

# Updating system (no reboot) 

 If the system is needing an update you will see the below screen with the "install now" button in the middle. Research and verify there are no known issues. In the lab environment, test and verify these updates. Once successfully tested, notify your shift lead or dept manager that approval is needed. After approval, schedule the maintenance, create a ticket in Ubersmith, set a timer and notify the team via Slack. During the scheduled maintenance window go ahead and click "Install Now". This will not reboot the system. 

## Core Assets/Documentation/Procedures/Cloud 1 


Document the changes in the ticket and send out completion notices. 

# Rebooting Server for updates. 

If the server prompts for "Reboot now" you will need to move VMs off of this server. 

# Moving Vm's from Node 

 Make note. Node = Physical Server Roles = VM sever Open failover Cluster Manager 

### 1. 

## Core Assets/Documentation/Procedures/Cloud 2 


 Go go Nodes. You should see all the nodes listed in the cluster. 

### 2. 

 Pause the node. in this case we are updating TXPLA1PC6SH03 Right click >> Pause >> Do Not Drain roles. ##The purpose for Pausing is so that Roles do not automatically move back to the node that is about to be updated/rebooted ##The purpose for "Do Not Drain Roles" is that at times Windows will bug out when moving all the roles at the same time. so has to be done in sets. Once paused it should look like the below. 

### 3. 

 On left Panel move over to roles. Sort the nodes by clicking on the "Owner Node" tab. This will list them accordly by what node they are in. Make note of any that are off and write them down. 

### 4. 

## Core Assets/Documentation/Procedures/Cloud 3 


 Highlight few of the nodes at a time. 5 seems to be a good number so it does not error out. ""Holding down shift and going from bottom up helps."" Right click and you will select (Move > Live Migration > Select best node. 

### 5. 

 A menu will pop up with the nodes available to move the role over. In today's case we will be moving them to 14. As a general practice we tend to keep 1 Node empty to be able to move the roles over to. Once the Node is selected the roles will start moving. You should be seeing the below. 

### 6. 

7. Repeat The previous steps 4-6 until roles are off the one you will be updating. 

## Core Assets/Documentation/Procedures/Cloud 4 


# Verifying no VM's on Node 

# Rebooting for update. 

# Restoring VMs. 

Once the server is back up. We will move the VM from 14 back to 3 using steps 6-7. Once complete you may Resume mode.. Resume --> Do not fail roles back Once Roles are back and node resumed you are complete and may move on to the next Node. Open Hyper-V manager and you should see the below. "Some Nodes do have VM's that are not cluster. These tend to be test VM's" Cross compare with fail over cluster manager. For those please pause them until after the updates. 

### 8. 

 If above is clear and any remaining we can now move on to reboot/apply the update. Go back to settings/ updates page. and click reboot now. 

### 9. 

## Core Assets/Documentation/Procedures/Cloud 5 


# When nodes are full. 

There may be times when you can not move all nodes from the one you are updating over to one that is empty. When this is the case. We will need to even the load. CPU Usage on Failover cluster Manager and Memory are the 2 to keep an eye out. Find the least populated one and move a few VMS keeping these numbers even so not to overload just 1. For memory you will get messages and its ok for a temporary alert if you do not have another choice. Repeat these steps for the rest of the Nodes until they are all updated. For Pod 2 cluster TXPLA1P1C6SH14 is usually the empty one. And Pod 01 is TXPLA1P1C6SH10 

### 10. 

## Core Assets/Documentation/Procedures/Cloud 6 


## Core Assets/Documentation/Procedures/Cloud 7 


