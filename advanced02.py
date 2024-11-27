def main():
    earthling_wieght = float(input("enter your wieght earthling _ "))
    mars_wieght : float = 37.8/100 * earthling_wieght
    mars_wieght = round(mars_wieght,2)
    print("your wieght on mars is _ ", mars_wieght )
    planet_name : str = input ("enter your planet name with first letter capital")
   
    if  "Mercury" in planet_name :
        converted_wieght = 37.6/100 * earthling_wieght
        converted_wieght = round (converted_wieght , 2)
        print("your wieght on mercury is _ " , converted_wieght)
    
    elif "Venus" in planet_name :
        converted_wieght : float = 88.9/100 * earthling_wieght
        converted_wieght = round (converted_wieght , 2)
        print("your_wieght on venus is _ " , converted_wieght) 

    elif "Mars" in planet_name :
       converted_wieght : float= 37.8/100 * earthling_wieght
       converted_wieght = round (converted_wieght , 2)
       print("your wieght on mars is _ " , converted_wieght)

    elif "Jupiter" in planet_name :
       converted_wieght : float= 236.0/100 * earthling_wieght
       converted_wieght = round (converted_wieght , 2)
       print("your wieght on jupiter is _ " , converted_wieght)

    elif "Saturn" in planet_name :
       converted_wieght: float = 108.1/100 * earthling_wieght
       converted_wieght = round (converted_wieght , 2)
       print("your wieght on Saturn is _ " , converted_wieght)

    elif "Uranus" in planet_name :
       converted_wieght : float= 81.5/100 * earthling_wieght
       converted_wieght = round (converted_wieght , 2)
       print("your wieght on Uranus is _ " , converted_wieght)

    elif "Neptune" in planet_name :
       converted_wieght : float = 114.0/100 * earthling_wieght
       converted_wieght = round (converted_wieght , 2)
       print("your wieght on Neputune is _ " , converted_wieght)

    else :
       print("Sorry! Enter a planet name with the firdt letter capital_ ") 
if __name__ == "__main__":
    main()