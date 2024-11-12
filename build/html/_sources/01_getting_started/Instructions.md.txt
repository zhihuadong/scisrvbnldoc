# Basic Info/Instructions for BNL CSI SciServer


### Contact/Help info
To receive notifications about outages/changes or to converse with the BNL CSI SciServer Community, please subscribe to the mailing list, sciserver-csi-l@lists.bnl.gov, at [https://lists.bnl.gov/mailman/listinfo/sciserver-csi-l](https://lists.bnl.gov/mailman/listinfo/sciserver-csi-l).

Another option is to join the BNL CSI SciServer Mattermost channel: [https://chat.sdcc.bnl.gov/bnl/channels/sciserver---users](https://chat.sdcc.bnl.gov/bnl/channels/sciserver---users)

To access this Mattermost channel, you must first register with BNL SDCC's CILogon COmanage instance; please see the "Setting up COmanage" link at [https://www.sdcc.bnl.gov/information/comanage-service](https://www.sdcc.bnl.gov/information/comanage-service). For projects doing alot of development, or needing alot of support, we can create a private mattermost channel if you'd like? (contact the sciserver-csi-admins email below if interested in a private channel)

For issues/problems with the BNL CSI SciServer deployment, please contact: [sciserver-csi-admins@brookhavenLab.onmicrosoft.com](mailto:sciserver-csi-admins@brookhavenLab.onmicrosoft.com) and/or try the mailing list or Mattermost channel above.

Or for help with SciServer in general, including API documentation, there's also: [https://www.sciserver.org/support/](https://www.sciserver.org/support/) or contact: [sciserver-help@jhu.edu](mailto:sciserver-help@jhu.edu)

### Initial Registration
Currently, only a small set of Federated Identity Providers (IDPs) are permitted.
[todo: provide link to list of currently permitted IDPs: currently just "Brookhaven National Laboratory" and "Brookhaven National Laboratory - SDCC.BNL.GOV". WIP to permit other DOE IDPs participating in https://cilogon.org/idplist/ (raw json output), eg. ameslab, anl, fnal, ornl]
[todo: limit the cilogon IDP menu to only include permitted IDPs.]
* Register with BNL SDCC's CILogon COmanage instance; please follow "Setting up COmanage" at https://www.sdcc.bnl.gov/information/comanage-service Choose BNL instead of BNLSDCC if your don't have SDCC account. 
* It is recommanded to send us email sciserver-csi-admins@brookhavenLab.onmicrosoft.com once you have submitted the request.
* Once above registration is approved, email sciserver-csi-admins@brookhavenLab.onmicrosoft.com and request access to BNL CSI's SciServer.
* Once above email request is granted, click the blue "Federated Login (via cilogon.org/COmanage)" button below and authenticate with a permitted IDP.
* On the next screen shown after that:
  * Ignore the option on the left for linking an existing account.
  * Click "Create Account", you should then be logged in and redirected to the SciServer "Dashboard".
### Working with files
* Use "Files" to upload reasonably sized files/directories through the web interface. Browse into either your peristent or scratch space and drag and drop files and/or use the "Upload" button. You can upload/download tar/zip file with size  upto 250GB.  If you have very large files/directories you'd like to upload, please contact [sciserver-csi-admins@brookhavenLab.onmicrosoft.com](mailto:sciserver-csi-admins@brookhavenLab.onmicrosoft.com) for help ingesting large datasets.
### Starting Containers
* Use "Compute" to run interactive compute jobs (eg. Jupyter notebooks or Xwindows sessions).
    * Within "Compute", click the green "Create container" button.
    * Enter a "Container name" for your container (eg. "[your_username]_test_1").
    * Select a "Domain" to choose the hardware resources allocated (details for the selected domain are displayed below the pull down menu).
    * Select your desired "Compute Image". (details for the selected image are displayed below the pull down menu; select "VNC -KDE-GPU" for an Xwindows session)
    * Check the desired User and Data volumes to mount within your container.
    * Click the green "Create" button.
    * If the container started successfully and shows "running" for Status, click on the Name of the container. If it shows "stopped" try refreshing the page. If clicking on the Name opens a new tab with the dashboard, close the new tab and try clicking on the Name again, might have been too fast?
    * At this point you should be in a working Jupyter or Xwindows environment and able to read/write files to your storage volumes:
        * ~/workspace/Storage/[username]/persistent
        * ~/workspace/Temporary/[username]/scratch
* <span style="color: red;"><strong>Please stop the container (red square icon) after you finished interactive session, as it allocates computing resoruces!</strong></span>
