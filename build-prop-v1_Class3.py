with open("build.prop", "r") as file:       #open the file and assign it to variable 'file'
    out = open(input("enter file name to save as: "), "a")           #Declare output file name
    for line in file:                       #go line by line through the file
        splits = line.split('=')             #Everything after '=' starts at position 1
        if 'ro.product.vendor.manufacturer=' in line:
            print(f'Android manufacturer is {splits[1].rstrip()}', file=out) #rstrip removes trailing newline
        elif 'ro.product.vendor.model=' in line:
            print(f'Android model is {splits[1].rstrip()}', file=out)
        elif 'ro.product.first_api_level' in line:
            print(f'API Level: {splits[1].rstrip()}', file=out)
        elif 'ro.vendor.build.security_patch' in line:
            print(f'Build security patch: {splits[1].rstrip()}', file=out)
