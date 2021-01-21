# http://www.pythonchallenge.com/pc/def/274877906944.html

# Shift each character of the input twice to the right
# K -> M, O -> Q, E -> G
input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet        = "abcdefghijklmnopqrstuvwxyz"
shiftedAlphabet = "cdefghijklmnopqrstuvwxyzab"

url = "map"

# Make a translation mapping using the given alphabet and its shifted counterpart
trans = str.maketrans(alphabet, shiftedAlphabet) 

# Print the input translated using the given mapping
print(input.translate(trans))

print(url.translate(trans))