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



