"""
Program: Wind Chill Weather Report Calculator
Author: Kenny Truong
Course: CS 115
Description: This program will calculating WCT at several different locations
    throughout a city, where air temperature and wind velocity have been recorded.
    Please do note that extra credit was done.
        The program will reject negative wind velocities.
        The program will reject extreme temperatures (high and low) reported on the surface of the earth.
        The program will reject wind velocities that exceed the speed of sound.
"""

import sys


def main():
    allwct = 0
    leastWCT = float("inf")
    leastWCTLocation = ""
    leastAirTemp = float("inf")
    leastAirTempLocation = ""
    allAir_temp = 0
    allWind_velo = 0
    highestWindVelo = float("-inf")
    highestWindVeloLocation = ""

    print("==> Windchill Temperature (WCT) Weather Report Calculator <==")

    nLocations = int(input("Select the number of locations for the report: "))

    if nLocations <= 0:
        print("Error:", nLocations, "is not a valid input.")
        sys.exit(-1)

    nDecimal = int(input("Select decimal precision for the report [1--4]: "))

    if nDecimal < 1 or nDecimal > 4:
        print("Error:", nDecimal, "is not in the range 1--4.")
        sys.exit(-1)

    for i in range(nLocations):
        location = input("Enter name of ** Location " + str(i+1) + " **: ")
        air_temp = int(input("\tEnter air temperature [in deg F]: "))

        if air_temp >= 150 or air_temp <= -150:
            print("Sorry, that temperature is absurd and unheard of.")
            sys.exit(-1)  # Any number >= 150 or <= -150 will not be accepted.

        wind_velo = int(input("\tEnter wind velocity [in mph]: "))

        if wind_velo <= -1:
            print("Sorry, negative numbers are not allowed.")
            sys.exit(-1)

        if wind_velo >= 767.269:
            print("Wind velocity will not exceed the speed of sound, unless Coldplay is playing.")
            sys.exit(-1)

        wct = 35.74 + 0.6215 * air_temp - 35.75 * (wind_velo ** 0.16) + 0.4275 * air_temp * (wind_velo**0.16)
        print("\tWCT is", round(wct, nDecimal), "deg F.")  # This will round WCT depending on # of nDecimal.
        allwct = allwct + wct
        allAir_temp = allAir_temp + air_temp
        allWind_velo = allWind_velo + wind_velo

        if wct < leastWCT:
            leastWCTLocation = location
            leastWCT = min(wct, leastWCT)  # This line will set the minimum WCT to leastWCT.

        if air_temp < leastAirTemp:
            leastAirTempLocation = location
            leastAirTemp = min(air_temp, leastAirTemp)

        if wind_velo > highestWindVelo:
            highestWindVeloLocation = location
            highestWindVelo = max(wind_velo, highestWindVelo)

    print("\n*** Summary ***")
    print("WCT")
    print("\tAvg recorded WCT:", round((float(allwct)/nLocations), nDecimal), "deg F")
    print("\tLocation with lowest WCT: ", leastWCTLocation, " (", round(leastWCT, nDecimal), " F)", sep="")
    print("Air Temperature")
    print("\tAvg recorded air temperature:", float(allAir_temp/nLocations), "deg F")
    print("\tLocation with lowest air temperature: ", leastAirTempLocation, " (", float(round(leastAirTemp, nDecimal)),
          " F)", sep="")
    print("Wind Velocities")
    print("\tAvg recorded wind velocity:", float(allWind_velo/nLocations), "mph")
    print("\tLocation with highest wind velocity: ", highestWindVeloLocation, " (",
          float(round(highestWindVelo, nDecimal)), " mph)", sep="")

main()
