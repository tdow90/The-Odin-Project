words = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]


def substring(substring, list):
    substringDictionary = {} # Makes empty dict
    for i in list:
        if i in substring:
            if i in substringDictionary:
                substringDictionary[i] += 1
            else:
                substringDictionary[i] = 1
    print(substringDictionary)



                
            


substring("Howdy partner, sit down! How's it going?", words)