import pandas as pd
import openpyxl as xl
import os.path
from openpyxl import Workbook
from datetime import datetime

#create a class instead
from modules.identifier import generate_identifier
from modules.student import Student


class Processor:



    def __extract_data(self,csv:str):
        df=pd.read_csv(csv)
        for index,row in df.iterrows():
            student=Student(row["matriculation_number"],row["firstname"],row["lastname"], generate_identifier(8))



    def __data_conversion(self):
        pass

    def __create_folder_name(self):
        folder_name = "Folder_Excelfiles_" + datetime.now().now().strftime("%Y-%m-%d_%H_%M_%S")
        return folder_name

    def __create_folder(self,folder_name):
        assert os.path.exists(folder_name)==False
        os.makedirs(folder_name, exist_ok=True)



    def __create_xlsx(self,students:list[Student]):
        for student in students:
            pass


    def run(self,file_name:str):
        if not os.path.exists(file_name):
            print("File path doesn't exist")
        else:
            print(">> Processing...")

            folder_name=self.__create_folder_name()
            self.__create_folder(folder_name)
            self.__extract_data(file_name)
            # TODO: Step 1
            #verfiy if file exists
            df=pd.read_csv(file_name)




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
