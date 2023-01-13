#Answers 

##2. Quiz

####2.1 What is the difference between Openpyxl and Xlwings? Why and when would you use one over the other?
- Openpyxl is a good when it comes to writing and reading Excel files
- Xlwings can control excel through its api in addition to writing and reading
- one can use Xlwings to write custom Excel functions in python instead of VBA
- Xlwings requires excel to be installed whereas Openpyxl doesn't

Use case: 

For this task which is a writing heavy tasks or read (add the details of the students in to the Excel file ) it 
is best to use Openpyxl. To be fair reading and writing can also be done by xlwings however after 
researching it seems to me that openpyxl is the industry standard. 

Xlwings is stronger when it comes automating excel tasks and controlling excel directly. 
So it should be used for tasks that require one to use Excel in realtime, writing custom functions 
if one doesn't want to use VBA.

####What does the following code snippet do? What might be wrong with it? What could be done better?
```python
Name_path = os.path.join(some_folder_name, some_file_name)
if os.path.exists(Name_path) is True:
    console.print(
        f"ERROR: The path {Name_path} is missing.\nINSERT THE some_file_name IN THE {some_folder_name} FOLDER",
        style="black",
    )
    exit()
```
- The code snippet checks if a path exists, in the case that the path exists it tells the user
that the file needs to be added to the folder and the path is missing.
- This doesn't make sense logically because the message is shown when the **path exists**
- It should be shown in the scenario that the path doesn't exist
- so to fix one would have to change following

```python 
if not os.path.exists(Name_path):
    #same code as above
 ```



##3. Reflection
### Approach 
My initial approach was to create several classes and work with that. For instance to create a class for each student as well as putting run into class.
However, later on I noticed that creating these classes would be redundant because there's no benefit in having container classes. 
When looking at this task, I structured it into three subtasks... 
- first create a new folder
- extract student data from csv & create identifier
- copying the template adding the student details to the excel file
- adding the file to the folder

These subtasks are done by the function within the run function, so that it easier to debug and more clear.
I also created the constants.py file. This file stores where the template file is located and necessary information where to 
add name, m-number, etc.
The benefit of such file is that stores all of these constants together in one place. If one where to save the template else where
one would solely have to change it the constants file.

I wasn't familiar with Openpyxl and Xlwings, so I used different sources to learn the necessary information, namely Stackoverflow, 
openai(chatbot) and Youtube to learn. 

###Feedback to the task

Find the tasks fair and clear. 

