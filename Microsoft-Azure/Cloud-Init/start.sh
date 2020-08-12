#Set-up a VM with the app and dependencies using cloud-init

az group create -n groupname
az vm create -g groupname -n templateVM --admin-username agris --image UbuntuLTS --generate-ssh-keys --custom-data template-init.txt

Start-Sleep -s 300
_______________________________________________________________________________________________________________________
#Make the VM an image for use in a scale-set

az vm deallocate -g groupname -n templateVM
az vm generalize -g groupname -n templateVM
az image create -g groupname -n image --source templateVM
______________________________________________________________________________________________________________________
#Launch a scale-set using the image and a cloud-init to start the app

az vmss create -g groupname -n scaleset --image image --upgrade-policy-mode automatic --admin-username agris --generate-ssh-keys --custom-data scale-init.txt
