//SAMBIT KUMAR MISHRA - EM WAVES ASSIGNMENT - SUBMITTED ON 20 MAY 2020

// Assume that both of the semi-infinite regions are either vaccuum or perfect/ideal dielectric (i.e. conductivity is 0)
// Make sure that both of the semi-infinite regions are not identical.
// We will assume that the coordinate axes are aligned along the interface and the wave is assumed to travel at an angle wrt media interface.
// Assume that the media are isotropic in their respective semi-infinite region
// Value of all angles and phase are in radians

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<complex.h>

// float a=0,b=0,c=0,d=0,m=0,n=0;
float Eo[6]; //This array will store the input values of coefficients of Eo
float Q[4]; // Angles
int i=0,poi=0,pod=0,polarisation=0;
float dp[4]; // Dielectric properties of medium 1 and medium 2 combined-dp stands for the dielectric properties
float n[2]; // For storing the intrinsic impedance of medium 1 and medium 2 combined
float B[2]; // For storing the phase constant values
float arr_phase[2]; //Final phase values to be stored in format of arr_phase[transmitted,reflected]
float arr_magnitude[2]; // Final magnitude values to be stored in format of arr_magnitude[transmitted,reflected]
float transmitted_angle=0; // For storing the value of transmitted angle
float a1=0,b1=0,a2=0,b2=0,reflection_coefficient=0,transmission_coefficient=0,Ei=0;
float ba[2]; // For storing brewster angle values [perpendicular,parallel]
//=============================================================================================================================================================


