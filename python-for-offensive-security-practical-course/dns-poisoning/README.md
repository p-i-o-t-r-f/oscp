

Win Target: DNS_Poisoning.py

Append the host file C:\Windows\System32\drivers\etc with new entries : google , then flush dns cache

To create exe file, please change setup.py file and past like below:

sys.argv.append("py2exe")
setup(
    options = {'py2exe': {'bundle_files': 1}},
 
    windows = [{'script': "DNS_Poisoning.py", 'uac_info':"requireAdministrator"}],    
    zipfile = None,
    
)
