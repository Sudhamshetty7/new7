import sys
print(sys.argv)
module=sys.argv[1]
print(f"The file name is {sys.argv[0]}")
print(f"The module is {module}")
print(f"The second arguement is  {sys.argv[2]}")        
print(sys.path)
sys.exit(0)
sys.exit(f"Execution stopped")
