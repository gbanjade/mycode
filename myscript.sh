#!/bin/bash

# Function to grab user and group name
promptuser(){
    read -p "Enter username: " username
    read -p "Enter usergroup: " usergroup
    }

#Function to create a user and assign group
createuser(){
    
    sudo useradd $username
    sudo groupadd $usergroup
    sudo usermod -aG  $usergroup $username
    echo Requested$'\n'Operation$'\n'Completed
    sleep 2
}



#Calling our functions to do the job!
i=1
while((i != 0))
do
   promptuser
   createuser
   read -p "Enter 1 to coninue and any other  key  to quit " i 
done


