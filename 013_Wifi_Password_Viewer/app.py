import subprocess

def get_wifi_profiles():
    result = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
    profiles = []
    for line in result.split("\n"):
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            profiles.append(profile)
    return profiles

def get_wifi_password(profile):
    try:
        result = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode()
        for line in result.split("\n"):
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return "(no password found)"
    except:
        return "(error retrieving password)"
    
def main():
    print("Wi-Fi SSID & Password Viewer\n")
    profiles = get_wifi_profiles()
    for profile in profiles:
        password = get_wifi_password(profile)
        print(f"SSID: {profile}\nPassword: {password}\n{'-'*30}")

if __name__ == "__main__":
    main()