import shutil

import pandas as pd
import openpyxl as xl
import os.path
from openpyxl import Workbook
from datetime import datetime
import modules.constants as const
from modules.identifier import generate_identifier



class Processor:



    def __extract_data(self,csv:str, target_folder:str):
        df=pd.read_csv(csv)
        for index,row in df.iterrows():
            identifier=generate_identifier(8)
            file_name= f"__{identifier}__" + ".xlsx"

            file_path=os.path.join(target_folder, file_name)
            shutil.copy(const.template_path, file_path)

            wb = xl.load_workbook(file_path)
            ws =wb.worksheets[0]

            ws[const.identifier_cell].value=identifier

            wb.save(file_path)


    def __create_folder_name(self):
        folder_name = "Folder_Excelfiles_" + datetime.now().now().strftime("%Y-%m-%d_%H_%M_%S")
        return folder_name

    def __create_folder(self,folder_name):
        assert not os.path.exists(folder_name)
        os.makedirs(folder_name, exist_ok=True)



    def run(self,file_name:str):
        if not os.path.exists(file_name):
            print("File path doesn't exist")
        else:
            print(">> Processing...")

            folder_name=self.__create_folder_name()
            self.__create_folder(folder_name)
            self.__extract_data(file_name, folder_name)




            # ----- Read students.csv for further processing

            # TODO: Step 2

            # TODO: Step 3
            # ----- For each student, generate a copy of template.xlsx containing the student information in the appropriate fields
            # ----- Store the generated student files in the generated/ folder using a naming scheme like "<identifier>.xlsx"
            # ----- Hint: the identifier of each student should be stored in the cell R2
            # ----- Hint: the following might help: https://openpyxl.readthedocs.io/en/stable/tutorial.html

            # ---- YOUR CODE ENDS HERE ----
            print(">> Finished processing.")
