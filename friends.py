employees = [{
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
},
{
    "name": "Kennan Salisbury",
    "age": 30,
    "department": "Software Engineer",
    "phone": "786-4259",
    "salary": "$1,000,000"
},
{
    "name": "Millie Salisbury",
    "age": 1,
    "department": "Number One Doge",
    "phone": "111-1111",
    "salary": "$5,000"
}]

for employee in employees:
    print(f'{employee["name"]} in {employee["department"]} can be reached at {employee["phone"]}')
        