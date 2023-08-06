import subprocess
import os


def menu():
	optionsList = ["Discovery", "Full", "UDP", "Exit"]

	for counter, i in enumerate(optionsList,1):
		print(str(counter) + ".", i)

	print('')
	scan = input("Select the type of scan you want: ")
	return scan

	



scan = menu()

while scan != '4':
	if scan == '1':
		os.mkdir("nmap")
		os.chdir("nmap")
		result = subprocess.run(["nmap", "-Pn", "-n", "-sS", "-p", "21-23,25,53,111,137,139,445,80,443,8443,8080", "--min-hostgroup", "255", "--min-rtt-timeout", "0ms", "--max-rtt-timeout", "100ms", "--max-retries", "1", "--max-scan-delay", "0", "--min-rate", "620", "-oA", "DISCOVERY", "-vvv", "--open", "-iL", "../hosts"])
		#print(result.communicate()[1])
		subprocess.run(["ultimate-nmap-parser.sh", "*.gnmap", "--up"])
		scan = menu()

	elif scan == '2':
		subprocess.run(["nmap", "-Pn", "-n", "-sS", "-p-", "--min-hostgroup", "255", "--min-rtt-timeout", "0ms", "--max-rtt-timeout", "100ms", "--max-retries", "1", "--max-scan-delay", "0", "--min-rate", "620", "-oA", "01-FULL", "-vvv", "--open", "-iL", "hosts_up.txt"])
		subprocess.run(["ultimate-nmap-parser.sh", "*.gnmap", "--all"])
		scan = menu()

	#elif scan == 3:

	else:
		print("you didn't select a valid option")
		scan = menu()
print("Exiting...")