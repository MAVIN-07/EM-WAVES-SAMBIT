#CREATED AND MAINTAINED BY: SAMBIT KUMAR MISHRA
#Email-ID: sambitmishra1968@gmail.com

import math
import cmath
import matplotlib.pyplot as plt 
import matplotlib.image as img
#===========================================================================================================================================================
# Defining lists to use through this program
Eo = []
Q = []
dp = []					#[permittivity1,permeability1,permittivity2,permeability2]
n = [0,0]
B = [0,0]
ba = [0,0]				#[perpendicular,parallel]
arr_phase = [0,0]		#[transmission,reflection]
arr_magnitude = [0,0]	#[transmission,reflection]
critical_angle = 0
#===========================================================================================================================================================
#Printing on the screen- Assumptions and sign conventions to be used.
print("ASSUMPTIONS-NOTE THESE BEFORE PROCEEDING")
print("_________________________________________________________________________________________________________________________________________________")
print("")
print("Assume that the complex Electric field is given by the equation: E = ((a+jb)x^ + (c+jd)y^ + (m+jn)z^)e*exp(-j*B*(xcos(Qx)+ycos(Qy)+zcos(Qz)))")
print("Where ^ means cap, eg. x^ means unit vector in direction of x")
print("j = complex imaginary number analogous to i in maths")
print("e = natural log base")
print("a,c,m are coefficients of real part whereas b,d,n are coefficients of imaginary part of Eo")
print("Qx,Qy,Qz represent the angle made by the incident electric field wrt x,y,z axes respectively")
print("Qi is the incident angle of wave wrt to the normal to the plane of incidence")
print("_________________________________________________________________________________________________________________________________________________")
print("")


#===========================================================================================================================================================
# TAKING THE INPUTS FROM THE USER

