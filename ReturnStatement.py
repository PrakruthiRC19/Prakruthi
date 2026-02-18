class SkyScanner:

    def searchFlight(self, source, destination): # source and destinmation is a input parameter stored in stack because it is a local variable.

        NoOfFlights=1
        NameOfAirlines="INDIGO"

        return "No of Flights is", NoOfFlights, "and Name of Airlines", NameOfAirlines # return statement is always wrote in end of the function itself.
    
s=SkyScanner()

# option 1 to capturing data from return

FlightInfo=s.searchFlight("Bangalore", "Bangkok")
print(FlightInfo)

# option 2 to capturing data from return

print(s.searchFlight("Hyderbad", "Bangalore"))