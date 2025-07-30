# Operating Procedure 

## Change Management 


 ISMS-DOC-A12-02a Change Management 01 Final 

### Revision history 

###### VERSION DATE REVISION AUTHOR SUMMARY OF CHANGES 

 1 10/05/2023 Frank Marshall Initial document 

## Distribution 

###### NAME TITLE 

 Global IP Networks All staff CloudKey All staff Verdyne All staff 

## Approval 

###### NAME POSITION SIGNATURE DATE 

 Frank Marshall Process Improvement Manager 

###### 01/26/2024 

###### DOCUMENT 

###### CLASSIFICATION 

 Protected | Internal Use Procedure DOCUMENT REF ISMS-DOC-A12-02a Change Management 01 Final VERSION 1 DATED 

###### 10/05/2023 

 DOCUMENT AUTHOR Frank Marshall DOCUMENT OWNER Frank Marshall 


ISMS-DOC-A12-02a Change Management 01 Final 


 ISMS-DOC-A12-02a Change Management 01 Final 

### Contents 

Introduction 1 Operating procedure 1.1 Scope of procedure 1.2 Prerequisites 1.2.1 Knowledge 1.2.2 Access 1.2.3 Materials 1.2.4 Other 1.3 Timing and scheduling 1.4 Instructions 1.4.1 If you are the initiator 1.4.2 If you are a member of the change management CAB and or E-CAB 1.5 Output and media handling 1.6 Backup 1.7 Error handling 1.8 Support and escalation 1.9 Auditing and logging 1.10 Monitoring 

### Tables 

Table 1: Error handling 8 Table 2: Support contacts 8 


 ISMS-DOC-A12-02a Change Management 01 Final 

### Introduction 

It is important that this procedure is followed carefully and to a high standard each time it is used. This control applies to all systems, people and processes that constitute the organization’s information systems, including board members, directors, employees, suppliers and other third parties who have access to company systems. The following policies and procedures are relevant to this document: Global IP Networks Change Management Policy 

## 1 Operating procedure 

### 1.1 Scope of procedure 

This procedure covers the process of submitting and resolving a change request in accordance with the Global IP Networks change management policy. This process is to be followed for both internal and external systems. The outcome will result in a fully documented, assessed, planned, and implemented change. 

### 1.2 Prerequisites 

There are a number of prerequisites that need to be in place before beginning this procedure. Without them the procedure may fail. 

#### 1.2.1 Knowledge 

In order to successfully carry out the procedure you should have the following level of knowledge and/or experience: In order to successfully carry out the procedure you should have the following level of knowledge and/or experience: ● Knowledge of how to use Zendesk. ● Understanding of the Global IP Networks Change Management Policy Note: Implementers may require additional knowledge depending on the change request. 


 ISMS-DOC-A12-02a Change Management 01 Final 

#### 1.2.2 Access 

You will need the following levels of access to carry out this procedure: ● Agent level access to Zendesk. ● Access and at least read permissions to internal documentation residing in the following locations: ○ Global IP Networks IT Glue ○ Global IP Networks Google Drive ○ CloudKey Microsoft Sharepoint Note: Implementers may require additional access depending on the change request. 

#### 1.2.3 Materials 

The following materials will be needed: Internet access and a device capable of accessing the items listed above will be needed. 

#### 1.2.4 Other 

Additional prerequisites are: Other prerequisites may be needed depending on the change management request that is created. This may include additional knowledge and access to internal systems as specified by the change request. 

### 1.3 Timing and scheduling 

This procedure needs to be performed to begin the change management process. This can be initiated by internal or external sources. Generally change requests include (but are not limited to) requests or observations that require changes to internal or external infrastructure, tools, and or systems. 


 ISMS-DOC-A12-02a Change Management 01 Final 

### 1.4 Instructions 

#### 1.4.1 If you are the initiator 

1. A ticket needs to be created in Zendesk to document and initiate the change     request.        a. With Zendesk open, create a new ticket by clicking (+ Add > New > Ticket). 

2. Apply the macro that is most appropriate for the change being requested. The     three applicable macros are as follows:        a. For emergency and standard changes:           i. Change Management > Change Request - Emergency 

1. Generally used for changes that are identified as emergency     changes per the change management policy. ii. Change Management > Change Request - Standard 

1. Generally used for changes that are identified as standard     changes per the change management policy. b. For normal and major changes: i. Change Management > Change Request - Infrastructure 

