# H_V.dat - lattice Hamiltonian. It can be calculated by fortran code
import numpy as np

chi_ch_imp_pi_pi = complex(0.0, 0.0)
chi_ch_loc_pi_pi = complex(0.0, 0.0)

######################
#
#  input file
#
######################

V = 0.5 # non-local interaction
kpt = 50  # mesh 
qx = int(kpt / 2)
qy = int(kpt / 2)

######################
#
#  input H_V.dat
#
######################

f = open('H_V.dat')
data = f.readlines()

intensity = [ [0.0] * np.int(kpt) for i in range(np.int(kpt))]

i = 0
j = 0
for str in data:
    value = str.split()
    for val in value:
        intensity[i][j] = float(val)
        i += 1
        if (i == kpt):
            i = 0
            j += 1
f.close()

# find a value in (pi; pi) = (ktp /2; ktp /2)
H_V = intensity[int(kpt / 2)][int(kpt / 2)]
print "H_V( pi; pi) = ", H_V

######################
#
#  read chi impurity
#
######################

f = open("chi_n.dat", "r")
lines = f.readlines()

i = 0
for line in lines:
    if (i == 0):
        params    = line.split()
        nu        = params[0]
        chi_0_imp = complex(float(params[1]), float(params[2]))
    else:
        continue
f.close()

######################
#
#  read chi local
#
######################

f = open("Chi_loc.dat", "r")
lines = f.readlines()

i = 0
for line in lines:
    if (i == 0):
        params    = line.split()
        chi_0_loc = complex(float(params[1]), float(params[2]))
    else:
        continue
f.close()

######################
#
#  read lambda
#
######################

f = open("lambda.dat", "r")
lines = f.readlines()

i = 0
for line in lines:
    if (i == 0):
        params    = line.split()
        lambda_0 = complex(float(params[1]), float(params[2]))
    else:
        continue
f.close()

######################
#
# calculation of
# static charge susceptibility 
# at the zero matsubara
#
######################


chi_ch_imp_pi_pi = 1.0 / (1.0 / chi_0_imp + lambda_0 - H_V)
chi_ch_loc_pi_pi = 1.0 / (1.0 / chi_0_loc + lambda_0 - H_V)

print "Chi static impurity (pi, pi) = ", chi_ch_imp_pi_pi
print "Chi static local (pi, pi) = ", chi_ch_loc_pi_pi
