# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
E_E = 0.081819221456

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
o_lat_deg = float('nan') #latitude in degrees 
o_lon_deg = float('nan') #longitude in degrees 
o_hae_km  = float('nan') #height above ellipsoid in km 
s_km      = float('nan') #south coordinate 
e_km      = float('nan') #east coordinate  
z_km      = float('nan') #zenith coordinate 

# parse script arguments
if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km  = float(sys.argv[3])
    s_km      = float(sys.argv[4])
    e_km      = float(sys.argv[5])
    z_km      = float(sys.argv[6])
else:
    print(\
        'Usage: '\
            'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae s_km e_km z_km'\
    )
    exit()

# write script below this line
o_lat_rad = o_lat_deg*(math.pi/180)
o_lon_rad = o_lon_deg*(math.pi/180)
C_theta = math.cos(o_lon_rad)
S_theta = math.sin(o_lon_rad)
C_phi = math.cos(o_lat_rad)
S_phi = math.sin(o_lat_rad)

r_ecef = [C_theta*S_phi*s_km + C_theta*C_phi*z_km - S_theta*e_km,
          S_theta*S_phi*s_km + S_theta*C_phi*z_km + C_theta*e_km,
          -C_phi*s_km + S_phi*z_km]


#calculate (ecef_x_km, ecef_y_km, ecef_z_km)
ecef_x_km, ecef_y_km, ecef_z_km = r_ecef 

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
