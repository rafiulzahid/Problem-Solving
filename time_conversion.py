# Read input
N = int(input("Enter the duration in seconds: "))

hours = N // 3600
N %= 3600
minutes = N // 60
seconds = N % 60

print(f"{hours}:{minutes}:{seconds}")
