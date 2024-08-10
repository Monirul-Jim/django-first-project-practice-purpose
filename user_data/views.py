from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    students = [
        {'name': 'Rahim', 'roll': '34', 'class': '10', 'father_name': 'Karim',
            'mother_name': 'Ayesha', 'address': '123 Main St'},
        {'name': 'Jhon Cena', 'roll': '42', 'class': '8', 'father_name': 'Unknown',
            'mother_name': 'Unknown', 'address': '456 Elm St'},
        {'name': 'Rollins', 'roll': '20', 'class': '9', 'father_name': 'Smith',
            'mother_name': 'Emma', 'address': '789 Maple St'},
        {'name': 'Alice', 'roll': '55', 'class': '10', 'father_name': 'John',
            'mother_name': 'Mary', 'address': '111 Birch St'},
        {'name': 'Bob', 'roll': '12', 'class': '7', 'father_name': 'Robert',
            'mother_name': 'Sara', 'address': '222 Pine St'},
        {'name': 'Charlie', 'roll': '17', 'class': '8', 'father_name': 'James',
            'mother_name': 'Laura', 'address': '333 Oak St'},
        {'name': 'David', 'roll': '29', 'class': '9', 'father_name': 'Daniel',
            'mother_name': 'Sophia', 'address': '444 Cedar St'},
        {'name': 'Eva', 'roll': '38', 'class': '7', 'father_name': 'Michael',
            'mother_name': 'Grace', 'address': '555 Spruce St'},
        {'name': 'Frank', 'roll': '44', 'class': '10', 'father_name': 'George',
            'mother_name': 'Helen', 'address': '666 Willow St'},
        {'name': 'Grace', 'roll': '50', 'class': '9', 'father_name': 'Henry',
            'mother_name': 'Lily', 'address': '777 Ash St'},
    ]
    return render(request, 'home.html', {'students': students})
