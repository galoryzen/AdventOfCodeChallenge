#Counting the appearences of a letter and comparing if it matches between the limits
def getValidPasswords1(file):
    password_counter = 0
    for line in file:
        helper = line.split(":")
        limits = helper[0].split("-")

        inferior_limit = int(limits[0])
        superior_limit = int(limits[1][:len(limits[1])-2])

        letter = helper[0][len(helper[0])-1]
        count = helper[1].count(letter)

        if(count>=inferior_limit and count<=superior_limit):
            password_counter += 1
    return password_counter

#Verifying if a letter appears and does not repeat in the positions specified
def getValidPasswords2(file):
    password_counter = 0
    for line in file:
        helper = line.split(":")
        letter = helper[0][len(helper[0])-1]
        limits = helper[0].split("-")
        pos_1 = int(limits[0])
        pos_2 = int(limits[1][:len(limits[1])-2])
        lp1 = letter == helper[1][pos_1]
        lp2 = letter == helper[1][pos_2]

        if((lp1 or lp2) and not (lp1 and lp2)):
            password_counter += 1
    return password_counter

def main():
    fh = open("input.txt")
    print(getValidPasswords1(fh))
    #print(getValidPasswords2(fh))

main()
