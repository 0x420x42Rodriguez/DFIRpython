report = []                                 #Create an empty list to write the output to
with open("build.prop", "r") as file:       #open the file and assign it to variable 'file'
    for line in file:                       #go line by line through the file
        splits = line.split('=')             #Everything after '=' starts at position 1
        if 'ro.product.vendor.manufacturer=' in line:
            print(f'Android manufacturer is {splits[1].rstrip()}') #rstrip removes trailing newline
            report.append(f'Android manufacturer: {splits[1]}')
        elif 'ro.product.vendor.model=' in line:
            print(f'Android model is {splits[1].rstrip()}')
            report.append(f'Android model: {splits[1]}')
        elif 'ro.product.first_api_level' in line:
            print(f'API Level: {splits[1].rstrip()}')
            report.append(f'API Level: {splits[1]}')
        elif 'ro.vendor.build.security_patch' in line:
            print(f'Build security patch: {splits[1].rstrip()}')
            report.append(f'Build security patch: {splits[1]}')

    print(report)

with open(input("Enter File Name: "), "w") as file:     #This can be turned into a function
    for value in report:
        file.write(value)
