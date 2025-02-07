# Read from the file file.txt and output all valid phone numbers to stdout.

awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

# Link to the problem: https://leetcode.com/problems/valid-phone-numbers/
