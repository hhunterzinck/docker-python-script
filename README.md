# docker-python-script
This repository runs a single python script with specific package requirements via Docker. The python script accepts command line arguments that can be entered via the Docker run command.  


## Instructions

Clone the github repo and navigate to the directory.  Type in the following commands:

```
docker build -t docker-python-script .
docker run --rm docker-python-script --message 'hello world!'
```

The Dockerfile uses the standard Python image in the Docker repository, builds the Docker container according to the requirements, executes the script, and then stops and removes the Docker container.

If the environment is installed correctly, the result should output 'Old pandas version'.  The script exploits an antiquated functionality of older pandas package version that automatically sorted column names alphabetically after appending to another data frame.  The script checks that the data frame columns have been sorted alphabetically to ensure that an older version of pandas has been correctly installed.  

The script will also output the entered message by the user (i.e. 'hello world!').  The message can be changed to show how different parameters may be input to the script for the same Docker container.  For example: 

```
docker run --rm docker-python-script --message 'The quick brown fox jumps over the lazy dog'
```

