#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, os
import cgitb, string, random
import smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("id")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Password</title>
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

        input[type="text"] {
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
        <center><h1>Reset Password</h1></center>
        <form method="post">

            <div class="form-group">
                <input type="text" class="form-control" name="MAIL" required placeholder="Enter Email">
            </div>

            <div class="form-link">
                <a href="index.py">Back to Login</a>
            </div>

            <div class="form-group" style="margin-top: 15px;">
                <input type="submit" class="btn btn-primary" value="Submit" name="SUB">
            </div>
            <div class="form-group">
                <a href="index.py" class="btn btn-danger">Cancel</a>
            </div>
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

pid = form.getvalue("MAIL")
submit = form.getvalue("SUB")
if submit != None:
    if id != 1:
        q = """select * from patient where Email='%s'""" % (pid)
        cur.execute(q)
        idd = cur.fetchone()
        if idd != None:
            fromadd = 'badrinathcvb@gmail.com'
            password = 'mgpe dzpq ueup rwvt'
            toadd = idd[0][2]
            subject = "Reset Password"
            body = "Hi {}\nPatient ID: {}\nPassword: {}\nThank you,\nSecondlife Team".format(idd[0][1], idd[0][16],
                                                                                             idd[0][17])
            msg = """Subject: {} \n\n {}""".format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromadd, password)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print("""
            <script>
            alert("Id & password sent to email.");
            location.href="patientlogin.py";
            </script>
            """)
    else:
        q = """select * from doctor where Email='%s'""" % (pid)
        cur.execute(q)
        idd = cur.fetchone()
        if idd != None:
            fromadd = 'badrinathcvb@gmail.com'
            password = 'mgpe dzpq ueup rwvt'
            toadd = idd[0][2]
            subject = "Reset Password"
            body = "Hi {}\nDoctor ID: {}\nPassword: {}\nThank you,\nSecondlife Team".format(idd[0][1], idd[0][3],
                                                                                            idd[0][4])
            msg = """Subject: {} \n\n {}""".format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromadd, password)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print("""
                    <script>
                    alert("Id & password sent to email.");
                    location.href="doctorlogin.py";
                    </script>
                    """)
