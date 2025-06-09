#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, os
import cgitb, string, random
from datetime import datetime
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-image: url('formbg.jpg');
            background-repeat: no-repeat;
            background-size: cover;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .container {
            width: 100%;
            max-width: 500px;
            
            padding: 30px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #2d5b83;
            font-weight: 600;
            margin-bottom: 25px;
        }

        input[type="text"], input[type="password"] {
            border-radius: 10px;
            padding: 12px;
            font-size: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .form-link {
            display: block;
            text-align: center;
            margin-top: 10px;
        }

        footer {
            background-color: #2d5b83;
            color: #fff;
            padding: 15px;
            text-align: center;
            position: absolute;
            bottom: 0;
            width: 100%;
        }

        .navbar {
            background-color: transparent;
            border: none;
            box-shadow: none;
        }

        .logo-container img {
            max-width: 300px;
            margin-top: -80px;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid logo-container">
            <img src="./image/logo.png" alt="Company Logo">
        </div>
    </nav>

    <div class="container">
        <h1 class="text-center">Admin Login</h1>
        <form method="post">

            <div class="form-group">
                <input type="text" class="form-control" name="ADMIN" required placeholder="Admin ID">
            </div>

            <div class="form-group">
                <input type="password" class="form-control" name="PASS" required placeholder="Password">
            </div>

            <div class="row">
                <div class="col-md-6">
                    <input type="submit" class="btn btn-primary w-100" value="Submit" name="SUB">
                </div>
                <div class="col-md-6">
                    <a href="index.py" class="btn btn-danger w-100">Cancel</a>
                </div>
            </div>
        </form>
    </div>

    <footer>
        &copy; 2023 Your Company | All Rights Reserved
    </footer>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
""")

id = form.getvalue("ADMIN")
password = form.getvalue("PASS")
submit = form.getvalue("SUB")

if submit is not None:
    if id == "Admin" and password == "1234":
        print("""
        <script>
        alert("Login success");
        location.href="adminindex.py";
        </script>
        """)
