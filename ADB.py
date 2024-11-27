import subprocess

# List connected devices
devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
print(devices.stdout)

# Run a shell command on the device
result = subprocess.run(["adb", "shell", "ls", "/sdcard"], capture_output=True, text=True)
print(result.stdout)
