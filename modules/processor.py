# import pandas as pd
# import openpyxl as xl
import os.path
from openpyxl import Workbook

# import modules.identifier as identifier

#create a class instead
from identifier import Identifier
from modules.student import Student


class Processor:

    def __extract_data(self,csv:str)->list:
        pass
    def __data_conversion(self):
        pass

    def __create_xlsx(self,students:list[Student]):
        pass
    def __reset(self):
        pass

    def run(file_name:str):
        print(">> Processing...")
        # TODO: check if exists file
        # ---- YOUR CODE STARTS HERE ----

        # TODO: Step 1
        #verfiy if file exists
        with open(file_name,"r") as csv:
            array=csv.readlines()

        # ----- Read students.csv for further processing

        # TODO: Step 2
        #create a class student
        #student has a name
        # ----- Generate a random 8-character string ("identifier") for each student
        # ----- Hint: you can use the identifier.py module ("import modules.identifier as identifier")

        # TODO: Step 3
        # ----- For each student, generate a copy of template.xlsx containing the student information in the appropriate fields
        # ----- Store the generated student files in the generated/ folder using a naming scheme like "<identifier>.xlsx"
        # ----- Hint: the identifier of each student should be stored in the cell R2
        # ----- Hint: the following might help: https://openpyxl.readthedocs.io/en/stable/tutorial.html

        # ---- YOUR CODE ENDS HERE ----
        print(">> Finished processing.")
