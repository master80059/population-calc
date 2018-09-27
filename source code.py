# program: population calc
# written by: steve W Cornell
# date: 9-25-2018
#description: take 4 user inputs prints the inputs and population calc out in a table format
#challenges: context to what the assinment was looking  for. plus mising more advanced knolege into it.
# time spent: 4 hourss research on wrong question solution idea. 10 min once I found out what the intent was of the question.  and removed everything but what i new.

#imports needed
import sys
# key words table
# SO = starting organisms input
# SPI = inputed population percentage
# SD = input of howmany days of increase will happen
# CD = Current day count var
# PI = the percent increase in proper math format
# CO = current organism var

# setVars

SO = int(input ( "how many starting orgaanisms?"))
sys.stdout.flush()
SPI = float(input( "percentage increase per day?"))
sys.stdout.flush()
SD = int(input(" how many days of increase?" ))
sys.stdout.flush()
# Convert percent to proper format
PI = SPI / 100
#created volitial var.
CO = SO

#print function
sys.stdout.flush()
   # header of table
print("\nday\testimated population\n<><>\t<><M><S><A><>")

#table loop SD + 1 so itdoes day 1 to the day you input.
for CD in range ( 1, SD + 1 ):
    #print table per day
    print ( "day", CD ,"\t","organisms", CO )
# once day is printed then add increase of population to current population done last so day one is shown

    CO = CO + (PI * CO )
   
else:
#pervents program from closing right off the bat.
    input("press enter to exit")