int main()
{	
	//Description of the sign convention and variables used in this program
	printf("Assume that the complex Electric field is given by the equation: E = ((a+jb)x^ + (c+jd)y^ + (m+jn)z^)e*exp(-j*B*(xcos(Qx)+ycos(Qy)+zcos(Qz))) \n");
	printf("Where ^ means cap, eg. x^ means unit vector in direction of x \n");
	printf("j = complex imaginary number analogous to i in maths \n");
	printf("e = natural log base\n");
	printf("a,c,m are real coefficients whereas b,d,n are complex coefficients of imaginary values of Eo \n");
	printf("Qx,Qy,Qz represent the angle made by the incident electric field wrt x,y,z axes respectively \n\n");
//==============================================================================================================================================================

	//From here onwards the user will input the values of the respective variables
	printf("Enter the values of a,b,c,d,m,n sequentially in this exact same order- separated by spaces:\n");
	scanf("%f%f%f%f%f%f",&Eo[0],&Eo[1],&Eo[2],&Eo[3],&Eo[4],&Eo[5]);

	printf("Enter the values of incident angles wrt different axes, given by Qx,Qy,Qz in this exact same order- separated by spaces:\n");
	scanf("%f%f%f",&Q[0],&Q[1],&Q[2]); 
	
	printf("Enter the permittivity_medium1,permeability_medium1,permittivity_medium2,permeability_medium2 in this exact same order- separated by spaces:\n");
	printf("The two media must not be identical\n");
	scanf("%f%f%f%f",&dp[0],&dp[1],&dp[2],&dp[3]); // dp = [epsilon1,mu1,epsilon2,mu2]

	printf("Enter the plane of incidence: \n");
	printf("Type 1 for XY, 2 for YZ and 3 for XZ\n");
	scanf("%d",&poi);

	printf("Enter the dielectric plane: \n");
	printf("Type 1 for XY, 2 for YZ and 3 for XZ\n");
	scanf("%d",&pod);

	printf("Enter the incident angle wrt normal to the plane of incidence: \n");
	scanf("%f",&Q[3]); // Incident wave, reflected and transmitted wave will lie on this plane

//===============================================================================================================================================================
	//For identification of polarisation of wave

	if (poi == 1)
	{
		if (cos(Q[2])==0)
		{
			polarisation = 1; //Perpendicular polarisation
		}
		else if (sin(Q[2])==0)
		{
			polarisation = 0; //Parallel polarisation
		}
	}

	else if (poi == 2)
	{
		if (cos(Q[0])==0)
		{
			polarisation = 1; //Perpendicular polarisation
		}
		else if (sin(Q[0])==0)
		{
			polarisation = 0; //Parallel polarisation
		}
	}

	else if (poi == 3)
	{
		if (cos(Q[1])==0)
		{
			polarisation = 1; //Perpendicular polarisation
		}
		else if (sin(Q[1])==0)
		{
			polarisation = 0; //Parallel polarisation
		}
	}

//===============================================================================================================================================================
	//Calculation of the Brewster angles in case of the parallel and perpendicular polarisations
	ba[0] = atan(sqrt(dp[3]/dp[1])*sqrt(((dp[3]*dp[0])-(dp[1]*dp[2])) / ((dp[3]*dp[2])-(dp[1]*dp[0]))));
	ba[1] = atan(sqrt(dp[3]/dp[1])*sqrt(((dp[1]*dp[2])-(dp[3]*dp[0])) / ((dp[3]*dp[2])-(dp[1]*dp[0]))));

//===============================================================================================================================================================
//The case when incident wave just grazes through the plane of dielectric interface
//In this case no reflection or transmission of wave is possible. This is an exceptional case.
if (cos(Q[3])==0)
{
	printf("\nNO TRANSMISSION OR REFLECTION POSSIBLE IN THIS CASE: BECAUSE THE WAVE GRAZES THROUGH THE PLANE OF INTERFACE\n");
}
//===============================================================================================================================================================
else//This is where our actual calculations begin.
{	//Calculation of intrinsic impedance
	//mu1 and mu2 relative, are 1 because the medium is non-magnetic
	n[0] = (120*3.14)/(sqrt((dp[0])/(dp[1]))); // For medium 1  
	n[1] = (120*3.14)/(sqrt((dp[2])/(dp[3]))); // For medium 2
	B[0] = (sqrt(dp[3]*dp[2]));
	B[1] = (sqrt(dp[1]*dp[0]));

	//For the calculation of transmitted and reflection phase - Concept in page 219-220 point no 1 = RK Shevgaonkar

	//CASE-1: When the incident wave is at an angle less than Brewster's Angle
	if (((B[0]/B[1])*sin(Q[3]))<1)
	{
		transmitted_angle = asin((B[0]/B[1])*sin(Q[3]));

		//For the case of perpendicular polarisation
		if (polarisation == 1)
		{
			a1 = n[0]*(cos(transmitted_angle)); 
			b1 = n[1]*(cos(Q[3]));

			reflection_coefficient = (b1-a1)/(b1+a1);
			transmission_coefficient = (2*b1)/(b1+a1);

			if (reflection_coefficient>=0)
			{
				arr_phase[1]= (2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*sin(Q[3]),2))) / (n[0]*cos(Q[3])));
			}
			else
			{
				arr_phase[1]= (-2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*sin(Q[3]),2))) / (n[0]*cos(Q[3]))); // A phase change of Pi
			}

			if (transmission_coefficient>=0)
			{
				arr_phase[0]= (2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(Q[3]),2))) / (n[0]*sin(Q[3])));
			}
			else
			{
				arr_phase[0]= (-2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(Q[3]),2))) / (n[0]*sin(Q[3]))); // A phase change of Pi
			}
			
			//Now we will find the magnitude of transmitted and reflected waves.
			for(i=0;i<6;i++)
			{
				Ei += pow(Eo[i],2); // We have to take square root of this value(Ei) to obtain Magnitude of incident electric field.
			}

			arr_magnitude[0] = transmission_coefficient*(sqrt(Ei));
			arr_magnitude[1] = reflection_coefficient*(sqrt(Ei));
		}
	//===============================================================================================================================================================
			
		//For the case of parallel polarisation
		else if (polarisation == 0)
		{
			a2 = n[1]*(cos(transmitted_angle)); 
			b2 = n[0]*(cos(Q[3]));

			reflection_coefficient = (b2-a2)/(b2+a2);
			transmission_coefficient = (2*b1)/(b2+a2);
			
			if (reflection_coefficient>=0)
			{
				arr_phase[1]= (2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*sin(Q[3]),2))) / (n[0]*cos(Q[3])));
			}
			else
			{
				arr_phase[1]= (-2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*sin(Q[3]),2))) / (n[0]*cos(Q[3]))); // A phase change of Pi
			}

			if (transmission_coefficient>=0)
			{
				arr_phase[0]= (2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(Q[3]),2))) / (n[0]*sin(Q[3])));
			}
			else
			{
				arr_phase[0]= (-2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(Q[3]),2))) / (n[0]*sin(Q[3]))); // A phase change of Pi
			}
			
			//Now we will find the magnitude of transmitted and reflected waves.
			for(i=0;i<6;i++)
			{
				Ei += pow(Eo[i],2); // We have to take square root of this value(Ei) to obtain Magnitude of incident electric field.
			}

			arr_magnitude[0] = transmission_coefficient*(sqrt(Ei));
			arr_magnitude[1] = reflection_coefficient*(sqrt(Ei));
		}			
	}
	//==============================================================================================================================================================
	
	//CASE-2: When the incident wave is at an angle greater than the Brewster's Angle
	else if (((B[0]/B[1])*sin(Q[3]))>1)
	{
		printf("\nThis is the case of Total Internal Reflection\n");
		transmitted_angle = casin((n[1]/n[0])*sin(Q[3])); //For calculation of complex arc sin

		//For the case of perpendicular polarisation
		if (polarisation == 1)
		{
			a1 = n[0]*(ccos(transmitted_angle)); 
			b1 = n[1]*(ccos(Q[3]));

			// reflection_coefficient = (b1-a1)/(b1+a1);
			reflection_coefficient = (b1 - I*n[0]*(sqrt(pow((B[0]/B[1])*sin(Q[3]),2)-1))) / (b2 + I*n[0]*(sqrt(pow((B[0]/B[1])*sin(Q[3]),2)-1)));
			// transmission_coefficient = (2*b1)/(b1+a1);
			
			arr_phase[1]= (-2)*atan((n[1]*(sqrt(pow((B[0]/B[1])*sin(Q[3]),2)-1))) / (n[0]*cos(Q[3])));

			//We wont calculate the coefficient of transmission as it is not provided in the book. It can be edited later.			
			// if (transmission_coefficient>=0)
			// {
			// 	arr_phase[0]= (2)*atan((n[1]*(sqrt(1-(pow((B[0]/B[1])cos(Qi)),2)))) / (n[0]*sin(Qi)));
			// }
			// else
			// {
			// 	arr_phase[0]= (-2)*atan((n[1]*(sqrt(1-(pow((B[0]/B[1])cos(Qi)),2)))) / (n[0]*sin(Qi))); // A phase change of Pi
			// }
			
			//Now we will find the magnitude of transmitted and reflected waves.
			for(i=0;i<6;i++)
			{
				Ei += pow(Eo[i],2); // We have to take square root of this value(Ei) to obtain Magnitude of incident electric field.
			}

			arr_magnitude[0] = transmission_coefficient*(sqrt(Ei));
			arr_magnitude[1] = reflection_coefficient*(sqrt(Ei));
		}
	//===============================================================================================================================================================
			
		//For the case of parallel polarisation
		else if (polarisation == 0)
		{
			a2 = n[1]*(ccos(transmitted_angle)); 
			b2 = n[0]*(ccos(Q[3]));

			reflection_coefficient = (b1 - I*n[1]*(sqrt(pow((B[0]/B[1])*sin(Q[3]),2)-1))) / (b2 + I*n[1]*(sqrt(pow((B[0]/B[1])*sin(Q[3]),2)-1)));
			// transmission_coefficient = (2*b1)/(b2+a2);

			arr_phase[1]= (-2)*atan((n[1]*(sqrt(pow((B[0]/B[1])*sin(Q[3]),2)-1)))) / (n[0]*cos(Q[3]));
					
			// if (transmission_coefficient>=0)
			// {
			// 	arr_phase[0]= (2)*atan((n[1]*(sqrt(1-(pow((B[0]/B[1])cos(Qi)),2)))) / (n[0]*sin(Qi)));
			// }
			// else
			// {
			// 	arr_phase[0]= (-2)*atan((n[1]*(sqrt(1-(pow((B[0]/B[1])cos(Qi)),2)))) / (n[0]*sin(Qi))); // A phase change of Pi
			// }
			
			//Now we will find the magnitude of transmitted and reflected waves.
			for(i=0;i<6;i++)
			{
				Ei += pow(Eo[i],2); // We have to take square root of this value(Ei) to obtain Magnitude of incident electric field.
			}

			// arr_magnitude[0] = transmission_coefficient*(sqrt(Ei)); // BECAUSE WE ARE NOT FINDING TRANSMISSION PARAMETERS AS THEY ARE NOT MENTIONED IN BOOK
			arr_magnitude[1] = reflection_coefficient*(csqrt(Ei));
			arr_magnitude[0] = 0;
		}

	}
	//==============================================================================================================================================================

	//CASE-3 : When angle of incidence is equal to the Brewster's Angle
	else if (((B[0]/B[1])*sin(Q[3]))==1)
	{
		printf("\nIn this case no reflection will take place and the wave will graze through the plane of interface\n");

		//For case of perpendicular polarisation
		if (polarisation == 1)
		{
			transmitted_angle = acos((n[1]*cos(ba[0]))/n[0]);
			transmission_coefficient = (2*n[0]*cos(ba[0])) / ((n[1]*cos(ba[0]))+(n[0]*cos(transmitted_angle)));
			if (transmission_coefficient>=0)
			{
				arr_phase[0]= (2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(ba[0]),2))) / (n[0]*sin(ba[0])));
			}
			else
			{
				arr_phase[0]= (-2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(ba[0]),2))) / (n[0]*sin(ba[0]))); // A phase change of Pi
			}
		}

		//For the case of parallel polarisation
		else if (polarisation == 0)
		{
			transmitted_angle = acos((n[0]*cos(ba[1]))/n[1]);
			transmission_coefficient = (2*n[0]*cos(ba[0])) / ((n[1]*cos(ba[0]))+(n[0]*cos(transmitted_angle)));
			if (transmission_coefficient>=0)
			{
				arr_phase[0]= (2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(ba[1]),2))) / (n[0]*sin(ba[1])));
			}
			else
			{
				arr_phase[0]= (-2)*atan((n[1]*sqrt(1-pow((B[0]/B[1])*cos(ba[1]),2))) / (n[0]*sin(ba[1]))); // A phase change of Pi
			}
		}	


		//Now we will find the magnitude of transmitted wave.
		for(i=0;i<6;i++)
		{
			Ei += pow(Eo[i],2); // We have to take square root of this value(Ei) to obtain Magnitude of incident electric field.
		}

		arr_magnitude[0] = transmission_coefficient*(sqrt(Ei));
		// arr_magnitude[1] = reflection_coefficient*(sqrt(Ei)); 
		// WONT BE APPLICABLE BECAUSE REFLECTION DOESNT TAKE PLACE IN THIS CASE
		arr_magnitude[1] = 0;
		arr_phase[1] = 0;
	}

//==================================================================================================================================================================
//The final required values using the input values are printed below
printf("\nThe phase of transmitted wave is %f",arr_phase[0]);
printf("\nThe phase of reflected wave is %f",arr_phase[1]);
printf("\nThe magnitude of transmitted wave is %f",arr_phase[0]);
printf("\nThe magnitude of reflected wave is %f",arr_phase[1]);

}

printf("\nThese were your final results. THANK YOU\n");
//==================================================================================================================================================================
return 0;
}
//THE END
//FOR QUERIES/REMARKS CONTACT- sambitmishra1968@gmail.com


