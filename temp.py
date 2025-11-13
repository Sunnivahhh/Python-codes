def farenheit():
    f=int(input("Enter farenheit"))
    convertf=(f-30)/2
    convertkf=(f-32)*5/9+ 273.15
    print (f'{f} degrees farenheit is : {convertf} degrees celcius and {convertkf} degrees farenheit')
      
def celcius():
    c=int(input("Enter celcius"))
    convertc=(c*2)+30
    convertkc = c+273.15
    print (f'{c} degrees celcius is {convertc} degrees farenheit and {convertkc} degrees kelvin')


def kelvin():
    k=int(input("Enter kelvin"))
    kintoc = k-273.15
    kintof=(k-273.15)* 9/5 + 32
    print (f'{k} degrees kelvin is {kintof} degrees farenheit and {kintoc} degrees celcius')


while True:
    a=input("Enter what temperature you need to convert(farenheit/celcius/kelvin)")
    if a=="farenheit":
        farenheit()
    

    elif a=="celcius":
        celcius()


    elif a=="kelvin":
        kelvin()


    else:
        print ("Error! Please try again")
    
    decision = input("Would you like to continue? (y/n): ").lower()
    if decision == "n":
        print("Thank you for using the converter!")
        break
    elif decision == "y":
        continue
    else:
        print("Error! Please enter 'y' or 'n' ")


    

    


