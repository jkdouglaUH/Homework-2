def isapalindrome(inputname):
  inputname = inputname.replace("","").lower()
  return inputname == inputname[::-1]
def main():
  inputname = input("")
  if isapalindrome(inputname):
    print(f"{inputname} is a palindrome")
  else:
    print(f"{inputname} is not a palindrome")
if __name__ == "__main__":
  main()