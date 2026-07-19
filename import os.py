import os
print("Current Directory:", os.getcwd())
fp = open("sample.txt", 'w') #relative path
fp.write("We are learning Python")
fp.close()

print("Files in current directory:", os.listdir())
print("Does sample.txt exist?", os.path.isfile("sample.txt"))

fp = open(r"sample2.txt", 'w')#absolute path
fp.write("""Working with absolute path \n ckjblbkjb;""")
fp.close()

fp = open("sample2.txt", 'r')
print("Full content:")
print(fp.read())
fp.close()

fp = open("sample2.txt", 'r')
print("First line:")
print(fp.readline())

print("All lines:")
print(fp.readlines())
fp.close()