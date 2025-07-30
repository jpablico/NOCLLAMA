# Operating Procedure 

## Key Management 


 ISMS-DOC-A10-01a Key Management 01 Final 

### Revision history 

##### VERSION DATE REVISION AUTHOR SUMMARY OF CHANGES 

 1 10/02/2024 Frank Marshall Original document 

### Distribution 

##### NAME TITLE 

 Global IP Networks Engineers and management CloudKey Engineers and management Verdyne Engineers and management 

### Approval 

##### NAME POSITION SIGNATURE DATE 

 Frank Marshall Process Improvement Manager 

##### 12/02/2024 

##### DOCUMENT 

##### CLASSIFICATION 

 Protected | Internal Use Operating Procedure DOCUMENT REF ISMS-DOC-A10-01a Key Management 01 Final VERSION 1 DATED 10/02/2024 DOCUMENT AUTHOR Frank Marshall DOCUMENT OWNER Frank Marshall 


 ISMS-DOC-A10-01a Key Management 01 Final 

### Contents 

Introduction 1 Operating procedure 1.1 Scope of procedure 1.2 Prerequisites 1.2.1 Knowledge 1.2.2 Access 1.2.3 Materials 1.2.4 Other 1.3 Timing and scheduling 1.4 Instructions 1.5 Output and media handling 1.6 Backup 1.7 Error handling 1.8 Support and escalation 1.9 Auditing and logging 1.10 Monitoring 

### Tables 

Table 1: Error handling 6 Table 2: Support contacts 7 


 ISMS-DOC-A10-01a Key Management 01 Final 

### Introduction 

It is important that this procedure is followed carefully and to a high standard each time it is used. This control applies to all systems, people and processes that constitute the organization’s information systems, including board members, directors, employees, suppliers and other third parties who have access to company systems. The following policies and procedures are relevant to this document: Cryptographic Policy 

## 1 Operating procedure 

### 1.1 Scope of procedure 

This procedure covers key management for all Global IP Networks internal systems 

### 1.2 Prerequisites 

There are a number of prerequisites that need to be in place before beginning this procedure. Without them the procedure may fail. 

#### 1.2.1 Knowledge 

In order to successfully carry out the procedure you should have the following level of knowledge and/or experience: A. Knowledge of how to utilize authorized vendors used for purchasing keys B. Knowledge of adding assets into IT Glue C. Knowledge of storing key information in Google Drive D. Knowledge of how to apply keys to internal Global IP Networks systems 

#### 1.2.2 Access 

You will need the following levels of access to carry out this procedure: A. Access to purchase keys from authorized vendors B. Access to add assets into IT Glue C. Access to Google Drive location for stored and archived keys D. Administrator access to internal Global IP Networks systems 


 ISMS-DOC-A10-01a Key Management 01 Final 

#### 1.2.3 Materials 

The following materials will be needed: A. Computer with internet access (VPN access if outside the office network) 

#### 1.2.4 Other 

Additional prerequisites are: No other prerequisites are required. 

### 1.3 Timing and scheduling 

This procedure is to be followed anytime a key is needed to be obtained, applied, stored, archived, and or deleted. 

### 1.4 Instructions 

Applying or replacing a key 

1. If not already generated via the IT Glue system, create a new Zendesk ticket to     document the work being done 

2. Login to the authorized vendor to purchase the required key 

3. If able, apply the new key to the system(s) as needed     a. Schedule a time to install the key at a later time if the key cannot be        applied 

4. Store the key in Google Drive and name the file with the name of the system it was     applied to        a. Storage location is Management>Infrastructure>Keys>Current        b. Follow the steps in the next section if a key is being replaced 

5. Set an expiration reminder for the key in IT Glue     a. Use the Global IP Networks organization and add a new or update and        existing expiration asset entry     b. Fill out all fields, including the link to the key in Google Drive in the “Link to        Document” field 

6. Update and or close the related Zendesk ticket accordingly Archiving or destroying a key 

1. If not already generated via the IT Glue system, create a new Zendesk ticket to     document the work being done 


 ISMS-DOC-A10-01a Key Management 01 Final a. If a key is being replaced, moved the old key stored in Google Drive from the current folder to the archived folder and remove any IT Glue assets related to the key b. If a key is to be destroyed, delete the key and remove any IT Glue assets related to the key 

2. Update and or close the related Zendesk ticket accordingly 

### 1.5 Output and media handling 

There will not be any physical media as a result of this procedure 

### 1.6 Backup 

Keys will be stored and backed up in Google Drive 

### 1.7 Error handling 

The following errors may be encountered during the procedure: ERROR CAUSE CORRECTIVE ACTION Cannot login to system Expired or forgotten credentials Use the self password reset option Cannot update or create Zendesk ticket Zendesk internal error or backend configuration error Refresh and try again, ask if there are any currently active service outages/ interruptions, try again using another browser or after a computer reboot, check if you have a stable internet connection. Cannot apply key Invalid key or configuration Ensure the correct key is valid and try to apply the key again. Review the system configuration. _Table 1: Error handling_ 


 ISMS-DOC-A10-01a Key Management 01 Final 

### 1.8 Support and escalation 

If an error occurs which cannot be corrected using this procedure, support should be contacted using the following information: SUPPORT PERSON PHONE NUMBER HOURS OF AVAILABILITY Department Managers Slack 24x7 Internal IT Email (support@gipinternal.zendesk.com) 24x7 Program Manager Slack 24x7 _Table 2: Support contacts_ 

### 1.9 Auditing and logging 

Auditing and logging will be handled in the Zendesk system via tickets 

### 1.10 Monitoring 

Monitoring of this procedure will be handled in the Zendesk system via tickets 


