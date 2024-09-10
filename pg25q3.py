#error in this code, it for some reason makes the inputed numbers rediculously long
h = input("please put in the amount of hours:")
m = input("please put in the amount of minuts:")
s = input("please put in the amount of seconds:")
print ("time is", h, m, s)
hts = (h*3600)
mts = (m*60)
so = s
s2 = int(mts+hts+so)
print ("totals time in second =", s2)
