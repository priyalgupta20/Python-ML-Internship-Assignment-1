#to check suffix and prefix

str=input("Enter string...")
prefix=input("Enter prefix to check:")
suffix=input("Enter suffix to check:")

start=str.startswith(prefix)
end=str.endswith(suffix)

print("Prefix check:",start)
print("Suffix check:",end)