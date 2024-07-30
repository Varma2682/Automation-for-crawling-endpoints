import subprocess

def execute_command(command):
    try:
        # Run the command using subprocess
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"Output of '{command}':\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing '{command}':\n{e.stderr}")

if __name__ == "__main__":
    # Ask for the domain name and subdomain path at runtime
    domain = input("Enter the domain name: ")
    subdomain_path = input("Enter the subdomain file path: ")

    # List of commands to execute
    commands = [
        f"httpx-toolkit -l {subdomain_path} -o httpxlinks.txt",
        f"echo \"{domain}\" | gau --threads 5 >> End Points.txt",
        "cat httpxlinks.txt | katana -jc >> End Points.txt",
        "httpx-toolkit -l End points.txt -mc 200 -o endpoints200.txt"
        "httpx-toolkit -l End points.txt -mc 403 -o endpoints403.txt"
        "cat endpoints200.txt | urldedupe >> Endpointsfinal200.txt"
        "cat endpoints403.txt | urldedupe >> Endpointsfinal403.txt"
    ]
    
    for cmd in commands:
        execute_command(cmd)
