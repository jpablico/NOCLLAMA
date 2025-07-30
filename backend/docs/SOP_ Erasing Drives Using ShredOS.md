# Standard Operating Procedure: Erasing Drives Using ShredOS

This document outlines the standard operating procedure (SOP) for securely erasing hard drives using ShredOS. Following these steps will ensure that all data is unrecoverable and meets data disposal requirements.

# 1\. Purpose

The purpose of this SOP is to provide clear, step-by-step instructions for the complete and secure erasure of data from hard drives using ShredOS, a free and open-source data shredding utility. This ensures compliance with data protection policies and prevents unauthorized access to sensitive information.

# 2\. Scope

This SOP applies to all personnel responsible for the disposal or re-purposing of computer hard drives within the organization. It covers the preparation of the ShredOS boot media, the boot process, and the data erasure process.  
**This procedure is designed to support compliance with data protection standards including HIPAA and SOC 2 by ensuring that all stored data is securely and irreversibly destroyed.**

# 3\. Prerequisites

Before starting the data erasure process, ensure the following prerequisites are met:

* **ShredOS Bootable Media:** A USB drive or CD/DVD containing the ShredOS ISO image, properly created to be bootable.  
* **Target Drive(s):** The hard drive(s) to be erased must be physically accessible and connected to the system.  
* **Compatible System:** A computer capable of booting from USB or CD/DVD.  
* **Power Supply:** A stable power supply for the system and the drive(s).  
* **Documentation:** A method to record the erasure process, including drive serial numbers and confirmation of erasure.

# 4\. Procedure

## 4.1. Creating ShredOS Bootable Media

| Step | Description | Notes |
| :---- | :---- | :---- |
| 1 | Download the latest ShredOS ISO image from the official website. | Verify the integrity of the downloaded ISO. |
| 2 | Use a tool (e.g., Rufus for Windows, BalenaEtcher for macOS/Linux) to create a bootable USB drive from the ISO. | Ensure the correct USB drive is selected to avoid data loss on other drives. |
| 3 | For CD/DVD, burn the ISO image to a blank disc using disc burning software. |  |

## 4.2. Booting from ShredOS

| Step | Description | Notes |
| :---- | :---- | :---- |
| 1 | Insert the ShredOS bootable media into the target computer. |  |
| 2 | Power on the computer and access the BIOS/UEFI settings (typically by pressing F2, Del, F10, or F12 during startup). | The key varies by manufacturer. |
| 3 | Change the boot order to prioritize the ShredOS bootable media (USB or CD/DVD). | Save changes and exit BIOS/UEFI. |
| 4 | The computer will now boot into ShredOS. | The ShredOS command-line interface will appear. |

## 4.3a. Erasing Drives via CLI

| Step | Description | Notes |
| :---- | :---- | :---- |
| 1 | At the ShredOS prompt, type `sudo shred` and press Enter to list available drives. | Identify the correct drive(s) to be erased by their size and identifier (e.g., `/dev/sda`, `/dev/sdb`). **CAUTION: Selecting the wrong drive will result in irreversible data loss.** |
| 2 | To erase a drive, use the command: `sudo shred -v -n 3 /dev/sdX` (replace `X` with the correct drive letter, e.g., `a`, `b`).  | This command performs 3 passes of data erasure with verbose output. |
| 3 | For more secure erasure (e.g., 7 passes): `sudo shred -v -n 7 /dev/sdX` | More passes increase security but also erasure time. |
| 4 | To use a specific erasure method (e.g., Gutmann), refer to the ShredOS documentation or use the appropriate command-line options. | `sudo shred -v --method=gutmann /dev/sdX` (Gutmann is very slow but highly secure) |
| 5 | Monitor the erasure process. Once complete, ShredOS will indicate that the operation is finished. | The time taken depends on the drive size and the number of passes. |
| 6 | After erasure, remove the ShredOS boot media and power off the computer. |  |

# 

## 4.3b. Erasing Drives via GUI

| Step | Description | Notes |
| :---- | :---- | :---- |
| 1 | At the ShredOS menu, select nwipe using arrow keys and press Enter. | This opens a terminal-based GUI for erasing drives. |
| 2 | Select drives to erase by using arrow keys to highlight and pressing Spacebar. | An asterisk \* will appear next to the selected drives. |
| 3 | **Press M** to choose wipe method and select DoD Short. | The default is Zero Fill or PRNG Stream.  |
| 4 | **Press Shift \+ S** to start the wipe session. | Wipe begins for all selected drives. Progress will be shown in real-time |
| 5 | Monitor the wipe process. | Displays percent complete, speed, and ETA for each drive. |
| 6 | **Optional**: Cancel an individual wipe by highlighting the drive and pressing C. | Use only if necessary as canceled wipes will not complete securely. |
| 7 | Press Q to quit after all drives finish wiping. |  |
| 8 | Document the wipe. | Record date, drive serial, method used, and technician initials for auditing. |

# 

# 5\. Verification

After the erasure process is complete, it is recommended to:

* **Visually Inspect:** Ensure the drive is still functional (if intended for re-use) but contains no identifiable data.  
* **Attempt Boot:** For operating system drives, confirm that the system cannot boot from the erased drive.   
  * This should only be done only if the drive is not physically destroyed afterwards and that no user data should be ever recoverable.  
* **Documentation:** Record the successful erasure, including the drive's serial number,   
* the date of erasure, and the method used.

# 6\. Record Keeping

Maintain a log of all drives erased, including:

* Drive serial number  
* Date of erasure  
* ShredOS version used  
* Erasure method (e.g., number of passes, specific algorithm)  
* Name of the individual performing the erasure  
* Confirmation of successful erasure

This information is crucial for audit trails and compliance.

# 7\. Safety Precautions

* Always handle hard drives with care to avoid physical damage.  
* Ensure proper grounding to prevent electrostatic discharge (ESD) when handling internal components.  
* Do not interrupt the erasure process once it has begun, as this could leave residual data.

# 8\. Troubleshooting

* **ShredOS fails to boot:** Verify boot order in BIOS/UEFI, check the integrity of the ShredOS bootable media.  
* **Drive not detected:** Ensure the drive is properly connected and powered. Check cable connections.  
* **Erasure process freezes:** This could indicate a failing drive. Attempt re-erasure or consider physical destruction if the issue persists.

