# Catalog Project

Catalog is a web application written in python using the Python framework Flask. Provides a list of tracks within a variety of artist as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own tracks contains in the database.

### How to Run the application
Download the [Catalog] project.
This website is a server-side application. You need to run *application.py* in a web server and then access to http://localhost:8000/.

You can use a *virtual machine* (VM) to run a web server locally.
- **VirtualBox** is a software that runs a VM. [You can download it from virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
- **Vagrant** is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [You can download it from vagrantup.com](https://www.vagrantup.com/downloads.html)

On Mac or Linux systems, you can use the regular terminal program to run application.py. On Windows, you will need to download **Git** from [git-scm.com](https://git-scm.com/downloads). Git will provide you with a Unix-style terminal and shell (Git Bash)

Using the terminal, change directory to vagrant folder using the command *cd vagrant*, then type *vagrant up* to launch your virtual machine.
Once it is up and running, type *vagrant ssh*. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt.

Change directory to the /vagrant directory by typing *cd /vagrant*. This will take you to the shared folder between your virtual machine and host machine. Then change directory to the /catalog directory.

In order to create and populate the database run *additems.py*, then run *application.py* to get the web page running on http://localhost:8000/.
```sh
$ cd vagrant
$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ cd catalog
$ python additems.py
$ python application.py
```
Finally, you can access the application by visiting http://localhost:8000 locally.


License
----

MIT


**Free Software**

   [Catalog]: <https://github.com/oisbel/catalog-project.git>