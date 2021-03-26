# Bitwise OR (4 | 11)
a = 4
b = 11
c = a | b

print('a. ','Nilai :',a, ', binary :', format(a,'08b'))
print('   ','Nilai :',b, ', binary :', format(b,'08b'))
print('   ------------------------------- (|)')
print('    Nilai dari 4 | 11 =',c, '\n    Binary dari 4 | 11 =', format(c,'08b'))


# Shift right (4 >> 11)
c = a >> b

print('\nb. ','Nilai :',a, ', binary :', format(a,'08b'))
print('   ------------------------------- (>>)')
print('   ','Nilai :',b, ', binary :', format(b,'08b'))
print('    Nilai dari 4 >> 11 =',c, '\n    Binary dari 4 >> 11 =', format(c,'08b'))


# Bitwise XOR (4 ^ 11)
c = a ^ b

print('\nc. ','Nilai :',a, ', binary :', format(a,'08b'))
print('   ','Nilai :',b, ', binary :', format(b,'08b'))
print('   ------------------------------- (^)')
print('    Nilai dari 4 ^ 11 =',c, '\n    Binary dari 4 ^ 11 =', format(c,'08b'))


# Bitwise NOT (~4)
c = ~a

print('\nd. ','Nilai :',a, ', binary :', format(a,'08b'))
print('   ------------------------------- (~)')
print('    Nilai dari ~4 =',c, '\n    Binary dari ~4 =', format(c,'08b'))


# Bitwise AND (11 & 4)
c = b & a

print('\ne. ','Nilai :',b, ', binary :', format(b,'08b'))
print('   ','Nilai :',a, ', binary :', format(a,'08b'))
print('   ------------------------------- (&)')
print('    Nilai dari 11 & 4 =',c, '\n    Binary dari 11 & 4 =', format(c,'08b'))