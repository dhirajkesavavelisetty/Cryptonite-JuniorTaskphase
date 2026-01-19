import sys

p = 9129026491768303016811207218323770273047638648509577266210613478726929333106121387323539916009107476349319902011390210650434835260358014251332047605739279

def compute_list(values):
    return [pow(v, (p-1)//2, p) for v in values] # returns 1 for  quadratic residue, p-1 for quadratic non-residue

def binary_from_output(computeted_input, flag):
    # consider and print both the posibilities
    binary = []
    for e in computeted_input:
        if e == 1:
            binary.append('0' if flag else '1')  # If flag is True: e=1 then 0 or if e=p-1 then 1 and If flag is False: e=1 then 1, e=p then 0
        elif e == p-1:
            binary.append('1' if flag else '0')
    return ''.join(binary)

#MAIN 
path = 'out.txt'
with open(path, 'r') as f:
    s = f.read().strip()
input = eval(s) 

output_computation = compute_list(input)

binary_A = binary_from_output(output_computation, flag=True)
binary_B = binary_from_output(output_computation, flag=False)

print("Binary: ")
print(binary_A)
print(binary_B)