#!/bin/bash

red_color="tput setaf 1"
green_color="tput setaf 2"
reset_color="tput sgr0"


current_dir_name=`basename "$PWD"`
cd ../../virtual_environments

$green_color
echo -e "Creating virtual environment named: $current_dir_name ..."
$reset_color

virtualenv $current_dir_name
source $current_dir_name/bin/activate
cd ../django/$current_dir_name

$green_color
echo -e "\nInstalling requirements ..."
$reset_color
pip install -r requirements.txt

$green_color
echo -e "\nCreating Empty Django App ..."
$reset_color
app_name="_site"
django-admin startproject $current_dir_name$app_name

$green_color
echo -e "\nStarting the Django App ..."
$reset_color
cd $current_dir_name$app_name
python manage.py migrate
python manage.py runserver

# Install Angular 2 dependencies
#cd ../angular2
#npm install