## Network Outage 

# Types of outages. 

Main uplink Border router outage. Distro outage 

# Main uplink. 

**Symptoms**. As our uplinks are redundant going on opposite ends .we should be receiving notifications on zabbix. However a good tale sign is the graphs on our noc screen. Also reachable from [http://ggraphs.corp.gipnetworks.com/d/ICzywF3nz/net?orgId=1&refresh=5s](http://ggraphs.corp.gipnetworks.com/d/ICzywF3nz/net?orgId=1&refresh=5s) One end is going to Equinox the other going to our Dallas location then from there routes to Equinox in a triangle shape. still need more details and network map which is available somewhere. The main ones are the below.. Calling the support and giving them the id is what is needed to get support. DIA cogent CID: 3-001119497, support@cogentco.com, 877-726-4368 option 2 twice DIA CenturyLink CID: 441540042, 877-453-8353x1 CID: GI/DIA/00738566, optical.noc@gtt.net, 877-385-5252 equinix-ix CID: 21245893 support@equinix.com, 866-378-4649 ====== ntt CID: 248802 pp205006:9/10 Location: 1950 Stemmons, 888-268-8272 Steps to take. Notify infrastructure chat via Slack and make sure Jordan and Colton are aware Call the appropriate vendor depending on the link that is down. and provide the CID. And get a ticket number in response and add it to slack conversation. DIA cogent CID: 3-001119497, support@cogentco.com, 877-726-4368 option 2 twice DIA CenturyLink CID: 441540042, 877-453-8353x1 CID: GI/DIA/00738566, optical.noc@gtt.net, 877-385-5252 equinix-ix CID: 21245893 support@equinix.com, 866-378-4649 ====== ntt CID: 248802 pp205006:9/10 Location: 1950 Stemmons, 888-268-8272 

# Border routers 

Border routers are the devices that sit at the edge of our network at each location and is what routes our traffic. take a looks at them and note how the look now to note the difference if something was to happen At the time of writing this document below are the border routers we have. PLNOTXJUNRB01 67.210.227.1 Plano PLNOTXJUNRB02 67.210.227.2 Plano DLLSTXEQNRB01 67.210.227.3 Equinox DLLSTXEQNRB02 67.210.227.4 Equinox DLLSTXLONRB01 67.210.227.5 Dallas DLLSTXLONRB02 67.210.227.6 Dallas If we get alerts for this. Many more will follow for distros, cage 6 and even customer cabinets as some customers are not redundant. Phase 1, 2 and 3 are routed thru these so you may get alerts all over. For Dallas we need to engage PDS to do a check and best to dispatch someone at same time to check. For Equinox need details on engaging them, but best to dispatch someone with access and knowledge of the place. 1. Check to make sure they are getting power. and act appropriately 2. Check to make sure link lights are on ports 25 and 26 as those are the uplinks to the web. 3. Notify Infrastructure chat on findings and include Jordan 

# Distro outage. 

Distros is what distributes the uplinks to our customers. At time of writing this below is what we have.. Phase1 Primary Distro Distro1 66.128.52.248 Plano Phase 1 Net cage Phase 1 Secondary Distro Distro2 66.128.52.255 Plano Phase 1 Net cage Phase 2 Priamry distro Distro3 66.128.52.254 Plano Phase 2 Net Cage Phase 2 Secondary Distro Distro4 66.128.52.253 Plano Phase 2 Net Cage 

## Core Assets/Documentation/Procedures/Facilities 1 

## Global IP Networks (1850) | Infrastructure | Jul 06, 2025 08:53am 


Phase 1 Shared cab row A6 Distro5 66.128.52.247 Plano Phase 1 behind cage 6 Phase 3 Primary Distro Distro11 66.128.52.241 Plano Phase 3 Net Cage Phase 3 Secondary Distro Distro12 66.128.52.242 Plano Phase 3 Net Cage dallas 66.128.52.243 Net cage Distro 1 also handles Cage 6 and our office traffic. In addition many customers who do not have redundancy set up will be affected. 1. Check to make sure they are getting power. and act appropriately 2. View each of the slots accordingly as cards to seem to fail at times. 1. these can be replaced without any additional configurations. 3. Notify Infrastructure chat on findings and include Jordan 

## Core Assets/Documentation/Procedures/Facilities 2 

## Global IP Networks (1850) | Infrastructure | Jul 06, 2025 08:53am 


