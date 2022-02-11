[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6717585&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

The template repository contains a basic structure for coursework 1.

**Do not** use this to determine what to put in the coursework, you must refer to the coursework specification on
Moodle.
##Question can be answered
The target audience are two kinds of people, the first is police detective and the second is citizens. the visualisation of the dashboard could answer the question
1. what is the trend of London crime rate between 2019-2021? Going up or going down?

2. Which boroughs have significant higher crime rate than others? (Need to deploy more police resources)

3. What type of crime is the most frequent? (Need to increase public awareness of that crime)
According to the barchart showed 

##Explain your design for each visualisation. You can do this before you code the visualisation.
The upper-right visualisation is a map, which is created by connecting a geojson file with the longitude and latitude of
every borough in London and the given crime dataset. The different number of crime cases would reflect on the darkness 
level on the map, and there is interaction between the map and the upper-left visualisation, which is when clicking the 
borough area, the corresponding trend of crime cases chronologically on the upper-left corner.
The upper-left visualisation is combined with a line chart and a bar chart. The line chart represents the trend of number
of crime cases happened from 2019 to 2021 monthly, and the bar chart represents the number of total notifiable crime 
cases in every borough in London. They are interactive with each other as when clicking one borough in the bar chart, the
line chart would change accordingly to show the chosen borough’s trend of number of crime cases.
The down-left visualisation is a bar chart representing the major crime types of one borough. There is a new interaction
with the upper-left visualisation, because once clicking one borough in the bar chart, the major crime types would change
according to show the ranking of borough’s major crime types cases comparing in the whole dataset.
Similarly, the down-right visualisation is still a bar chart representing the minor crime types below the major crime 
types. There is also an interaction with the down-left visualisation Once clicking one borough in bar chart on upper-left,
the ranking of cases of major crime types in that borough would show, and the minor crime types below the major crime 
types would also show.

## Instructions for using the starter code

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
   or [Cloning a repository in VS Code](https://code.visualstudio.com/docs/editor/github#_cloning-a-repository)
2. Add a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [use python in your shell.](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. PyCharm, VisualStudio Code, Xcode and NetBeans have
   already been added.
5. Copy the prepared data set from COMP0035 coursework to this repository. You may need to use 'git add' to add the file
   to be tracked by git.
6. Commit and push the data set to GitHub. This is your first commit for coursework 1. Remember to use source code
   control throughout the coursework.
7. `dash_app.py` has been included to allow you to test that your project set up is sufficient to run Dash. Once you are
   happy that you have set up the project then you should delete the contents of app.py and replace with your coursework
   code.
    - To run the dash app from the terminal or shell make sure you are in directory of your repository and type and
      run `python dash_app.py`
    - To run the dash app from PyCharm, right click on the file name `dash_app.py` in the Project pane and
      select `Run dash_app`. Or open `dash_app.py` and click on the green run arrow near line 29.
    - To run the dash app from VS Code, use the Run option from the left pane.
8. By default, the dash app should launch on port 8050 of your localhost with the IP
   address [127.0.0.1:8050](http://127.0.0.1:8050/). Open the URL in a browser. Note: If you get an error like
   this: `OSError: [Errno 48] Address already in use` then another application is already using the default port (this
   will also happen if you forget to stop a previous Dash app and try to start another!). You can try another port by
   modifying the line of code that runs the Dash app to specify a different port number
   e.g. `app.run_server(debug=True, port=1337)`

## Before you submit the coursework

Remove the instruction text above and complete this README.md using the guidance in the coursework specification.

