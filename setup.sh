#!/bin/sh
# Initial setup script to setup the impiliontle project.

cwd=$(pwd)
projectdir=$HOME/impilointle

# Copy all code to project directory $HOME/impilointle
if [ "x$cwd" = "x$projectdir" ]; then
    echo "Already in the correct folder, no move required"
else
    if [ -d "$projectdir" ]; then
        echo "Project directory exists."
        echo "Copying all code to project directory. This will take some time."
        rsync -r --exclude '*.zip' . $projectdir/
    else
        echo "Project directory does not exist. Creating"
        mkdir $projectdir
        echo "Copying all code to project directory. This will take some time."
        rsync -r --exclude '*.zip' . $projectdir/
    fi
fi

echo "Installing python dependencies"
cd $projectdir
pip install -r requirements.txt


# Create service file
echo "Copying service file to system folder. If prompted, enter password for user pi"
sudo cp impilointle.service /etc/systemd/system/

echo "Starting application"
sudo systemctl start impilointle
sudo systemctl enable impilointle
echo "Current status of the application"

systemctl status impilointle

echo "Run 'systemctl status impilointle' to know the status of the application"