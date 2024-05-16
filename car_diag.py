import obd
import time

connection = obd.OBD() 

# Verify if the connection is established
if connection.is_connected():
    print("Connected to OBD-II adapter")
else:
    print("Failed to connect to OBD-II adapter")

# Get the car information 
vin = connection.query(obd.commands.GET_VIN)
calibration_id = connection.query(obd.commands.CALIBRATION_ID)
calibration_verification_number = connection.query(obd.commands.CALIBRATION_VERIFICATION_NUMBER)

# Print the vehicle information
print("Vehicle information : ")
print("Vin number is : " + vin.value)
print("Calibration ID : ", calibration_id.value)
print("Calibration verification number : ", calibration_verification_number.value)


#get the engine trouble codes
codes = connection.query(obd.commands.GET_DTC)

print ("\n Engine trouble codes : ")
for code in codes.value:
    print(code)
    
# Delete the trouble codes
connection.query(obd.commands.CLEAR_DTC)
print("Trouble codes cleared")


# Get the engine details in real time
while True :
    rpm = connection.query(obd.commands.RPM) # RPM = Revolutions Per Minute
    speed = connection.query(obd.commands.SPEED) # Speed = Speed in km/h
    load = connection.query(obd.commands.ENGINE_LOAD) # Load = Engine load in %
    coolant_temperature = connection.query(obd.commands.COOLANT_TEMP) # Coolant temperature in Celsius
    
    print("RPM : ", rpm.value)
    print("Speed : ", speed.value)
    print("Engine load : ", load.value)
    print("Coolant temperature : ", coolant_temperature.value)
    
    time.sleep(1)



