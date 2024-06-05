## 0x15. API  

### Tasks 
0. Gather data from an API
- A Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

1. Export to CSV
- Using what you did in the task #0, extend your Python script to export data in the CSV format.  
	- Requirements:  
		+ Records all tasks that are owned by this employee  
		+ Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"  
		+ File name must be: USER_ID.csv  

2. Export to JSON  
- Using what you did in the task #0, extend your Python script to export data in the JSON format.  
	- Requirements:  
		+ Records all tasks that are owned by this employee  
		+ Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}  
		+ File name must be: USER_ID.json  


3. Dictionary of list of dictionaries  
- Using what you did in the task #0, extend your Python script to export data in the JSON format.   
	- Requirements:  
		+ Records all tasks from all employees  
		+ Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}  
		+ File name must be: todo_all_employees.json  


