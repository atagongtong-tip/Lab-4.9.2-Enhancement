import urllib.parse
import requests
import time
import datetime

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "6e2VRrxJZLUOJTCyDcYbLAgceo9vQAOR"    # You should use your own key 


Time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time is :", Time)

while True:
    orig = input ("Source City :")
    if orig == "quit" or orig == "q":
        break
    dest = input("Dest City :")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Km/hr: " + str("{:.2f}".format(((json_data["route"]["distance"])*1760)/3600)))
        print("Mileage(Km/l): " + str("{:.2f}".format(100/(json_data["route"]["distance"])*3.78)))
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Arrival Time:   " + (json_data["route"]["formattedTime"]))
        print("-----------------Distance in different units!-----------------")
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Miles: " + str(json_data["route"]["distance"]))
        print("Yards: " + str("{:.2f}".format((json_data["route"]["distance"])*1760)))
        print("-----------------Fuel Used in different units-----------------")
        print("Fuel Used(ltr):      " + str("{:.2f}".format((json_data["route"]["distance"])*3.78)))
        print("Fuel Used(Imperial Gal):      " + str("{:.2f}".format((json_data["route"]["distance"])*0.8327)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
    elif json_status == 402:
        print("****************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("****************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("******************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")