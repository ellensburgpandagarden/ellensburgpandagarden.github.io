from src.entree import Entree
from src.family_dinners import FamilyDinner
from src.lunch_combination import LunchCombination
from src.dinner_combination import DinnerCombination
from src.lunch_menu import LunchMenu
from src.traditional_chinese_menu import TraditionalChineseMenu

import os
import time
from configparser import ConfigParser

class Driver:
    def __init__(self):
        configur = ConfigParser()
        configur.read('config.ini')
        # Set menu variable
        self.menu = configur.get("menu", "name_of_menu")

        # Set directory variable name
        self.directoryName = configur.get("createDirectory", "directoryName")

        # Set input file variables 
        self.entreeInputName = configur.get("input_files", "entree_input_name")
        self.familyDinnersInputName = configur.get("input_files", "familyDinners_input_name")
        self.lunchCombinationInputName = configur.get("input_files", "lunchCombination_input_name")
        self.dinnerCombinationInputName = configur.get("input_files", "dinnerCombination_input_name")
        self.lunchMenuInputName = configur.get("input_files", "lunchMenu_input_name")
        self.traditionalChineseMenuInputName = configur.get("input_files", "traditionalChineseMenu_input_name")

        # Set output file variables 
        self.entreeOutputName = configur.get("output_files", "entree_output_name")
        self.familyDinnersOutputName = configur.get("output_files", "familyDinner_output_name")
        self.lunchCombinationOutputName = configur.get("output_files", "lunchCombination_output_name")
        self.dinnerCombinationOutputName = configur.get("output_files", "dinnerCombination_output_name")
        self.lunchMenuOutputName = configur.get("output_files", "lunchMenu_output_name")
        self.traditionalChineseMenuOutputName = configur.get("output_files", "traditionalChineseMenu_output_name")

    def createdDirectory(self):
        directoryName = self.directoryName
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, directoryName)

        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
            return True
        
        count = 1
        while os.path.exists(final_directory + str(count)):
            count += 1
            print(count)
        
        os.makedirs(final_directory + str(count))
        self.directoryName = final_directory + str(count)
        return True

    def createMenu(self):
        if not self.createdDirectory():
            print("There already exist a directory with the same output name. Try again")
            return 0

        else:
            try:
                Entree.createEntree(self.menu, self.entreeInputName, self.entreeOutputName, self.directoryName)
                FamilyDinner.createFamilyDinner(self.menu, self.familyDinnersInputName, self.familyDinnersOutputName, self.directoryName)
                LunchCombination.createLunchCombination(self.menu, self.lunchCombinationInputName, self.lunchCombinationOutputName, self.directoryName)
                LunchMenu.createLunchMenu(self.menu, self.lunchMenuInputName, self.lunchMenuOutputName, self.directoryName)
                DinnerCombination.createDinnerCombination(self.menu, self.dinnerCombinationInputName, self.dinnerCombinationOutputName, self.directoryName)
                TraditionalChineseMenu.createTraditionalChineseMenu(self.menu, self.traditionalChineseMenuInputName, self.traditionalChineseMenuOutputName, self.directoryName)
                return 1
            
            except:
                return 0

driver = Driver()
if (driver.createMenu() == 1):
    print("--------------------------------------------------------------------------------------------------")
    print("Successfully generated the word documents! Check the Output folder to see the generated documents!")
    print("--------------------------------------------------------------------------------------------------")
    time.sleep(5)
else:
    print("--------------------------------------------------------------------------------------------------")
    print("An error has occurred while trying to generate the word documents")
    print("--------------------------------------------------------------------------------------------------")
    time.sleep(5)