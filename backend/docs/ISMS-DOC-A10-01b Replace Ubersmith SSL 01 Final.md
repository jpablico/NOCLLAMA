# Operating Procedure 

## Replace Ubersmith SSL 


 ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 

### Revision history 

##### VERSIO 

##### N 

##### DATE REVISION AUTHOR SUMMARY OF CHANGES 

 1 12/02/2024 Frank Marshall Original document 

### Distribution 

##### NAME TITLE 

 Global IP Networks Engineers and management 

### Approval 

##### NAME POSITION SIGNATURE DATE 

 Frank Marshall Process Improvement Manager 

##### 12/02/2024 

##### DOCUMENT 

##### CLASSIFICATION 

 Protected | Internal Use Operating Procedure DOCUMENT REF ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final VERSION 1 DATED 12/02/2024 DOCUMENT AUTHOR Frank Marshall DOCUMENT OWNER Frank Marshall 


ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 


 ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 

### Contents 

Introduction 1 Operating procedure 1.1 Scope of procedure 1.2 Prerequisites 1.2.1 Knowledge 1.2.2 Access 1.2.3 Materials 1.2.4 Other 1.3 Timing and scheduling 1.4 Instructions 1.5 Output and media handling 1.6 Backup 1.7 Error handling 1.8 Support and escalation 1.9 Auditing and logging 1.10 Monitoring 

### Tables 

Table 1: Error handling 7 Table 2: Support contacts 8 


 ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 

### Introduction 

It is important that this procedure is followed carefully and to a high standard each time it is used. This control applies to all systems, people and processes that constitute the organization’s information systems, including board members, directors, employees, suppliers and other third parties who have access to company systems. The following policies and procedures are relevant to this document: ISMS-DOC-A10-01a Key Management 01 Draft 01 

## 1 Operating procedure 

### 1.1 Scope of procedure 

This procedure is to be used to replace the SSL for the Ubersmith server. Keeping the SSL up to date will help ensure the server is secure and protected, and is necessary to maintain compliance standards. 

### 1.2 Prerequisites 

There are a number of prerequisites that need to be in place before beginning this procedure. Without them the procedure may fail. 

#### 1.2.1 Knowledge 

In order to successfully carry out the procedure you should have the following level of knowledge and/or experience: ● Knowledge of this procedure and the steps provided in the instructions below. 

#### 1.2.2 Access 

