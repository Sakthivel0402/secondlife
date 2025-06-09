#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, os
import cgitb
from datetime import datetime

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()
ename = form.getvalue("name")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Registration</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
        .error {
            color: red;
        }

        .container {
            width: 40%;
            margin-top: 5%;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 20px;
        }

        body {
            background-image: url("./image/formbg.jpg");
            background-repeat: no-repeat;
            background-size: cover;
        }

        

        .navbar.transparent-navbar {
            background-color: transparent;
            border: none;
            box-shadow: none;
        }

        footer {
            background-color: #2d5b83;
            color: #fff;
            padding: 20px;
            text-align: center;
            margin-top: 10%;
        }

        h1 {
            color: #2d5b83;
        }

        .form-group label {
            font-weight: bold;
            color: #333;
        }

        .btn-primary {
            background-color: #2d5b83;
            border-color: #2d5b83;
        }

        .btn-danger {
            background-color: #d9534f;
            border-color: #d9534f;
        }

        footer a {
            color: #fff;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-default transparent-navbar">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="#" style="margin-left:530px;margin-top:-155px;">
                    <img alt="Company Logo" src="./image/logo.png" style="width: 400px;">
                </a>
            </div>
        </div>
    </nav>

    <div class="container">
        <center>
            <h1>Volunteer Registration</h1>
        </center>

        <form id="volunteerForm" method="post">

            <div class="form-group">
                <label for="NAME">Name</label>
                <input type="text" class="form-control" id="NAME" name="NAME" placeholder="Enter Full Name" required>
            </div>

            <div class="form-group">
                <label for="EMAIL">Email</label>
                <input type="email" class="form-control" id="EMAIL" name="EMAIL" placeholder="Enter Email" required>
            </div>

            <div class="form-group">
                <label for="CITY">City</label>
                <input type="text" class="form-control" id="CITY" name="CITY" placeholder="Enter City" required>
            </div>

            <div class="form-group">
                <label for="PHONE">Phone Number</label>
                <input type="tel" class="form-control" id="PHONE" name="PHONE" placeholder="Enter Phone Number" required>
            </div>

            <div class="form-group">
                <label for="AVAILABILITY">Availability</label>
                <select class="form-control" id="AVAILABILITY" name="AVAILABILITY" required>
                    <option value="alldays">All Days</option>
                    <option value="weekends">Weekends</option>
                </select>
            </div>

            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-4">
                    <input type="submit" class="btn btn-primary" value="Submit" name="SUB">
                </div>
                <div class="col-md-2"></div>
                <div class="col-md-4">
                    <a href="index.py" class="btn btn-danger">Cancel</a>
                </div>
            </div>
        </form>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</body>
<footer>
    &copy; 2023 Your Company | All Rights Reserved
</footer>

</html>""")

name = form.getvalue('NAME')
email = form.getvalue('EMAIL')
phone = form.getvalue('PHONE')
city = form.getvalue('CITY')
availability = form.getvalue('AVAILABILITY')
sub = form.getvalue('SUB')

if sub != None:
    b = f"""
        INSERT INTO volunteer (Name, Email, Phone, Availability, city) 
        VALUES ('{name}', '{email}', '{phone}', '{availability}', '{city}')
    """
    cur.execute(b)
    con.commit()
    if ename != None:
        b = f"""INSERT INTO awarepdetail (AName, Volunteer) VALUES ('{ename}', '{name}')"""
        cur.execute(b)
        con.commit()
        print("""
            <script>
            alert("Successfully registered for the program");
            </script>
        """)
    else:
        print("""
            <script>
            alert("Registered successfully");
            </script>
        """)
