import urllib.parse
import requests



main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "pg8GtHuXt6MtC95vhRGUCRjiqrzZnfIP"    # You should use your own key 
while True:
    orig = input ("Starting Point/city :")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination Point/city :")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Km/hr: " + str("{:.2f}".format(((json_data["route"]["distance"])*1760)/3600)))
        print("Mileage(Km/l): " + str("{:.2f}".format(100/(json_data["route"]["distance"])*3.78)))
        print("Arrival Time:   " + (json_data["route"]["formattedTime"]))
        print("-----------------Distance in different units!-----------------")
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1760)))
        print("-----------------Fuel Used in different units-----------------")
        print("Fuel Used(ltr):      " + str("{:.2f}".format((json_data["route"]["distance"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
    elif json_status == 402:
        print("******************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("******************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("********************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")