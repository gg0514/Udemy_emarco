"""
Docstring for formatting
if __name__ == "__main__":

# Old style string formatting    
    print("%d x %d = %d" % (2,3,6))      # '2 x 3 = 6'
    print("[%d] x [%d] = [%d]" % (2,3,6))  # '[2] x [3] = [6]'
    print("[% -10d] x [%d] = [%d]" % (2,3,6))  # '[2         ] x [3] = [6]'

# New style string formatting   
    print("{0} x {1} = {2}".format(2,3,6))  # '2 x 3 = 6'
    print("{a} x {b} = {c}".format(a=2, b=3, c=6))  # '2 x 3 = 6'

"""

print("%d x %d = %d" % (2,3,6))      # '2 x 3 = 6'
print("[%d] x [%d] = [%d]" % (2,3,6))  # '[2] x [3] = [6]'
print("[% -10d] x [%d] = [%d]" % (2,3,6))  # '[2         ] x [3] = [6]'