try:
	Eo = list(map(float, input("Enter the values of a,b,c,d,m,n in this exact order separated by space= ").split()))
	# w = float(input("Enter the frequency of the EM Wave in Hz= "))#We dont have to use because in B value it will get cancelled Nr and Dr
	Q = list(map(float, input("Enter the values of Qx,Qy,Qz,Qi in this exact order separated by spaces= ").split()))


	# Enter 0 if degrees and 1 if radians
	unit = int(input("Enter the unit of angle chosen:- TYPE '0' for degrees, TYPE '1' for radians "))
	if unit == 0:
	    Q[0] = math.radians(Q[0])
	    Q[1] = math.radians(Q[1])
	    Q[2] = math.radians(Q[2])
	    Q[3] = math.radians(Q[3])
	# If the input type is chosen as radians then leave the value as it is.

	#This loop will exit only if the user enters proper values of dielectric properties
	while 1:
		dp = list(map(float, input(
		    "Enter the values of permittivity_medium1, permeability_medium1, permittivity_medium2, permeability_medium2 in "
		    "this same order separated by space= ").split()))
		if dp[3]*dp[2] == dp[1]*dp[0]:
			print("ERROR: Enter the values as per assumptions")
		else:
			break

	print("")
	print("For the following two categories:- TYPE '1' for XY, TYPE '2' for YZ, TYPE '3' for XZ")
	print("")

	poi = int(input("Enter the plane of interface= "))
	pod = int(input("Enter the plane of dielectric= "))
	#===========================================================================================================================================================
	#CALCULATION OF POLARISATION OF WAVE

	polarisation = 0
	#Declaration of polarisation variable for using in program.

	if poi == 1:
		if math.cos(Q[2]) == 0:
			polarisation = 1  # Perpendicular polarisation
		elif math.sin(Q[2]) == 0:
			polarisation = 0  # Parallel polarisation

	elif poi == 2:
		if math.cos(Q[0]) == 0:
			polarisation = 1  # Perpendicular polarisation
		elif math.sin(Q[0]) == 0:
			polarisation = 0  # Parallel polarisation

	elif poi == 3:
		if math.cos(Q[1]) == 0:
			polarisation = 1  # Perpendicular polarisation
		elif math.sin(Q[1]) == 0:
			polarisation = 0  # Parallel polarisation

	#===============================================================================================================================================================
	#Calculation of the magnitude of Incident Electric Field: Absolute value of Eo
	Ei=0
	#Declaration of Ei variable
	for i in range(0, 6):
		Ei += Eo[i]**2  # We have to take square root of this value(Ei) to obtain Magnitude of incident electric field.
	#===============================================================================================================================================================
	#CALCULATION OF BREWSTER'S ANGLE
	#The square root value might come out to be negative hence complex square root must be taken into account so this step can be postponed

	# reading png image file 
	im = img.imread('EMWAVE_2.png') 
	  
	# show image 
	plt.imshow(im)

	#For Perpendicular Polarisation
	if ((dp[3]/dp[1])*(((dp[3]*dp[0])-(dp[1]*dp[2]))/((dp[3]*dp[2])-(dp[1]*dp[0])))) >= 0:
		ba[0] = math.atan(math.sqrt((dp[3]/dp[1])*(((dp[3]*dp[0])-(dp[1]*dp[2]))/((dp[3]*dp[2])-(dp[1]*dp[0])))))
	else:
		print("BREWSTER ANGLE IS NOT POSSIBLE FOR THIS CASE")

	#For Parallel Polarisation
	if ((dp[2]/dp[0])*(((dp[1]*dp[2])-(dp[3]*dp[0]))/((dp[3]*dp[2])-(dp[1]*dp[0])))) >= 0:
		ba[1] = math.atan(math.sqrt((dp[2]/dp[0])*(((dp[1]*dp[2])-(dp[3]*dp[0]))/((dp[3]*dp[2])-(dp[1]*dp[0])))))
	else:
		print("BREWSTER ANGLE IS NOT POSSIBLE FOR THIS CASE")

	#=====================================================================================================================================================================

	#The case when incident wave just grazes through the plane of dielectric interface
	#In this case no reflection or transmission of wave is possible. This is an exceptional case.
	if math.cos(Q[3]) == 0:
		print("NO TRANSMISSION OR REFLECTION POSSIBLE IN THIS CASE: BECAUSE THE WAVE GRAZES THROUGH THE PLANE OF INTERFACE")

	#ACTUAL CALCULATION BEGINS HERE
	else:

		n[0] = (120*math.pi)/(math.sqrt((dp[1])/(dp[0])))  	#For medium 1  
		n[1] = (120*math.pi)/(math.sqrt((dp[3])/(dp[2])))   #For medium 2
		B[0] = math.sqrt(dp[1]*dp[0])                       #For medium 1
		B[1] = math.sqrt(dp[3]*dp[2])                       #For medium 2

	    
		b1 = n[1] * math.cos(Q[3])
		b2 = n[0] * math.cos(Q[3])

	    
	    #==================================================================================================================================================================
	    #CASE-1: When the incident wave is at an angle greater than the critical Angle and medium 2 is rarer than medium 1
		if ((B[0] / B[1]) * math.sin(Q[3])) >= 1 and (dp[3]*dp[2])<=(dp[1]*dp[0]):
	    #==================================================================================================================================================================
			print("THIS IS THE CASE OF TOTAL INTERNAL REFLECTION")
			print("")
			critical_angle = math.asin(B[1]/B[0])

	        # reading png image file 
			im = img.imread('EMWAVE_TIR.png') 
	  
			# show image 
			plt.imshow(im)

			if (B[0] / B[1])*math.sin(Q[3]) > 1: 

				if polarisation == 1:
					reflection_coefficient = (b1 - 1j*(n[0]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1))) / (b1 + 1j*(n[0]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)))
					arr_phase[1] = (-2)*math.atan((n[0]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)) / b1)

				elif polarisation == 0:
					reflection_coefficient = (b2 - 1j*(n[1]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1))) / (b2 + 1j*(n[1]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)))
					arr_phase[1] = (-2)*math.atan((n[1]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)) / b2)

	        	#Calculation of magnitude
				arr_magnitude[0] = "N/A"
				arr_phase[0] = "N/A"
				arr_magnitude[1] = reflection_coefficient * math.sqrt(Ei)

			elif (B[0] / B[1]) * math.sin(Q[3]) == 1: 
	       		
				try:

					if Q[3] == critical_angle:
						if polarisation == 1:
							reflection_coefficient = (b1 - 1j*(n[0]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1))) / (b1 + 1j*(n[0]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)))
							arr_phase[1] = (-2)*math.atan((n[0]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)) / b1)

						elif polarisation == 0:
							reflection_coefficient = (b2 - 1j*(n[1]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1))) / (b2 + 1j*(n[1]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)))
							arr_phase[1] = (-2)*math.atan((n[1]*math.sqrt((((B[0]/B[1])*math.sin(Q[3]))**2)-1)) / b2)

			        	#Calculation of magnitude
						arr_magnitude[0] = "N/A"
						arr_phase[0] = "N/A"
						arr_magnitude[1] = reflection_coefficient * math.sqrt(Ei)

					else:
						print("ERROR: DISCREPANCY IN ANALYTICAL AND INPUT VALUES")
				except:
					print("ERROR!")

			else:
				print("ERROR: Please re-enter practical values in input")

	    #==================================================================================================================================================================
	    #CASE-2: When the wave is incident at Brewster's Angle
		elif Q[3]==ba[0] or Q[3]==ba[1]:
	    #==================================================================================================================================================================
		    #No reflection will take place in this case
			arr_magnitude[1] = "N/A"
			arr_phase[1] = "N/A"

		    # reading png image file 
			im = img.imread('EMWAVE_BA.png') 
	  
			# show image 
			plt.imshow(im)

			a1 = n[0] * math.cos(transmitted_angle)
			a2 = n[1] * math.cos(transmitted_angle)

		    #Case of perpendicular polarisation
		    #--------------------------------------------------------
			if polarisation == 1:
				transmission_coefficient = (2 * b1) / (b1 + a1)
				if transmission_coefficient >= 0:
					arr_phase[0] = (2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))

				else:
					arr_phase[0] = (-2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))  # A phase change of Pi

	            #Calculation of magnitude
				arr_magnitude[0] = transmission_coefficient * math.sqrt(Ei)
	            

	        #Case of parallel polarisation
	        #--------------------------------------------------------
			elif polarisation == 0:
				transmission_coefficient = (2 * b1) / (b2 + a2)
				if transmission_coefficient >= 0:
					arr_phase[0] = (2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))

				else:
					arr_phase[0] = (-2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))  # A phase change of Pi
	            
	            #Calculation of magnitude
				arr_magnitude[0] = transmission_coefficient * math.sqrt(Ei)


	    #==================================================================================================================================================================
	    #CASE-3: The general case of reflection and transmission
	    #if ((B[0] / B[1]) * math.sin(Q[3])) < 1:  
		else:		
	    #==================================================================================================================================================================
			transmitted_angle = math.asin(B[0]/B[1]) * math.sin(Q[3])
			a1 = n[0] * math.cos(transmitted_angle)
			a2 = n[1] * math.cos(transmitted_angle)

	        # reading png image file 
			im = img.imread('EMWAVE_2.png') 
	  
			# show image 
			plt.imshow(im)

	        # For the case of perpendicular polarisation
			if polarisation == 1:
	        #----------------------------------------------  
				reflection_coefficient = (b1 - a1) / (b1 + a1)
				transmission_coefficient = (2 * b1) / (b1 + a1)

				if reflection_coefficient >= 0:
	            	#Calculation of phase of wave after reflection or transmission is a bit tricky: Need to look into that
					arr_phase[1] = (2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.sin(Q[3]), 2))) / (n[0] * math.cos(Q[3])))

				else:
					arr_phase[1] = (-2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.sin(Q[3]), 2))) / (n[0] * math.cos(Q[3])))  # A phase change of Pi

	            
				if transmission_coefficient >= 0:
					arr_phase[0] = (2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))

				else:
					arr_phase[0] = (-2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))  # A phase change of Pi

	            #Calculation of magnitude
				arr_magnitude[0] = transmission_coefficient * math.sqrt(Ei)
				arr_magnitude[1] = reflection_coefficient * math.sqrt(Ei)
	            #----------------------------------------------------------------------------------------------------------------------------------       

	        # For the case of parallel polarisation
			elif polarisation == 0:
	        #-------------------------------------------        
				reflection_coefficient = (b2 - a2) / (b2 + a2)
				transmission_coefficient = (2 * b1) / (b2 + a2)

				if reflection_coefficient >= 0:
					arr_phase[1] = (2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.sin(Q[3]), 2))) / (n[0] * math.cos(Q[3])))

				else:
					arr_phase[1] = (-2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.sin(Q[3]), 2))) / (n[0] * math.cos(Q[3])))  # A phase change of Pi

				if transmission_coefficient >= 0:
					arr_phase[0] = (2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))

				else:
					arr_phase[0] = (-2) * math.atan((n[1] * math.sqrt(1 - math.pow((B[0] / B[1]) * math.cos(Q[3]), 2))) / (n[0] * math.sin(Q[3])))  # A phase change of Pi
	            
	            #Calculation of magnitude
				arr_magnitude[0] = transmission_coefficient * math.sqrt(Ei)
				arr_magnitude[1] = reflection_coefficient * math.sqrt(Ei)

	#======================================================================================================================================================================
	# The final required values using the input values are printed below
	print("__________________________________________________________________________")
	print("The phase of transmitted wave is 		" + str(arr_phase[0]))
	print("The phase of reflected wave is 			" + str(arr_phase[1]))
	print("The magnitude of transmitted wave is 	" + str(arr_phase[0]))
	print("The magnitude of reflected wave is 		" + str(arr_phase[1]))
	print("")
	print("These were your final results. THANK YOU")
	print("__________________________________________________________________________")
#======================================================================================================================================================================
except:
	# reading png image file 
	im = img.imread('SORRY.png') 
	  
	# show image 
	plt.imshow(im)
	print("__________________________________________")
	print("PLEASE RECHECK THE VALUES YOU HAVE ENTERED")
	print("__________________________________________")

#THE END
#FOR QUERIES/REMARKS CONTACT: SAMBIT KUMAR MISHRA (sambitmishra1968@gmail.com)