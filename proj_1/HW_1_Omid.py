first_line = 'track type=wiggle_0 name=AO3.sr.30kb_bin.wig autoScale=on\n'
file_name = 'AO3.sr.30kb_bin.wig.txt'
input_file = open(file=file_name,mode= 'rt') # open file
threshhold = 5 #define threshhold

max_overal=0 #set the max_overall amplification
max_scaf=0 #set the max ratio for the scaffold only

while True:
    line= input_file.readline() 
    if line == first_line: # checks the first line
        print('This is just the beginning!')
    elif line =='':
        print('This is the file end')
        break
    elif line[0:9]=='fixedStep':
    #New scaffold has been found so, let's print the previous one.
        if max_scaf > threshhold:
            print (latest_scaf_name)
            print (max_scaf)
        latest_scaf_name = line[:-2]
        max_scaf = 0
    else:
        latest_num= float(line)
        if latest_num > max_scaf:
            max_scaf = latest_num
        if latest_num >= max_overal:
            max_overall_scaf_name = latest_scaf_name
            max_overal=latest_num

print('The scaffold with the most amplification is:')
print(max_overall_scaf_name)
print(max_overal)