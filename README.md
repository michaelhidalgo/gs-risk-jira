### GS-Risk-Jira

App to help visualise JIRA based risks

### Setup instructions

using python3 (in OSX)

1) clone repo

and run these commands

2) pip3 install -r requirements.txt

create file ```config.py``` with
```
basic_auth=('jira-user', 'jira-pwd')
debug=True
```

3) python3 models.py

this step will require a valid connection to a JIRA server

4) python3 getrisks.py getvulns.py

5) echo {} > techops.json

### Execution instructions

run app using python3 app.py


### update instuctions

to update run

1) python3 models.py
2) python3 datapull_projects.py

run app using

3) python3 app.py