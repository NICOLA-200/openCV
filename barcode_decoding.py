import subprocess

result = subprocess.run(['zbarimg', 'bar.png'], capture_output=True, text=True)
print(result.stdout)
