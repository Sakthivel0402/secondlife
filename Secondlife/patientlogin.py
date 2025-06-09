#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, os
import cgitb, string, random

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
    <title>Rehabilitation Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
        body {
            background-image: url('./image/formbg.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            
            width: 100%;
            max-width: 400px;
        }

        h1 {
            color: #2d5b83;
            font-weight: 600;
            margin-bottom: 25px;
        }

        input[type="text"],
        input[type="password"] {
            border-radius: 10px !important;
            padding: 12px;
            font-size: 15px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        input[type="submit"],
        .btn-danger {
            width: 100%;
            padding: 10px;
            font-weight: bold;
            font-size: 16px;
            border-radius: 10px;
        }

        .form-link {
            display: block;
            margin-top: 10px;
            text-align: center;
        }

        a {
            color: #2d5b83;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
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
            margin-top: 80px;
        }

        .logo-container {
            text-align: center;
            margin-bottom: 20px;
        }

        .logo-container img {
            max-width: 250px;
        }
    </style>
</head>
""")
print("""
<body>
    <nav class="navbar navbar-default transparent-navbar">
        <div class="container-fluid logo-container">
            <img src="./image/logo.png" alt="Company Logo">
        </div>
    </nav>

    <div class="container">
        <center><h1>Patient Login</h1></center>
        <form method="post">

            <div class="form-group">
                <input type="text" class="form-control" name="PATIENT" required placeholder="Patient ID">
            </div>
            <div class="form-group">
                <input type="text" class="form-control" name="PASS" required placeholder="Password">
            </div>
            <div class="form-link">
                <a href="forgetpassword.py?id=2">Forgot Password?</a>
            </div>
            <div class="form-group" style="margin-top: 15px;">
                <input type="submit" class="btn btn-primary" value="Login" name="SUB">
            </div>
            <div class="form-group">
                <a href="index.py" class="btn btn-danger">Cancel</a>
            </div>
            <p class="form-link">Don't have an account? <a href="patientreg.py">Register</a></p>

        </form>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>

<footer>
    &copy; 2023 Your Company | All Rights Reserved
</footer>

</html>
""")

pid = form.getvalue("PATIENT")
password = form.getvalue("PASS")
submit = form.getvalue("SUB")
if submit != None:
    q = """select id from patient where Username='%s' and Password='%s'""" % (pid, password)
    cur.execute(q)
    idd = cur.fetchone()
    print("""
    <script>
    alert("Login success");
    location.href="patientindex.py?id=%s";
    </script>
    """ % (idd))
