#P5T1
#Kilometer Converter
#Sutcliffe
#April 22, 2018

def askForKilometers():
    userKilo = float( input("Please enter the distance in Kilometers:"))
    return userKilo

def Show_miles(userKilo ):
    miles = userKilo * 0.6214
    return miles

def main():
    userKiloEntered = askForKilometers()
    convertedMiles = Show_miles( userKiloEntered )

    print( userKiloEntered, "kilometers converted to miles is", format( convertedMiles, ".2f" ), "miles" )
                
main()
