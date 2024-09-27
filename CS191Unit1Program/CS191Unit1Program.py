
# Conditional Operation
# This function returns the truth value for p -> q
# The conditional operation is false if only if the hypothesis is true 
# and the conclusion is false
def implies(p, q):
    if (p and not q): 
        return False
    return True  
        
# Table 1
# Prints out the rows of a truth table for "not(p -> q)" and "p or not(q)"
# A message is printed for every truth assignment that makes the two propositions have different truth values.
print("Table 1")
print("p\t\tq\t\tnot(p -> q)\t\t(p or not(q))")  # column header
for p in (True, False):
    for q in (True, False):
        one = not(implies(p, q))
        two = p or not(q)
        print( p, "\t",q, "\t\t", one, "\t\t",two, end = '' ) 
        if (one != two ):
            print("  <-- Different truth values. Not logically equivalent.", end = '') 
        print(" ")
print(" ")

# Table 2
# Prints out the rows of a truth table for "not(p -> q)" and "p and not(q)"
# A message is printed for every truth assignment that makes the two propositions have different truth values.
print("Table 2")
print("p\t\tq\t\tnot(p -> q)\t\t(p and not(q))")  # column header
for p in (True, False):
    for q in (True, False):
        one = not(implies(p, q))
        two = p and not(q)
        print( p, "\t",q, "\t\t", one, "\t\t",two, end = '' ) 
        if (one != two ):
            print("  <-- Different truth values. Not logically equivalent.", end = '') 
        print(" ")
print(" ")


# Table 3
# Add code to show that  "p -> q" and "not p or q" are equivalent
# A message is printed for every truth assignment that makes the two propositions have different truth values.
print("Table 3")
print("p\t\tq\t\t(p -> q)\t (not p or q)")  #column header
for p in (True, False):
    for q in (True, False):
        one = implies(p, q)
        two = not(p or q)
        print( p, "\t",q, "\t\t", one, "\t\t",two, end = '' ) 
        if (one != two ):
            print("  <-- Different truth values. Not logically equivalent.", end = '') 
        print(" ")
print(" ")


# Table 4
# Add code to print out the rows of a truth table for "(p or q) -> r" and "(p -> r) and (q -> r)"
# A message should be printed for every truth assignment that makes the two propositions have different truth values.
print("Table 4")
print("p\t\tq\t\tr\t\t((p or q) -> r)\t\t((p -> r) and (q -> r))")  # column header
for p in (True, False):
    for q in (True, False):
        for r in (True, False):
            one = implies((p or q), r)
            two = implies(p, r) and implies(q, r)
            print( p, "\t",q, "\t\t", one, "\t\t",two, end = '' ) 
            if (one != two ):
                print("  <-- Different truth values. Not logically equivalent.", end = '') 
            print(" ")
        print(" ")
print(" ") 

# Table 5
# Put your code here to print out the rows of a truth table for "(p and q) -> r" and "(p -> r) and (q -> r)"
# A message should be  printed for every truth assignment that makes the two propositions have different truth values.
print("Table 5")
print("p\t\tq\t\tr\t\t((p and q) -> r)\t\t((p -> r) and (q -> r))")  # column header
for p in (True, False):
    for q in (True, False):
        for r in (True, False):
            one = implies((p and q), r)
            two = implies(p, r) and implies(q, r)
            print( p, "\t",q, "\t\t", one, "\t\t",two, end = '' ) 
            if (one != two ):
                print("  <-- Different truth values. Not logically equivalent.", end = '') 
            print(" ")
        print(" ")
print(" ") 


