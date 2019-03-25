#5
def encoder(string):
    count = 0
    encode = []
    letter = string[0]
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
        else:
            encode += [[letter, count]]
            count = 1
            letter = string[i]
    encode.extend([[letter,count]])
    return encode

def decoder(ls):
    decode = ""
    for i in range(len(ls)):
        decode += str(ls[i][0] * ls[i][1])
    return decode

def main():
    string = "aadcccca"
    ls = [["a", 2], ["d",1], ["c", 4], ["a", 2]]
    print("Encoded string: ", encoder(string))
    print("Decoded list: ", decoder(ls))
    
main()