You will need the following levels of access to carry out this procedure: ● Root level SSH access to cp.gipnetworks.com (you must be on the approved list to perform this task) ● Be the recipient of admin@gipnetworks.com or other group required by the SSL generator or have read/write access to the DNS server to create DNS record to approve the SSL certificate request ● Account at the SSL generator (https://ssls.com, etc) 


 ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 

#### 1.2.3 Materials 

The following materials will be needed: ● Computer with internet access 

#### 1.2.4 Other 

Additional prerequisites are: ● No other prerequisites are required 

### 1.3 Timing and scheduling 

This procedure needs to be performed prior to the existing SSL expiration date. 

### 1.4 Instructions 

NOTE: Before you do this, please notify the appropriate team that you’re doing maintenance. This may generate warnings! The ssl folder in cp.gipnetworks.com is located at /usr/local/ubersmith/conf/ssl. In order to install/replace the SSL cert, you need to login as root (ask management/Dir of IT for proper root access) and you will need the following files: 

- cp.gipnetworks.com.csr # Certificate request 

- cp.gipnetworks.com.key # The private key 

- cp.gipnetworks.com.cert # The SSL certificate 

- cp.gipnetworks.com.cacert # The SSL authority or ca-bundle, usually contains 2     certs 

- cp.gipnetworks.com.pem # The .key and .cert combined--in that order Once you login via ssh as root, do the following: ==================================== 

1. BACKUP the current SSL Certs     cp -f /usr/local/ubersmith/conf/ssl/cp.gipnetworks.com.cert     /usr/local/ubersmith/conf/ssl/old/     cp -f /usr/local/ubersmith/conf/ssl/cp.gipnetworks.com.key     /usr/local/ubersmith/conf/ssl/old/     cp -f /usr/local/ubersmith/conf/ssl/cp.gipnetworks.com.cacert     /usr/local/ubersmith/conf/ssl/old/     cp -f /usr/local/ubersmith/conf/ssl/cp.gipnetworks.com.pem     /usr/local/ubersmith/conf/ssl/old/ 


 ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 

2. Run this command to create private key (cp.gipnetworks.com.key) and the CSR (cp.gipnetworks.com.csr) in the /usr/local/ubersmith/conf/ssl/ folder:     cd /usr/local/ubersmith/conf/ssl/     rm -f cp.gipnetworks.com.csr     openssl req -new -newkey rsa:2048 -nodes -keyout cp.gipnetworks.com.key -out     cp.gipnetworks.com.csr -subj /CN=cp.gipnetworks.com     cat cp.gipnetworks.com.csr 

3. Go to https://ssls.com or another SSL generator, paste the CSR. Follow the SSL approval process and wait for the cert and ca-bundle to be sent to you. 

4. Once you receive the SSL cert, replace the content of the existing cert cp.gipnetworks.com.cert (make sure the file ends with a new line or <ENTER>) and cacert to cp.gipnetworks.com.cacert in /usr/local/ubersmith/conf/ssl folder. 

5. Paste the key and cert into cp.gipnetworks.com.pem in /usr/local/ubersmith/conf/ssl folder:     cat cp.gipnetworks.com.key cp.gipnetworks.com.cert > cp.gipnetworks.com.pem Note: The content for cp.gipnetworks.com.pem should be something like this (with new line after the dashes):     -----BEGIN PRIVATE KEY-----     [PRIVATE KEY HERE]     -----END PRIVATE KEY-----     -----BEGIN CERTIFICATE-----     [CERT HERE]     -----END CERTIFICATE----- 

6. Run these to activate the new SSL cert:     /usr/local/ubersmith/docker-compose stop web mail     /usr/local/ubersmith/docker-compose up -d web mail Once completed, do these tests: ========================= 

1. Email test. Run this command below and create a ticket in Ubersmith by sending a test email to support@gipnetworks.com 


ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final tail -f /var/log/ubersmith/mail/docker.log You will be able to see in real time that a ticket is created and sent to multiple email addresses. If you see a TLS failure or if a ticket is not created, it means that something is wrong with the SSL certificate and make sure that you repeat the above steps correctly. 

2. Cert test. Open a browser and go to: https://www.ssllabs.com/ssltest/analyze.html? d=cp.gipnetworks.com You should see the test result and verify the new expiration date. The SSL install is successful when you pass these 2 tests. 

### 1.5 Output and media handling 

There will not be any physical output or media as a result of this procedure. 

### 1.6 Backup 

Certificate backup is described in the following procedure: ISMS-DOC-A10-01a Key Management 01 Draft 01 

### 1.7 Error handling 

The following errors may be encountered during the procedure: ERROR CAUSE CORRECTIVE ACTION Unable to access Ubersmith server Not connected to office network or entering incorrect credentials Ensure connection is established to the office network and that credentials are correctly input. _Table 1: Error handling_ 


 ISMS-DOC-A10-01b Replace Ubersmith SSL 01 Final 

### 1.8 Support and escalation 

If an error occurs which cannot be corrected using this procedure, support should be contacted using the following information: SUPPORT PERSON PHONE NUMBER HOURS OF AVAILABILITY Department Managers Slack 24x7 Internal IT Email (support@gipinternal.zendesk.com) 24x7 Program Manager Slack 24x7 _Table 2: Support contacts_ 

### 1.9 Auditing and logging 

No additional auditing and logging needed. 

### 1.10 Monitoring 

No additional monitoring needed. 


