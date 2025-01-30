import pyinputplus as pyip
from colorama import Fore, Back, Style, init

#Creating a function
def main():
    #Setting Up Loop
    while True:
        conversion_selection = pyip.inputMenu(['Celsius to Farenheit', 'Farenheit to Celsius'], numbered=True)
        print(conversion_selection)
        temperature_selection = pyip.inputInt('What is the temperature you want to convert?: ')
    
        #Conditonals

        #If Celsius to Farenheit, do conversion and return the value to the user
        if conversion_selection == 'Celsius to Farenheit':
            Farenheit_Output = round((temperature_selection * 9/5)+32)
            print(Fore.BLACK + Back.WHITE + f"{Farenheit_Output} degrees Farenheit")
            print(Style.RESET_ALL)
        #If Farenheit to Celsius, do conversion and return the value to the user
        elif conversion_selection == 'Farenheit to Celsius':
            Celsius_Output = round((temperature_selection - 32)*5/9)
            print(Fore.BLACK + Back.WHITE + f"{Celsius_Output} degrees Celsius")
            print(Style.RESET_ALL)

        #Let user choose to continue the program or exit
        loopCondition = pyip.inputMenu(['Do Another Conversion', 'Exit'], numbered=True)
        if loopCondition == 'Do Another Conversion':
            pass
        elif loopCondition == 'Exit':
            print('Thank you for using the Temperature Converter.')
            break

main()
