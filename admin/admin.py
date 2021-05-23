import hashlib

  # add salt and hash in a password 
salt = "$PNP"

def encrypt_password(password, salt):
  salted = str(password) + str(salt)
  #print(salted)
  hash = hashlib.sha256(salted.encode('utf-8')).hexdigest()
  return hash

#encrypt_account
def encrypt_account(username, password):
  #print("[+] encrypting password ...")
  hash = encrypt_password(password, salt)
  #print("[+] password encrypted!")
  return username + ":" + hash

def create_db(account):
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  new_account = encrypt_account(username, password)
  f = open("admin/admin_db.txt","a+")
  f.write(new_account + "\n")
  print("[+] written account details into database!")

def get_username(account):
  # check for before the colon ":"
  result = account.split(':')[0]
  print(type(result))
  return result
  
def get_password(account):
  # check for after the colon ":"
  result = account.split(':')[1]
  print(type(result))
  return result

def eval_login(account):
  # loopy process that loops through line by line -> admin_db.txt
  admin_db = open("admin/admin_db.txt", "r")
  lines = admin_db.readlines()
  count = 0
  #this_line
  for line in lines:
    count += 1
    current_line = line.strip()
    if current_line == account:
      print("[+] Login Successful!")
      return 1
    else:
      print("[-] Invalid Login!")
      return 0

def login():
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  login_account = encrypt_account(username, password)
  #print(login_account)
  eval_login(login_account)
  






