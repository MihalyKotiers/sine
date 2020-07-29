from sys import argv

script, angle_rad = argv

x = float(angle_rad)

# 'fancy' ascii art
print ".,-~:;=!#$@$#!=;:~-,.....................,-~:;=!#$@$#!=;:~-,....................."
print "=!#$@$#!=;:;=!#$@$#!=;:~-,.........,-~:;=!#$@$#!=;:;=!#$@$#!=;:~-,.........,-~:;="
print "@$#!=;:~-,.,-~:;=!#$@$#!=;:~-,.,-~:;=!#$@$#!=;:~-,.,-~:;=!#$@$#!=;:~-,.,-~:;=!#$@"
print "=;:~-,.........,-~:;=!#$@$#!=;:;=!#$@$#!=;:~-,.........,-~:;=!#$@$#!=;:;=!#$@$#!="
print ".....................,-~:;=!#$@$#!=;:~-,.....................,-~:;=!#$@$#!=;:~-,."

# calculating a to the power of n using while loop
def p(a,n):
    if n == 0:
        return 1
    else:
        i = n - 1
        temp = a
        while i > 0:
            temp = temp*a
            i -= 1
        return temp

# an inefficient way to calculate factorials
def f(n):
    temp = n
    if temp == 1:
        return 1
    else:
        return temp*f(n-1)
    

print '\n>We will calculate the sine of %s with the help of power series' % (angle_rad)
print " \n sin(x) ~ x - (x^3)/3! + (x^5)/5! - (x^7)/7! \n"
print ">The result: %f \n" % (x - p(x,3)/f(3) + p(x,5)/f(5) - p(x,7)/f(7))