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
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient reg</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
        .error {
            color: red;
        }

        .container {
            width: 60%;
            margin-top: 20px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 30px;
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
        }

        h1 {
            color: #2d5b83;
            margin-bottom: 30px;
        }

        .btn-primary {
            background-color: #2d5b83;
            border-color: #2d5b83;
        }

        .btn-danger {
            background-color: #d9534f;
            border-color: #d9534f;
        }

        .form-group label {
            font-weight: bold;
            color: #333;
        }

        .form-group input,
        .form-group select {
            border-radius: 8px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
        }

        .form-group input:focus,
        .form-group select:focus {
            box-shadow: 0px 0px 10px rgba(0, 123, 255, 0.5);
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
            <h1>Patient Register</h1>
        </center>
        <form id="rehabForm" method="post">

            <div class="form-group row">
                <div class="col-md-6">
                    <label for="name">Full Name:</label>
                    <input type="text" class="form-control" id="name" name="NAME" required placeholder="Enter Full Name">
                </div>
                <div class="col-md-6">
                    <label for="email">Email:</label>
                    <input type="email" class="form-control" id="email" name="EMAIL" required placeholder="Enter Email">
                </div>
            </div>
            <div class="form-group row">
                <div class="col-md-4">
                    <label for="dob">Date of Birth:</label>
                    <input type="date" class="form-control" id="dob" name="DOB" required>
                </div>
                <div class="col-md-4">
                    <label for="gender">Gender:</label>
                    <select class="form-control" id="gender" name="GENDER" required>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <label for="phno">Phone Number:</label>
                    <input type="tel" class="form-control" id="phno" name="PHNO" required placeholder="Enter Phone Number">
                </div>
            </div>

            <div class="form-group row">
                <div class="col-md-4">
                    <label for="pincode">Pincode:</label>
                    <input type="text" id="pincode" name="pincode" class="form-control" required placeholder="Enter Pincode" onchange="getAddress()">
                </div>
                <div class="col-md-4">
                    <label for="doorno">Door No:</label>
                    <input type="text" class="form-control" id="doorno" name="DOORNO" required placeholder="Enter Door No">
                </div>
                <div class="col-md-4">
                    <label for="address1">Address Line 1:</label>
                    <input type="text" class="form-control" id="address1" name="ADDRESS1" required placeholder="Enter Address Line 1">
                </div>
            </div>

            <div class="form-group row">
                <div class="col-md-6">
                    <label for="address2">Address Line 2:</label>
                    <input type="text" class="form-control" id="address2" name="ADDRESS2" placeholder="Enter Address Line 2">
                </div>

                <div class="col-md-6">
                    <label for="city">City:</label>
                    <input type="text" class="form-control" id="city" name="CITY" placeholder="Enter City">
                </div>
            </div>

            <div class="form-group row">
                <div class="col-md-6">
                    <label for="state">State:</label>
                    <input type="text" class="form-control" id="state" name="STATE" placeholder="Enter State">
                </div>
                <div class="col-md-6">
                    <label for="country">Country:</label>
                    <input type="text" class="form-control" id="country" name="COUNTRY" placeholder="Enter Country">
                </div>
            </div>

            <div class="form-group row">
                <div class="col-md-6">
                    <label for="username">Create Username:</label>
                    <input type="text" class="form-control" id="username" name="USERNAME" required placeholder="Enter Username">
                </div>
                <div class="col-md-6">
                    <label for="password">Create Password:</label>
                    <input type="password" class="form-control" id="password" name="PASSWORD" required placeholder="Enter Password">
                </div>
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
            </div><br>
            <div class="row" style="margin-left:10px;">
                <p>Already have an account? <a href="patientlogin.py">Login</a></p>
            </div>
        </form>
        <br>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script>
        async function getAddress() {
            const pincode = document.getElementById('pincode').value;
            const apiUrl = `path_to_your_python_script.py?pincode=${pincode}`;

            try {
                const response = await fetch(apiUrl);
                const data = await response.json();

                if (!data.error) {
                    // Log the entire array to the console

                    // Select the first post office (assuming there is at least one)
                    const firstPostOffice = data[0].PostOffice[0];

                    // Update address input fields with details from the first post office
                    document.getElementById('address2').value = firstPostOffice.Description || '';
                    document.getElementById('city').value = firstPostOffice.District || '';
                    document.getElementById('state').value = firstPostOffice.State || '';
                    document.getElementById('country').value = firstPostOffice.Country || '';

                    // Display an alert indicating success
                    alert('Address details fetched successfully!');
                } else {
                    // Clear other address input fields if the PIN code is invalid
                    document.getElementById('address2').value = '';
                    document.getElementById('city').value = '';
                    document.getElementById('state').value = '';
                    document.getElementById('country').value = '';

                    // Display an alert indicating failure
                    alert(data.error);
                }
            } catch (error) {
                console.error('Error fetching data:', error);

                // Display an alert indicating an error
                alert('An error occurred while fetching address details.');
            }
        }
    </script>
</body>
<footer>
    &copy; 2023 Your Company | All Rights Reserved
</footer>

</html>
""")
name = form.getvalue('NAME')
email = form.getvalue('EMAIL')
dob = form.getvalue('DOB')
gender = form.getvalue('GENDER')
phno = form.getvalue('PHNO')
doorno = form.getvalue('DOORNO')
address1 = form.getvalue('ADDRESS1')
address2 = form.getvalue('ADDRESS2')
city = form.getvalue('CITY')
state = form.getvalue('STATE')
country = form.getvalue('COUNTRY')
username = form.getvalue('USERNAME')
password = form.getvalue('PASSWORD')
sub = form.getvalue('SUB')
if sub is not None:
    timestamp_string = str(dob)
    datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d")
    formatted_date = datetime_object.strftime("%d-%m-%Y")
    b = f"""
            INSERT INTO patient (Name, Email, DOB, Gender, Phone, DoorNo,
                                 Address1, Address2, City, State, Country, Username, Password)
            VALUES ('{name}', '{email}', '{timestamp_string}', '{gender}', '{phno}','{doorno}',
                    '{address1}', '{address2}', '{city}', '{state}', '{country}', '{username}', '{password}')
        """
    cur.execute(b)
    con.commit()
    print("""
    <script>
    alert("Registered successfully");
    </script>
    """)
