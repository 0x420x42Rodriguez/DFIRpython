"""
This script takes a list of in-addr-arpa addresses as input, strips the "in-addr-arpa",
and then reverses the IP addresses, before saving them to a txt file.

Change the input and output file paths to match your needs.
"""

with open(r"C:\Users\useraccount\Desktop\reverseIP.txt", "r") as file: #Change the file path to the list to convert

    x = file.readlines()  #Read each line in the file
    split_lines = []  
    new_ip = []
    joined_ip = []
    j = "."
    
    for i in range(len(x)):
        split_lines.append(x[i].split(".")) #Split by the "."
        new_ip.append(split_lines[i][:4][::-1]) #Slice out the text and then reverse the order
        joined_ip.append(j.join(new_ip[i])) #Join the items into a string

    file.close()

    with open(r"C:\Users\useraccount\Desktop\correctIP.txt", "w") as outfile:  #Change the file path to where you want to save the output
        for item in joined_ip:
            outfile.write(item + "\n")
        
    
        

    


    

    
