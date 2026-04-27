user = {'name': 'Alice', 'age': 25, 'city': 'New York'}
age = user.pop('age')
print(f"Removed age: {age}")   
print(f"Updated user: {user}") 
job = user.pop('job', 'Not Found')
print(f"Job: {job}")          
