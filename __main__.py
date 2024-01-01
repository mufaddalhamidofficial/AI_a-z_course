print("Hello World!")

# Print the current python environment
import sys

print(sys.executable)
print(sys.version)
print(sys.version_info)

print("\n\nTesting pytorch - ")
import torch

x = torch.rand(5, 3)
print(x)
