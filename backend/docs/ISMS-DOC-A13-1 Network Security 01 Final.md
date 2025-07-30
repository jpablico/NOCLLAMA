# Policy 

## Network Security 


 ISMS-DOC-A13-1 Network Security 01 Final 

### Revision history 

###### VERSIO 

###### N 

###### DATE REVISION AUTHOR SUMMARY OF CHANGES 

 1 11/14/2024 Frank Marshall Original document 

### Distribution 

###### NAME TITLE 

 Global IP Networks Network engineers, managers, executives CloudKey Network engineers, managers, executives Verdyne Network engineers, managers, executives 

### Approval 

###### NAME POSITION SIGNATURE DATE 

 Frank Marshall Process Improvement Manager 

###### 04/30/2025 

###### DOCUMENT 

###### CLASSIFICATION 

 Protected | Internal Use Policy DOCUMENT REF ISMS-DOC-A13-1 Network Security 01 Final VERSION 1 DATED 04/30/2025 DOCUMENT AUTHOR Frank Marshall DOCUMENT OWNER Frank Marshall 


ISMS-DOC-A13-1 Network Security 01 Final 


 ISMS-DOC-A13-1 Network Security 01 Final 

### Contents 

Introduction 1 Network security policy 1.1 Network security design 1.1.1 Requirements 1.1.2 Defense in depth 1.1.3 Network segregation 1.1.4 Perimeter security 1.1.5 Public networks 1.1.6 Wireless networks 1.1.7 Physical security 1.1.8 Remote access 1.1.9 Network intrusion detection 1.1.10 Network security standards 1.1.10.1 Network hardware 1.1.10.2 IP addressing 1.1.10.3 Network protocols 1.2 Network security management 1.2.1 Roles and responsibilities 1.2.2 Logging and monitoring 1.2.3 Network changes 1.2.4 Network security incidents 2 Conclusion 

### Tables 

Table 1: Roles and responsibilities 9 


 ISMS-DOC-A13-1 Network Security 01 Final 

### Introduction 

##### The use of networks is an essential part of the day to day business of Global IP Networks. 

Networks not only connect many of the components of business processes together internally, but they also link the organization with its suppliers, customers, stakeholders and the outside world. The organization’s networks have evolved over a period of time to become the circulatory system of the company, transporting information to where it needs to go and enabling business to be carried out effectively. But the fact that so much information runs through our networks makes them a target for those who would try to steal that information and disrupt our business. Therefore, these networks need to be protected to ensure that the confidentiality, integrity and availability of our vital information is always assured. The effective protection of our networks requires that we adopt good practices in information security covering the design, implementation, operation and management of them and that we ensure that everyone involved follows these practices. 

##### This policy sets out Global IP Networks’s rules and standards for network protection and 

acts as a guide for those who create and maintain our IT infrastructure. Its intended audience is IT and information security management and support staff who will implement and maintain the organization’s defenses. As a cloud service provider (CSP), this policy also applies to the methods used to design and create the physical and virtual networks used to deliver service to our cloud customers. This control applies to all systems, people and processes that constitute the organization’s information systems, including board members, directors, employees, suppliers and other 

##### third parties who have access to Global IP Networks systems. 

The following policies and procedures are relevant to this document: _Mobile Device Policy Teleworking Policy Change Management Process Software Policy Anti-Malware Policy_ 


 ISMS-DOC-A13-1 Network Security 01 Final 

## 1 Network security policy 

### 1.1 Network security design 

The design of networks is a complicated process requiring a good knowledge of network principles and technology. Each design is likely to be different, based on a specific set of requirements that are established early in the process. This policy does not attempt to specify how individual networks should be designed and built but provides guidance for the standard building blocks that should be used. 

#### 1.1.1 Requirements 

A network design must be based on a clear definition of requirements which should include the following security-related factors: A. The classification of the information to be carried across the network and accessed through it B. A risk assessment of the potential threats to the network, taking into account any inherent vulnerabilities C. The level of trust between the different components or organizations that will be connected D. The hours of availability and degree of resilience required from the network E. The geographical spread of the network F. The security controls in place at locations from which the network will be accessed G. Security capabilities of existing computers or devices that will used for access Requirements must be documented and agreed before design work starts. 

