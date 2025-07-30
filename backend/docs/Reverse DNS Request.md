# Reverse DNS Requests(follow steps) 

**_IPV4 Reverse DNS Requests_** *** Make sure the IP address belongs to the customer making the request before making any changes** 

1. Go to the search field in Ubersmith and change “Support Manager” to “Device Manager” in the drop down 2. Copy the IP address provided by the customer and paste it to the search bar (top right hand of the page) 

3. Confirm the IP address belongs to the customer making the request 

4. Open PowerDNS-Admin window - PowerDNS (credentials in IT Glue) 

5. Login 

6. Go to “Hosted Domains **in-addr** ” (Go to “List zones” and “show all”) 

7. Look up IP address backwards as follows:     **A**. If IP address is 67.210.230.142 – You would look it up in this order 230.210.67 (last octet not     included here)     **B**. Once found, click on view zone (notepad icon), this will the “edit zone” page     **C**. Now to find 67.210.230.142, simply look for the last octet, which would be 142     **D**. When you find it , click Edit (Notepad Icon)     **E**. In the “Content” field type or paste the new domain provided by the customer     **F**. Click “Commit Changes”. Repeat if more entries are required     **G**. If there’s no existing record, scroll to the bottom of the page to “Add Record” section , put the last     octet of the IP provided (142 in this case) for the name, the “Type” should be “PTR”, in the “Content”     field type in the domain name provided by the customer, in the “TTL” type 86400 and then click “Add     record”     **I**. Verify that this IP address now exists with correct Domain name 


 IPV6 Reverse DNS Requests 

1. Copy and paste IP address to the search bar located at the top right hand of ticket page 

2. Change Support Manager to Device Manager 

3. Make sure the IP address does belong to the customer making the request 

4. Open PowerDNS window 

5. Login 

6. Go to “Hosted Domains **ip6** ” and select “Manage” for “ **0.0.e.a.5.0.6.2.ip6.arpa** ” 

7. Look up IP address backwards as follows: A. If the IP address is 2605:ae00:2265::18 - go to [http://ipv6-literal.com/](http://ipv6-literal.com/) and paste the IPV6 address in the box. Click convert to get the ip6.arpa address B. Now look up the converted address, excluding “.0.0.e.a.5.0.6.2.ip6.arpa” C. If an entry already exists, simply select “Edit” and change the “Data” field accordingly to how the customer wants it. D. If a record does not exist, select “Add Record” on the top left E. For “Name”, place the converted address from earlier (still omitting .0.0.e.a.5.0.6.2.ip6.arpa). F. Change “Type” to “PTR”. Leave Status to “Active” G. Change “TTL” to “24 hours” H. Place the domain info the customer provided in the “Data” field, make sure to add a “.” at the very end, and hit “Save”. I. Then click “Apply Changes” on the top right. J. Verify that this IP address now exists with correct Domain name 

## Once complete, please utilize the “RDNS Request Complete” template on Ubersmith, and fill out the 

## appropriate fields (Entries Added, Entries removed if any). 


