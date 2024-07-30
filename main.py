from datetime import datetime
import importlib.metadata

now = datetime.now()
version = importlib.metadata.version("virtualenv")


print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("VirtualEnv version:", version)