#### 1.1.2 Defense in depth 

A “Defense in Depth” approach will be adopted to network security whereby multiple layers of controls are used to ensure that the failure of a single component does not compromise the network. For example, network firewalls may be supplemented by hostbased software firewalls on servers and clients in order to provide several levels of firewall protection. At key points in the network a “defense diversity” approach must also be taken so that vulnerabilities are minimized. For example, this may involve using firewalls from different vendors in series so that if a vulnerability is exploited in one device, the other will not be subject to it. This may be extended to the use of more than one network virus scanner at the perimeter for the same reason. 


 ISMS-DOC-A13-1 Network Security 01 Final 

#### 1.1.3 Network segregation 

The principle must be adopted that, where appropriate, a network will consist of a set of smaller networks segregated from each other based on either trust levels or organizational boundaries (or both). For a large network this may be achieved using separate domains, particularly where separate organizations’ networks are being linked. An appropriate level of trust must be configured at the domain level and domain perimeters must be secured using a firewall where appropriate. Within networks, Virtual Local Area Networks (VLANs) will be used to segregate organizational units. In a cloud environment, it is important that requirements for segregating networks to achieve tenant isolation are defined and the cloud service provider’s ability to meet these requirements is verified. 

##### Where Global IP Networks is acting as a CSP, it is important to enforce segregation 

between our multi-tenant clients and also between the cloud service customer environment and our own internal network. 

#### 1.1.4 Perimeter security 

At all perimeters between the internal network and an external network (such as the Internet) effective measures must be put in place to ensure that only authorized network traffic is permitted. This will usually consist of at least one Stateful Inspection firewall and for major links with the Internet an Application (or Application Gateway) firewall must be used. For connections such as broadband at smaller locations a Packet Filtering firewall may suffice, depending on the results of a risk assessment. Servers that are intended to be accessed from an external, insecure network (such as web servers) must be located in a DeMilitarised Zone (DMZ) of the firewall in order to provide additional protection for the internal network. 

#### 1.1.5 Public networks 

Where information is to be transferred over a public network such as the Internet, strong encryption via TLS must be used to ensure the confidentiality of the data transmitted. Servers that will be accessed from devices on the public network will be located in the DMZ of the firewall. 


 ISMS-DOC-A13-1 Network Security 01 Final 

#### 1.1.6 Wireless networks 

Wireless networks must be secured using WPA2 encryption. WEP and WPA must not be used. Wireless networks must be treated as insecure even if WPA2 is used as the encryption method and a firewall installed between the wireless network and the main LAN. A guest wireless network may be provided for visitors. This must be physically separate from all internal networks (including internal wireless networks) and secured using a firewall. Wireless access points must be configured to not broadcast their SSID and to not allow secure connection using WPS (WiFi Protected Setup) via physical access to the access point itself. Wireless access point admin logon passwords must always be changed from the default. 

#### 1.1.7 Physical security 

Remote network equipment will be housed in secure cabinets which will always be locked. Only support staff will have access to the key to each cabinet. Backbone and centralized network equipment will be housed in appropriate lockable cabinets or racks in a secure server room to which only authorized support staff will have access (except for local facilities staff for reasons of health and safety). Wireless access points located in public areas must be hidden from view where possible and must be placed in positions where access by the public is difficult e.g. in or near the ceiling. A lockable protective casing must be installed where an access point is located in an unprotected public area e.g. a car park. 

#### 1.1.8 Remote access 

Where there is a requirement for remote access to the internal network the following controls will be used: A. A Virtual Private Network (VPN) will be used providing session encryption using SSL/TLS or IPsec B. Two factor authentication at the client where appropriate C. Secure authentication using a Tacacs where possible D. Network Access Control (NAC) will be used to restrict access to remote clients that do not meet minimum requirements e.g. virus control Remote access must be granted on an “as required” basis rather than for all users by default. 


 ISMS-DOC-A13-1 Network Security 01 Final 

#### 1.1.9 Network intrusion detection 

A Network-based Intrusion Detection System (NIDS) must be installed at the network perimeter and at all key points within the network e.g. on critical servers. For networks with high security requirements an Intrusion Prevention System (IPS) may be considered, although its implementation should be approached with caution to avoid a high degree of false positives with corresponding disruption to service to users. 

