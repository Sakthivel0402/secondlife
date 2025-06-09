#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb
from datetime import datetime

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()
did = form.getvalue("id")

# Fetch patient data
q = """select * from patient where id='%s'""" % (did)
cur.execute(q)
res = cur.fetchall()
pname = res[0][1]
pgender = res[0][4]
pcity = res[0][13]

# Fetch doctors
l = """select * from doctor where Role='Physician' """
cur.execute(l)
add = cur.fetchall()
p = """select * from doctor where Role='aware'"""
cur.execute(p)
aw = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Appointment</title>

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">

    <style>
        :root {
            --primary-color: #2d5b83;
            --secondary-color: #1a3a5e;
            --sidebar-color: #ffffff;
            --sidebar-header-color: #2d5b83;
            --accent-color: #4a90e2;
            --light-color: #f8f9fa;
            --dark-color: #212529;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            min-height: 100vh;
        }

        #sidebar {
            background-color: var(--sidebar-color);
            color: var(--dark-color);
            height: 100vh;
            position: fixed;
            width: 280px;
            transition: all 0.3s;
            z-index: 1000;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
            border-right: 1px solid #dee2e6;
            display: flex;
            flex-direction: column;
        }

        #sidebar .sidebar-header {
            padding: 20px;
            background-color: var(--sidebar-header-color);
            color: white;
        }

        #sidebar .sidebar-content {
            flex: 1;
            overflow-y: auto;
        }

        #sidebar ul.components {
            padding: 20px 0;
            display: flex;
            flex-direction: column;
        }

        #sidebar ul li a {
            padding: 12px 20px;
            color: var(--dark-color);
            display: block;
            transition: all 0.3s;
            border-left: 3px solid transparent;
            text-decoration: none !important;
        }

        #sidebar ul li a:hover {
            background-color: rgba(41, 91, 131, 0.1);
            color: var(--primary-color);
            text-decoration: none;
            border-left: 3px solid var(--primary-color);
        }

        #sidebar ul li.active > a {
            background-color: rgba(41, 91, 131, 0.1);
            color: var(--primary-color);
            border-left: 3px solid var(--primary-color);
            font-weight: 500;
        }

        #sidebar ul li a i {
            margin-right: 10px;
            width: 20px;
            text-align: center;
            color: var(--primary-color);
        }

        #content {
            margin-left: 280px;
            padding: 20px;
            transition: all 0.3s;
            min-height: 100vh;
        }

        .form-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            margin-top: 30px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .form-title {
            color: var(--primary-color);
            margin-bottom: 30px;
            text-align: center;
            font-weight: 600;
        }

        .form-label {
            font-weight: 500;
            color: var(--secondary-color);
        }

        .btn-primary {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
            padding: 10px 25px;
        }

        .btn-primary:hover {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }

        .btn-danger {
            padding: 10px 25px;
        }

        .logo-img {
            height: 80px;
            transition: all 0.3s;
        }

        .logo-img:hover {
            transform: scale(1.05);
        }

        @media (max-width: 768px) {
            #sidebar {
                margin-left: -280px;
            }

            #sidebar.active {
                margin-left: 0;
            }

            #content {
                margin-left: 0;
            }

            #content.active {
                margin-left: 280px;
            }
        }
        
        .logout-btn {
            color: #dc3545 !important;
            padding: 10px 20px;
            transition: all 0.3s;
            text-decoration:none;
            border-left: 3px solid transparent !important;
        }

        .logout-btn:hover {
            background-color: rgba(220, 53, 69, 0.1) !important;
            border-left: 3px solid #dc3545 !important;
            transition: all 0.3s;
        }

        .logout-btn i {
            color: #dc3545 !important;
        }
    </style>

    <script>
        function logout() {
            location.href = "index.py";
        }

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('active');
            document.getElementById('content').classList.toggle('active');
        }

        $(document).ready(function () {
            $('#awareOrAddicted').change(function () {
                var awareForContainer = $('#awareForContainer');
                var addictionTypeContainer = $('#addictionTypeContainer');

                if (this.value === 'aware') {
                    awareForContainer.show();
                    addictionTypeContainer.hide();
                } else if (this.value === 'addicted') {
                    awareForContainer.hide();
                    addictionTypeContainer.show();
                } else {
                    awareForContainer.hide();
                    addictionTypeContainer.hide();
                }
            });

            // Basic client-side validation
            $('#appointmentForm').submit(function () {
                var isValid = true;

                // Reset previous validation styles
                $('.form-control').removeClass('is-invalid');

                // Validate each required field
                $('.form-control[required]').each(function () {
                    if (!$(this).val()) {
                        isValid = false;
                        $(this).addClass('is-invalid');
                    }
                });

                return isValid;
            });
        });
    </script>
