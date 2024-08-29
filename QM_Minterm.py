
# Finding the number of changes in the bits and their positions
def grouping(a, b):
    change = 0
    position = []
    for i in range(6):
        if a[i] != b[i]:
            change += 1
            position.append(i)
    return change, position


# Updating the binary list according to the positions
def grouping1(a, b, change, position):
    if change == 1:
        c = list(a)
        c[position[0]] = '_'
        c = "".join(c)
        paired_terms.extend([str(dictionary[a]), str(dictionary[b])])
        if c not in group2[s]:
            group2[s].append(c)
            min_terms_pair1[s].append(str(dictionary[a]) + "-" + str(dictionary[b]))


# Finding the EPI and PI terms
def find_epi(min_list):
    terms = []
    epi = []
    min_terms_str = [str(i) for i in min_terms]
    for w in min_list:
        w1 = w.split('-')
        for p in range(0, len(w1)):
            terms.append(w1[p])
    for e in min_terms_str:
        if terms.count(e) == 1:
            for f in min_list:
                if e in f.split('-') and f not in epi:
                    epi.append(f)
    pi = []
    for u in min_list:
        if u not in epi:
            pi.append(u)
    return epi, pi


# Decimal to binary conversion
def decimal_to_binary(number):
    binary_convert = []
    while (number // 2) >= 1:
        rem = number % 2
        binary_convert.append(str(rem))
        number = number // 2
    binary_convert.append(str(number))
    while len(binary_convert) < 6:
        binary_convert.append(str(0))
    new_list = binary_convert[::-1]
    dec_to_bin = "".join(new_list)
    return dec_to_bin


# Getting the final terms from the EPI and PI terms
def final_terms(epi, pi):
    final_terms1 = []
    min_terms_str = [str(i) for i in min_terms]
    for e in min_terms_str:
        t = 0
        for f in epi:
            if e in f.split('-'):
                t += 1
        if t == 0:
            term1 = []
            for m in pi:
                if e in m:
                    term1.append(m)
            j = 0
            for c in range(len(term1)):
                if c == 0:
                    j = term1[c]
                if len(term1[c]) > len(j):
                    j = term1[c]
            final_terms1.append(j)
    final_terms1.extend(epi)
    return final_terms1


# Converting the final terms into final expression
def expression(final):
    final1_group = []
    termz = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
    exp = ""
    for b in range(len(list_min_terms)):
        if list_min_terms[b] in final:
            final1_group.append(list_group[b])
    for o in final1_group:
        for g in range(len(o)):
            if o[g] == '0':
                exp = exp + termz[g] + "'"
            if o[g] == '1':
                exp = exp + termz[g]
        if o != final1_group[-1]:
            exp = exp + ' + '
    return exp


# To check if the dictionary is empty
def check(a):
    for i in a:
        if len(i) == 0:
            continue
        else:
            return True
    return False


# Finding the unpaired min terms
def unpaired_min_terms1(paired_terms):
    elements = []
    elements1 = []
    for h in range(len(min_terms_pair.values())):
        for g in range(len(min_terms_pair[h])):
            elements.append(min_terms_pair[h][g])
            elements1.append(group1[h][g])
    for v in range(len(elements)):
        if elements[v] not in paired_terms:
            unpaired_group.append(elements1[v])
            unpaired_min_terms.append(elements[v])


# Getting the ASCII values for the min terms
min_terms = [int(i) for i in (input("Enter the min_terms:").split(','))]

# Converting the min terms to binary
binary_conversion = {decimal_to_binary(i): str(i) for i in range(64)}
no_of_bits = len(str(bin(2 ** 6 - 1))[2:])
binary_numbers = []

for i in min_terms:
    binary = str(bin(int(i)))[2:]
    if len(binary) != no_of_bits:
        n = no_of_bits - len(binary)
        binary = "0" * n + binary
    binary_numbers.append(binary)

# Grouping the min terms
group1 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

min_terms_pair = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for k in binary_numbers:
    count = k.count('1')
    group1[count].append(k)
    min_terms_pair[count].append(binary_conversion[k])

print("\nStep 1:")
print("Group:", group1)
print("Min terms:", min_terms_pair)

z = 2
unpaired_group = []
unpaired_min_terms = []
while check(group1.values()):
    dict_key = []
    for i in group1:
        dict_key.extend(group1[i])
    dict_val = []
    for i in min_terms_pair:
        dict_val.extend(min_terms_pair[i])
    dictionary = dict(zip(dict_key, dict_val))

    group2 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}  # Initialize group2 with the same structure as group1
    min_terms_pair1 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    paired_terms = []
    for s in range(5):
        for l in group1[s]:
            for m in group1[s + 1]:
                ch, pos = grouping(l, m)
                grouping1(l, m, ch, pos)

    # Check if new groups were formed, if not, break the loop
    if not check(group2.values()):
        break

    # Updating group1 and min_terms_pair based on group2 and min_terms_pair1
    unpaired_min_terms1(paired_terms)
    group1 = dict(group2)
    min_terms_pair = dict(min_terms_pair1)
    print("\nStep" + str(z) + ":")
    print("Group:", group1)
    print("Min_terms:", min_terms_pair)
    z += 1

for b in range(len(unpaired_group)):
    for x in range(len(group1.keys())):
        if len(group1[x]) == 0:
            group1[x].append(unpaired_group[b])
            min_terms_pair[x].append(unpaired_min_terms[b])
            break
    else:
        group1[len(group1.keys())] = [(unpaired_group[b])]
        min_terms_pair[len(min_terms_pair.keys())] = [(unpaired_min_terms[b])]
print("\nFinal Group:", group1)
print("Final Min terms:", min_terms_pair)

list_min_terms = []
list_group = []
for q in min_terms_pair:
    if len(min_terms_pair[q]) != 0:
        list_min_terms.extend(min_terms_pair[q])
        list_group.extend(group1[q])
epi_terms, pi_terms = find_epi(list_min_terms)
print("\nEPI Terms:", epi_terms)
print("PI Terms:", pi_terms)
final = final_terms(epi_terms, pi_terms)
final_expression = expression(final)
print("\nThe minimized final expression is:", final_expression)