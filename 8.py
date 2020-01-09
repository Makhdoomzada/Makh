def convert_to_kelvin(temperature, units):
    if temperature==int:
        if units == C:
            return(temperature + 273)
        elif units == F: 
            return(((temperature - 32)/1.8)+273)
        elif units== K:
            return(temperature)
        else:
            return(None)
    else:
        return(None)
def is_gas(temperature):
    if temperature==int:
        if temperature > 373:
            return(True)
        else:
            return(False)
    else:
        return(None) 
def is_solid(temperature):
    if temperature==int:
        if temperature < 273:
            return(True)
        else:
            return(False)
    else:
        return(None)
if __name__=="__main__":
  units=input("input units in K, C, or F")
  temperature=input("Input temperature")
  if temperature.isnumeric:
     temperature = convert_to_kelvin(temperature, units)
     if is_gas(temperature):
         print("Is gas")
     elif is_solid(temperature):
         print("Solid")
  else:
      print("invalid input") 
input("input string")



def print_greeting(name):
    return print("good morning " + name)
 