</head>
""")

print(f"""
<body>
    <div class="" id="wrapper">
        <!-- Sidebar -->
        <div class="" id="sidebar">
            <div class="sidebar-header">
                <h3 class="text-center">Patient Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="patientindex.py?id={did}">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li class="active">
                                <a href="patientreq.py?id={did}">
                                    <i class="bi bi-file-earmark-plus"></i> Request
                                </a>
                            </li>
                            <li>
                                <a href="patientstatus.py?id={did}">
                                    <i class="bi bi-clock-history"></i> Status
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
                </div>
                <div class="sidebar-footer mb-3">
                <a href="javascript:logout()" class="logout-btn d-block">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            
            </div>
        </div>""")
print(f"""

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i> Toggle Menu
                </button>

               

                <div class="form-container">
                    <h2 class="form-title">Request Appointment</h2>
                    <form id="appointmentForm" method="post">
                        <div class="mb-3">
                            <label for="awareOrAddicted" class="form-label">Appointment Type</label>
                            <select class="form-select" id="awareOrAddicted" name="AWAREORADDICTED" required>
                                <option value="" selected disabled>Select appointment type</option>
                                <option value="aware">Awareness Program</option>
                                <option value="addicted">Addiction Treatment</option>
                            </select>
                        </div>

                        <div id="awareForContainer" class="mb-3" style="display:none;">
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <label for="awareFor" class="form-label">Awareness Topic</label>
                                    <select class="form-select" id="awareFor" name="AWAREFOR">
                                        <option value="alcohol">Alcohol Addiction</option>
                                        <option value="drugs">Drug Addiction</option>
                                        <option value="gambling">Gambling Addiction</option>
                                        <option value="technology">Technology/Internet Addiction</option>
                                        <option value="food">Food Addiction</option>
                                        <option value="shopping">Shopping Addiction</option>
                                    </select>
                                </div>
                                <div class="col-md-6 mb-3">
                                    <label for="special" class="form-label">Consult With</label>
                                    <select class="form-select" name="SPECIAL">""")

for i in aw:
    print(f"""
                                        <option value="{i[1]}">{i[1]}</option>""")

print("""
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div id="addictionTypeContainer" class="mb-3" style="display:none;">
                            <div class="row">
                                <div class="col-md-4 mb-3">
                                    <label for="addictionType" class="form-label">Addiction Type</label>
                                    <select class="form-select" id="addictionType" name="ADDICTIONTYPE">
                                        <option value="alcohol">Alcohol Addiction</option>
                                        <option value="drugs">Drug Addiction</option>
                                        <option value="gambling">Gambling Addiction</option>
                                        <option value="technology">Technology/Internet Addiction</option>
                                        <option value="food">Food Addiction</option>
                                        <option value="shopping">Shopping Addiction</option>
                                    </select>
                                </div>
                                <div class="col-md-4 mb-3">
                                    <label for="yearsInAddiction" class="form-label">Years in Addiction</label>
                                    <input type="number" class="form-control" id="yearsInAddiction" name="YEARSINADDICTION" min="0" placeholder="Enter years">
                                </div>
                                <div class="col-md-4 mb-3">
                                    <label for="specialist" class="form-label">Consult With</label>
                                    <select class="form-select" name="SPECIAL1">""")

for i in add:
    print(f"""
                                        <option value="{i[1]}">{i[1]} ({i[15]})</option>""")

print("""
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="apointon" class="form-label">Appointment Date</label>
                                <input type="date" class="form-control" name="APOINTON" required>
                            </div>
                            <div class="col-md-6">
                                <label for="change" class="form-label">If Doctor Unavailable</label>
                                <select class="form-select" name="CHANGE">
                                    <option value="OK">Appoint available doctor</option>
                                    <option value="NO">Wait for selected doctor</option>
                                </select>
                            </div>
                        </div>

                        <input type="hidden" value="offline" name="MODE">
                        <input type="hidden" value="%s" name="NAME">
                        <input type="hidden" value="%s" name="GENDER">
                        <input type="hidden" value="%s" name="CITY">

                        <div class="d-flex justify-content-center mt-4">
                            <input type="submit" class="btn btn-primary me-3" name="SUB" value="Submit Request">
                            <a href="javascript:history.back()" class="btn btn-danger">Cancel</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <!-- jQuery -->
""" % (pname, pgender, pcity))

# Process form submission
aoa = form.getvalue("AWAREORADDICTED")
awarefor = form.getvalue("AWAREFOR")
addictedtype = form.getvalue("ADDICTIONTYPE")
yia = form.getvalue("YEARSINADDICTION")
apointon = form.getvalue("APOINTON")
name = form.getvalue("NAME")
change = form.getvalue("CHANGE")
special = form.getvalue("SPECIAL")
special1 = form.getvalue("SPECIAL1")
sub = form.getvalue("SUB")
Mode = form.getvalue("MODE")

if sub != None:
    Gender = form.getvalue("GENDER")
    City = form.getvalue("CITY")
    timestamp_string = str(apointon)
    datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d")
    formatted_date = datetime_object.strftime("%d-%m-%Y")

    if aoa == "aware":
        q = """insert into aware(patient,awarefor,apointon,gender,city,status,mode,doctor,changee) 
               values('%s','%s','%s','%s','%s','Requested','%s','%s','%s')""" % (
            name, awarefor, formatted_date, Gender, City, Mode, special, change)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Appointment requested successfully");
        location.href = "patientstatus.py?id=%s";
        </script>
        """ % did)
    elif aoa == "addicted":
        w = """insert into addicted(patient,addictedfor,yinaddict,apointon,gender,city,status,doctor,mode,changee) 
               values('%s','%s','%s','%s','%s','%s','Requested','%s','%s','%s')""" % (
            name, addictedtype, yia, formatted_date, Gender, City, special1, Mode, change)
        cur.execute(w)
        con.commit()
        print("""
        <script>
        alert("Appointment requested successfully");
        location.href = "patientstatus.py?id=%s";
        </script>
        """ % did)

print("""
</body>
</html>
""")