#### 1.1.10 Network security standards 

The following standards will be adopted with respect to network configuration and security. 

##### 1.1.10.1 Network hardware 

Where possible a single supplier policy will be used for network hardware. An exception will be made where the use of multiple vendor hardware may increase the level of security provided e.g. in a dual network-based firewall configuration. Network routing will be based on routers using OSPF and BGP. Gigabit switches will be used as standard for connectivity. Switch ports, including diagnostic ports, will be configured to be administratively disabled until required. Hubs will not be used due to their inherent security weaknesses. Cat 6 UTP will be used for network cabling unless specific circumstances (such as excessive interference) preclude its use. The network topography used will be Ethernet according to the IEEE 802.3 family of standards. 

##### 1.1.10.2 IP addressing 

IPv4 will be used on internal networks. However new network devices purchased must support IPv6 in preparation for the future. The internal IP address ranges used are part of the RFC1918 standard. The assignment and use of subnets must be monitored carefully and disclosed only to authorized parties. IP addresses and associated network information for desktop and laptop clients will be controlled using DHCP. Internal DNS servers will be used. 


 ISMS-DOC-A13-1 Network Security 01 Final 

##### 1.1.10.3 Network protocols 

The protocol used on all networks will be TCP/IP. UDP will be used where appropriate but other OSI layer 4 network protocols should not be used. Only protocols and ports required on a specific server will be enabled by default in order to reduce the attack surface. This is especially true for servers within the DMZ of the firewall(s). 

### 1.2 Network security management 

Once networks have been designed and implemented based on a clear set of security requirements, there is an ongoing responsibility to manage and control the secure networking environment to protect the organization’s information in systems and applications. This must be achieved via controls in the following areas. 

#### 1.2.1 Roles and responsibilities 

Roles and responsibilities for the management and control of networks must be clearly defined. In order to provide effective segregation of duties, the operation of networks is managed separately from the operation of the rest of the infrastructure such as servers and applications. This segregation of duties is detailed in the following table. MANAGER ROLE TEAM MAIN RESPONSIBILITIES IT Director Network and Communication s Management Design and implementation of new and changed networks Installation and removal of networking equipment Configuration of networking equipment Third line incident management Infrastructure Manager Network Operations Network availability monitoring Network intrusion monitoring Second line incident management Configuration backups Patching and updates Setup and management of remote access users Manage Services Computer Operations Server and application backups 


ISMS-DOC-A13-1 Network Security 01 Final Manager (iOPs) Job scheduling Infrastructure monitoring First line incident management _Table 1: Roles and responsibilities_ 

#### 1.2.2 Logging and monitoring 

Logging levels on network devices must be configured in accordance with organization policy and logs monitored on a regular basis. Firewall logs will be monitored for signs of excessive port scanning which may be a precursor to a remote attack. Where installed, a Network-based Intrusion Detection System must be configured to alert the Network Operations team of this activity. Network monitoring for availability may be achieved using an appropriate SNMP-based network management tool and recovery actions automated where possible. Alerts from the Network Access Control (NAC) system must be addressed immediately to ensure that clients that do not meet minimum security requirements are only allowed access to a quarantined subset of systems on the network. 

#### 1.2.3 Network changes 

All changes to network devices will be subject to the change management process and appropriate risk assessment, planning and back-out methods put in place. Configuration records must be updated whenever such changes are carried out so that a current and accurate picture of the network is always maintained. 

#### 1.2.4 Network security incidents 

Network events which are deemed to be security incidents must be recorded and managed according to the Information Security Incident Response Procedure. 

## 2 Conclusion 

##### Network security is a cornerstone of Global IP Networks’s defenses against many of the 

threats with which we are faced. Only by designing effective security into every new system and network from the very beginning can effective control be maintained, and 


ISMS-DOC-A13-1 Network Security 01 Final risk reduced. Further to this, additional controls must be implemented which ensure that proper segregation of duties is achieved and changes to the network environment happen in a managed way. Combined with watchful monitoring of the network itself and the tools put in place to manage it, this should ensure that the number and severity of network security incidents is minimized and our exposure from those that do occur is not as great as it otherwise might have been. 