1. Generally used for changes that affect Global IP Networks     data center/ colocation infrastructure, clients, and or tools. ii. Change Management > Change Request - iOps 

1. Generally used for changes that affect Global IP Networks     MSP infrastructure, clients, and or tools. iii. Change Management > Change Request - CloudKey 

1. Generally used for changes that affect CloudKey     infrastructure, clients, and or tools. 

3. Complete the required fields in the body (internal note) of the ticket. This is pre-     populated by the selected macro. 

4. Click (Submit as …) to finish creating the ticket. 

#### 1.4.2 If you are a member of the change management CAB and 

#### or E-CAB 

1. Once the change request ticket has been created, an email will be generated to     notify the manager that is designated by the macro that was selected during the     creation of the ticket.        a. A ticket will also be generated in the “Change Management” queue with           the “New” ticket status. 

2. Based on the content of the request, the ticket subject should be modified to     include a brief description of the request using the following template:        a. “INFRASTRUCTURE | “ _Brief description here’_ ”           i. Note the first word of the subject may be different depending on              the macro that was chosen during the creation of the ticket. 

3. The request will undergo a review process:     a. The “Change Status” field should be updated to “Under Review”.     b. The “Affected Department” field should be populated accordingly. 


 ISMS-DOC-A12-02a Change Management 01 Final c. The “Change Category” field should be populated based on the most appropriate category as defined in the change management policy. i. Note, if the category is set to “Major” the request requires additional review from the IT Steering Group. d. The “Affected Customer” field should be populated based on which customer the change request is associated with. i. For internal changes the customer would be Global IP Networks for example. e. The “Implementer” field should be populated with the name of the implementer(s) once that information has been established. f. The request shall be reviewed for accuracy and feasibility. If a MOP and or back-out plan is required, the initiator will be notified to update the ticket with the requested information/ documentation. i. The “Change Status” field should be updated to “Needing Revision”. ii. The ticket should be reassigned to the initiator. 

4. Once the review process has been completed, the request will either be approved     or denied.        a. If the request is denied, a brief description of the reason is to be           documented using an internal note and the “Change Status” field should           be updated to “Rejected”.        b. If the request is approved, the “Change Status” field should be updated to           “Approved”. 

5. Once approved, the request is to be scheduled (if applicable) by selecting a date     under the “Scheduled Change Date” field.        a. The “Change Status” field must also be changed to “Scheduled”. 

6. Once the change is completed, the “Change Status” field should be either updated     to “Successful” or “Failed” based on the change outcome.        a. For failed changes, a brief description of the failure reason and back-out           plan progress (if applicable) should be provided via internal note on the           ticket.        b. If the status is set to “Failed”, the change request is to be re-evaluated           starting at step 3 of this section. 

7. For change requests with the “Rejected” or “Successful" statuses, a final review     needs to be conducted with closing notes provided via internal note on the ticket     before setting the ticket status to “Solved”. 

### 1.5 Output and media handling 

There will not be any physical output as a result of this procedure. 

### 1.6 Backup 

There will not be any backup data to process as a result of this procedure. 


 ISMS-DOC-A12-02a Change Management 01 Final 

### 1.7 Error handling 

##### The following errors may be encountered during the procedure: 

###### ERROR CAUSE CORRECTIVE 

###### ACTION 

###### COMMENTS 

Cannot login to Zendesk Expired or forgotten credentials Use the self password reset option Cannot update or create Zendesk ticket Zendesk internal error or backend configuration error Refresh and try again, ask if there are any currently active service outages/ interruptions, try again using another browser or after a computer reboot, check if you have a stable internet connection. _Table 1: Error handling_ 

### 1.8 Support and escalation 

If an error occurs which cannot be corrected using this procedure, support should be contacted using the following information: SUPPORT PERSON PHONE NUMBER HOURS OF AVAILABILITY Department Managers Slack 24x7 Internal IT Email (support@gipinter nal.zendesk.com) 24x7 Program Manager Slack 24x7 _Table 2: Support contacts_ 


 ISMS-DOC-A12-02a Change Management 01 Final 

### 1.9 Auditing and logging 

Auditing records are documented and maintained via the Zendesk system used to initiate the change request. 

### 1.10 Monitoring 

The activity and progress will be monitored within the Zendesk system under the queue specified in section 1.4. 


