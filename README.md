# Send Bulk Email in python

## Steps to run:

### 1. To create virtual environment
`virtaulenv .ev`

### 2.  Activate .env
`source .env/bin/activate`

### 3.  Fill details of receives in excel.csv

### 4. Changes in code.py
  1. change path of cvs file to your local csv path(in line 12)
  
  ` csv_filepathname = <<Your Path>> `
  
  2. change sender's email, sender's name and password (in line 26, 27, 28)
  
  3. if you need to attach more file then copy paste code of line 16 to 23 and line 64 and change filename 
  
  4. Change html of line 55 to your message HTML and msg['Subject'] of line 52 to your message subject.
   
  TIP: enable Less secure app access of that google account(sender's email)
    
    manage your Google Account -> security -> Less secure app access -> enable

### 5. Run Code
  1. `python`
  2. `from code import email`
  3. `email()`
