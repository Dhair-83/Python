set={3,5,2,6,1,2,4,9,9,2,3,4,8}
print(set)

s1={0,1,3,5,6,7,11,13,14}
s2={2,3,4,5,8,11,12}

print("\n s1:",s1)
print("\n s2:",s2)

print("\n", s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))