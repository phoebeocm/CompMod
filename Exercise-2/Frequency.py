"""
Phoebe O'Carroll-Moran, s1624742

Finds frequency of the oscillations

"""

def frequency(generic_list,time_list):

    """
        Calculates frequency of an oscillation
    """
    # creates a list of local maxima for the given list
    max_list = [i for i in range(1,(len(generic_list)-1)) if generic_list[i] > generic_list[i-1] and generic_list[i+1] ]
    periodic_list = []
    for j in max_list:
        periodic_list.append(time_list[j])
  
    wavelength = periodic_list[2] - periodic_list[1]

    frequency = 1/wavelength
    print("this is the frequency")
    print(frequency)
    
def energy_vals(generic_list):
    """
           Calculates maximum and  minimum values out of a list

          """
         # creates a list of local maxima for the given list
    max_vals = [generic_list[i] for i in range(1,(len(generic_list)-1)) if generic_list[i] > generic_list[i-1] and generic_list[i] > generic_list[i+1]]
    min_vals = [generic_list[i] for i in range(1,(len(generic_list)-1)) if generic_list[i] < generic_list[i-1] and generic_list[i] < generic_list[i+1]]
    #prints the maximum and minimum values  
    print("max vals are")
    print(max_vals)
    print("min vals are")
    print(min_vals)
