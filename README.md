# What is ComfyGet?

ComfyGet is a fork of the TermGet project. It adds new features such as color support, and easier installation for certain operating systems. New unplanned features may come in the future. Some of the features may be merged back into TermGet soon.

TermGet is a project made by PizzaLovingNerd. TermGet is a frontend for:

 - apt-get
 - xbps
 - dnf
 - eopkg
 - zypper
 - pacman (includes yaourt support)
 - sol  (Coming Soon)
 - emerge (Coming Soon)
 - chocolatey (Coming Soon)
 - pip (Coming Soon)

## Some of TermGet's original features

 - Simple, easy to use interface
 - Works in the command line
 - Supports a lot of package managers
 - Feature rich
 - Works on any Linux distribution (and soon Windows)
 - Great for introducing the terminal to new users
 - Code is easy to modify.

## Features added in ComfyGet

 - COLOR
 - Bash Install Script
 - Fixed Grammar & Syntax Errors
 - General Code Cleanup
 - ... More features may come!

## How do I install ComfyGet on Linux

Some dependencies:

 - a terminal with color support (optional, 99% of Linux terminals have color support)
 - git (required to clone/pull repo)
 - bash (required for installation, 99% of Linux distros have this already installed)
 - python3 (required for running ComfyGet)

If this is a first time install, type:

    git clone https://github.com/tbilik/ComfyGet
    cd ComfyGet
    bash install.sh #Do not run as root

This will prompt you if the script detected the proper operating system installed. If all goes well, just it "y" and enter. If you hit another key, it will ask you if you want to proceed installing even though an OS wasn't detected. If you hit another key again, the installation will safely stop.

 If you are updating ComfyGet to a newer version, type:
 
    git pull
    sh update.sh #Do not run as root
    
## First Time Setup On Linux
After installing, run ComfyGet using

    comfyget

If no OS was detected during install, you should get a message that looks like this:

    Please choose a package manager

    1. apt-get (For Debian, and Debian based systems.)
    2. xbps (For Void Linux, and Void Linux based systems)
    3. dnf (For Fedora, and Fedora based systems)
    4. zypper (For OpenSUSE, and OpenSUSE based systems)
    5. eopkg (For Solus, and Solus based systems)
    6. pacman (For Arch, and Arch based systems)

Choose your distribution's package manager using the number. My package manager is eopkg, so I would type "5" and press enter.

## How do I use ComfyGet on Linux

This section gets updated with every release, if you are using an alpha build, there might be extra features that aren't on this section of the README file.

ComfyGet is really easy to use. To run it, all you have to do is open a terminal, and type:

    comfyget


Once your package manager has been chosen, you will get a message similar to this:

    Please choose an action

    1. Search for packages
    2. Install a package
    3. Remove a package
    4. Update all packages
    5. Update repository
    6. Clean
    7. Exit

*We will be using "eopkg" in the examples below.*
*Results may vary for other package managers*

### Searching for Packages

Search searches for packages. This is what it looks like when I search Minetest:

    Please enter search query: minetest

    minetest         - Minetest, an open source infinite-world block sandbox game with survival and crafting.
    minetest-dbginfo - Debug symbols for minetest

    Press enter to continue

### Installing a package

Installing a package downloads and installs a package. This is what it looks like if I install Minetest:

    Total size of package(s): 6.73 MB
    Downloading 1 / 1
    Package minetest found in repository Solus
    minetest-0.4.16-4-1-x86_64.eopkg [cached]
    Installing 1 / 1
    minetest-0.4.16-4-1-x86_64.eopkg [cached]
    Installing minetest, version 0.4.16, release 4
    Extracting the files of minetest
    Installed minetest
	    [✓] Syncing filesystems                                                success
	    [✓] Updating icon theme cache: hicolor                                 success
	    [✓] Updating desktop database                                          success
	    [✓] Updating manpages database                                         success

    Press enter to continue

### Removing a package

  Removing a package uninstalls a package. This is what it looks like if I install Minetest:

      The following list of packages will be removed
      in the respective order to satisfy dependencies:
	  minetest
	  Removing package minetest
	  Removed minetest
	     [✓] Syncing filesystems                                                success
	     [✓] Updating icon theme cache: hicolor                                 success
	     [✓] Updating desktop database                                          success
	     [✓] Updating manpages database                                    	    success

	  Press enter to continue

### Updating all packages

Updating all packages updates EVERYTHING ON THE SYSTEM. Here's what it looks like when you have nothing to upgrade:

	  Updating repositories
	  Updating repository: Solus

	  eopkg-index.xml.xz.sha1sum     (40.0  B)100%    289.47 KB/s [00:00:00] [complete]
	  Solus repository information is up-to-date.
	  No packages to upgrade.

	  Press enter to continue

### Updating the repository

Updating the repository, checks the repository for new versions of packages. It is recommended to do this before updating. Here it looks like when the repository is up-to-date:

	  Updating repository: Solus
	  eopkg-index.xml.xz.sha1sum     (40.0  B)100%    394.80 KB/s [00:00:00] [complete]

	  Solus repository information is up-to-date.

	  Press enter to continue

### Cleaning

Cleaning helps save hard drive space. It does this by deleting cache, and deleting unneeded dependencies. Here is what it looks like:

	  Cleaning package cache /var/cache/eopkg/packages...
	  Cleaning source archive cache /var/cache/eopkg/archives...
	  Cleaning temporary directory /var/eopkg...
	  Removing cache file /var/cache/eopkg/installdb.cache...
	  Removing cache file /var/cache/eopkg/componentdb.cache...
	  The following list of packages will be removed
	  in the respective order to satisfy dependencies:
	  irrlicht
	  Do you want to continue? (yes/no)yes
	  Removing package irrlicht
	  Removed irrlicht
	     [✓] Syncing filesystems    			                    success
	     [✓] Updating dynamic library cache                                     success
	
	  Press enter to continue

## Changing the package manager (on Linux)

### Temporally

To temporally change the package manager used, use an argument. For example, if I wanted to temporally change it to apt-get, I would type

    comfyget apt-get

### Permanently
run the following command in a terminal, then the first setup script will start next time you run termget.

    rm -rf ~/.termget/termget-package-manager && > ~/.termget/termget-package-manager


## Installing ComfyGet on Windows
ComfyGet isn't out for Windows yet. Go talk to PizzaLovingNerd on GitHub if this is a problem. :)

## License:

GNU LESSER GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.

