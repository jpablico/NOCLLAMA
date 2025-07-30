# Operating Procedure 

## Service Cancellation 


 ISMS-DOC-07-10 Service Cancellation 02 Final 

### Revision history 

##### VERSION DATE REVISION 

##### AUTHOR 

##### SUMMARY OF CHANGES 

 1 07/31/2023 Frank Marshall Original 2 01/25/2024 Frank Marshall Revision to comply with new ISO format 

### Distribution 

##### NAME TITLE 

 Global IP Networks Support analysts, support engineers, engineers, iOps leads 

### Approval 

##### NAME POSITION SIGNATURE DATE 

 Frank Marshall Process Improvement Manager 

##### 01/26/2024 

##### DOCUMENT 

##### CLASSIFICATION 

 Protected | Internal Use Procedure DOCUMENT REF ISMS-DOC-07-10 Service Cancellation 02 Final VERSION 2 DATED 01/25/2024 DOCUMENT AUTHOR Frank Marshall DOCUMENT OWNER Frank Marshall 


 ISMS-DOC-07-10 Service Cancellation 02 Final 

### Contents 

Introduction 1 Operating procedure 1.1 Scope of procedure 1.2 Prerequisites 1.2.1 Knowledge 1.2.2 Access 1.2.3 Materials 1.2.4 Other 1.3 Timing and scheduling 1.4 Instructions 1.5 Output and media handling 1.6 Backup 1.7 Error handling 1.8 Support and escalation 1.9 Auditing and logging 1.10 Monitoring 

### Tables 

Table 1: Error handling 6 Table 2: Support contacts 7 


 ISMS-DOC-07-10 Service Cancellation 02 Final 

### Introduction 

It is important that this procedure is followed carefully and to a high standard each time it is used. This control applies to all systems, people and processes that constitute the organization’s information systems, including board members, directors, employees, suppliers and other third parties who have access to company systems. 

## 1 Operating procedure 

### 1.1 Scope of procedure 

This procedure is to be used whenever a service cancellation is needed. This ensures that all services are properly removed and that the billing department is notified to cease invoicing. These tasks will be handled via the ticketing system. 

### 1.2 Prerequisites 

There are a number of prerequisites that need to be in place before beginning this procedure. Without them the procedure may fail. 

#### 1.2.1 Knowledge 

In order to successfully carry out the procedure you should have the following level of knowledge and/or experience: 

- Knowledge of how to use the Zendesk ticketing system Note: various other levels of knowledge may be required depending on the service(s) being modified. 

#### 1.2.2 Access 

You will need the following levels of access to carry out this procedure: 

- Team member level access to the Zendesk ticketing system 

- Access to view client level services in Ubersmith Note: various other levels of access may be required depending on the service(s) being modified. 

#### 1.2.3 Materials 


ISMS-DOC-07-10 Service Cancellation 02 Final The following materials will be needed: 

- Computer or other device with access to the internet 

#### 1.2.4 Other 

Additional prerequisites are: 

- No other prerequisites are needed 

### 1.3 Timing and scheduling 

This procedure is to be followed whenever a service cancellation need is generated either internally or externally. 

### 1.4 Instructions 

1. An internal ticket needs to be created in Zendesk to document the service     cancellation request.        a. The following macro must be applied to track the progress of the           cancellation: “Service Removal::All Services” 

2. List each service that is to be canceled with the desired cancellation date notated. 

3. Management will conduct a review of the account to ensure there are not any     conflicting factors to the request such as contract commitment dates or other     obligations. Once this is marked as complete (“account reviewed?: Y”) the next     steps must be followed.        a. Management should not mark this step as complete until all confirmations           have been made with the client. It’s possible this process ends at this step. The following should only be performed if the account reviewed field is marked yes by management. 

4. Once the target cancellation date is reached, remove the service from the     associated backend system. 

5. Once the service has been removed from the associated backend system, mark     the field “service status” as “removed”. 

6. Once all services have been marked as removed, assign the ticket to the     operations manager for review. 

7. Once reviewed and accepted by the operations manager, the ticket must be sent     to the controller so invoicing can be removed.        a. The billing department must indicate the status of each service item using           the field “invoicing status”. Once all invoicing statuses are marked as 


 ISMS-DOC-07-10 Service Cancellation 02 Final “removed”, the service cancellation can be considered complete and final confirmation can be sent to the client before closing the ticket. 

### 1.5 Output and media handling 

The only output resulting from this procedure will be ticket information which will be stored in the ticketing system. 

### 1.6 Backup 

There will not be any backup data to process as a result of this procedure. All records resulting from this procedure will be stored in the ticketing system. 

### 1.7 Error handling 

The following errors may be encountered during the procedure: ERROR CAUSE CORRECTIVE ACTION Cannot login to Zendesk Expired or forgotten credentials Use the self password reset option Cannot update or create Zendesk ticket Zendesk internal error or backend configuration error Refresh and try again, ask if there are any currently active service outages/ interruptions, try again using another browser or after a computer reboot, check if you have a stable internet connection. _Table 1: Error handling_ 


 ISMS-DOC-07-10 Service Cancellation 02 Final 

### 1.8 Support and escalation 

If an error occurs which cannot be corrected using this procedure, support should be contacted using the following information: SUPPORT PERSON PHONE NUMBER HOURS OF AVAILABILITY Department Managers Slack 24x7 Internal IT Email (support@gipinternal.zendesk.com) 24x7 Program Manager Slack 24x7 _Table 2: Support contacts_ 

### 1.9 Auditing and logging 

Auditing records are documented and maintained via the ticketing system used to initiate these requests. 

### 1.10 Monitoring 

The activity and progress will be monitored within the ticketing system. 


