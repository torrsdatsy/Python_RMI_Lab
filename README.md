This project is for Java RMI Architecture that translates into Python RMI using Pyro5(is a Python library that building distributed applications)

The Folder name "Python_RMI_Lab" has three python code files in project structure:

-client.py = Obtains URL, creates proxy, and invoke methods 
-product.py = implementing class objects
-server.py = Registers the Objects initializes Daemon(Pyro5)

STEPS:

clone repository(Optional)
- Locate project repositories on hosting platform
- Click the code button and copy the repository using (HTTP/SSH)
- Open the terminal and enter the command below:

    bash
    git clone https://github.com/torrsdatsy/Python_RMI_Lab.git

- Verify the Remote Connection

    Bash
    git remote -v


Before running the project in the terminal, make sure the version of python is 3 and above.

1. Open the terminal, enter the command "pip install Pyro5" to install library.

    bash
    pip install Pyro5

2. Then, separate the terminal for client and the server by clicking "Split Terminal"icons/(Ctrl + Shft + 5)

3. Start the server first:
     to run the command in CLI terminal just type "python server.py" and hit enter to start the server.

     bash
     python server.py

4. Then Run the client:

    to run the command by typing "python client.py" and hit enter to execute, display product details retreive from the server to console. 

    bash
    python client.py




Done......
