import random 

def get_student_names(count):
  '''Gets student names from a file or prompt user to enter them manually.'''

  # List that contains student names
  students = []

  # Ask user if they have a file with student names
  prompt = f"Please enter filename to upload student names \nor press Enter to type them manually: "
  filename = input(prompt)

  # If there is a filename
  if filename != "":
    with open('student_names.txt') as file_object:
      for line in file_object:
        # Check for empty lines
        if line != "\n":
          students.append(line.lower()) 
  
  # Or get student names from user input
  else:
    while len(students) < student_count:
      prompt = "Enter student first and last name: "
      student = input(prompt).lower()
      students.append(student)
    
  return students

def generate_id():
  '''Generates random numbers from 111111 to 999999.'''
  return random.randrange(111111, 999999)

def not_zero_digit(id, count = 3):   
  ''' Determine the last 3 digits of a given number.
  Determine if digit == 0. '''

  while count > 0:
    last_digit = id % 10

    if last_digit == 0:
      return False

    id = id // 10
    count -= 1
  
  return True

def generate_list_of_ids(count):
  '''Generates the specified count of IDs.'''

  # List that stores student ID numbers
  ids = []
  while len(ids) < count:
    id = generate_id()
    if not not_zero_digit(id, count=3):
      continue
    if id not in ids:
      ids.append(id)
  return ids

def generate_emails(students, ids, domain):
  '''Generates student email addresses.

  Email adresses will be generated in a given format: 
  (first initial)+(last name)+(last 3 digits of student ID number)@example.org'''

  emails = []
  index = 0
  while index < student_count:
    # Determine first name initial and last name
    full_name = students[index].split(' ')
    
    # Account for first names with a space in them
    if len(full_name) > 2:
      first_name_initial = f'{full_name[0][0]}{full_name[1][0]}'
      last_name = full_name[-1]      
    else:
      first_name_initial = full_name[0][0]
      last_name = full_name[1]

    # Determine last 3 didgits od student ID number
    id = str(ids[index])
    student_id = id[-3:] 

    # Generate email
    email = f'{first_name_initial}{last_name}{student_id}@{domain}'
    emails.append(email)

    index += 1

  return emails

################# MAIN #################

print("This program generates student information.\n")

student_count = 5

students = get_student_names(count = student_count)

ids = generate_list_of_ids(count = student_count)

emails = generate_emails(students, ids, domain = 'example.org')

print(students)
print(ids)
print(emails)