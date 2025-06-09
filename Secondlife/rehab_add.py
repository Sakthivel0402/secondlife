#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

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
    <title>Admin Dashboard</title>
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

        .dropdown-toggle::after {
            display: inline-block;
            margin-left: 0.255em;
            vertical-align: 0.255em;
            content: "";
            border-top: 0.3em solid;
            border-right: 0.3em solid transparent;
            border-bottom: 0;
            border-left: 0.3em solid transparent;
            color: var(--primary-color);
        }

        .dropdown-menu {
            background-color: var(--sidebar-color);
            border: 1px solid #dee2e6;
            border-radius: 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .dropdown-item {
            color: var(--dark-color);
            padding: 10px 20px;
            text-decoration: none;
        }

        .dropdown-item:hover {
            background-color: rgba(41, 91, 131, 0.1);
            color: var(--primary-color);
        }

        #content {
            margin-left: 280px;
            padding: 20px;
            transition: all 0.3s;
            min-height: 100vh;
        }

        .navbar {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 15px 0;
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

        .logo-img {
            height: 50px;
            transition: all 0.3s;
        }

        .logo-img:hover {
            transform: scale(1.05);
        }

        .logout-btn {
            color: #dc3545 !important;
            border-left: 3px solid transparent !important;
            text-decoration: none !important;
            padding: 10px 20px;
        }

        .logout-btn:hover {
            background-color: rgba(220, 53, 69, 0.1) !important;
            border-left: 3px solid #dc3545 !important;
        }

        .logout-btn i {
            color: #dc3545 !important;
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
    </style>

    <script>
        function logout() {
            location.href = "index.py";
        }

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('active');
            document.getElementById('content').classList.toggle('active');
        }
    </script>
</head>
""")

print("""
<body>
    <div class="" id="wrapper">
        <!-- Sidebar -->
        <div class="" id="sidebar">
            <div class="sidebar-header">
                <h3 class="text-center">Admin Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="adminindex.py">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li>
                        <a href="patientexis.py">
                            <i class="bi bi-people-fill"></i> Patient List
                        </a>
                    </li>

                    <li>
                        <a href="#doctorSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-person-badge-fill"></i> Doctor
                        </a>
                        <ul class="collapse list-unstyled" id="doctorSubmenu">
                            <li>
                                <a href="doctoradd.py">
                                    <i class="bi bi-person-plus"></i> Add Doctor
                                </a>
                            </li>
                            <li>
                                <a href="doctorexis.py"><i class="bi bi-list-ul"></i> Existing Doctors</a>
                            </li>
                        </ul>
                    </li>

                    <li>
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled" id="appointmentSubmenu">
                            <li>
                                <a href="patientoff_new.py"><i class="bi bi-file-earmark-plus"></i> New</a>
                            </li>
                            <li>
                                <a href="patientoff_exis.py"><i class="bi bi-check-circle"></i> Accepted</a>
                            </li>
                            <li>
                                <a href="patientoff_old.py"><i class="bi bi-archive"></i> Completed</a>
                            </li>
                        </ul>
                    </li>

                    <li >
                        <a href="#awareSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-megaphone"></i> Aware Program
                        </a>
                        <ul class="collapse list-unstyled " id="awareSubmenu">
                            <li >
                                <a href="awarepro.py" style="text-decoration: underline #2d5b83 2px;">
                                    <i class="bi bi-plus-circle"></i> Add
                                </a>
                            </li>
                            <li>
                                <a href="awarepro_exis.py"><i class="bi bi-person-check"></i> Assign Volunteer</a>
                            </li>
                        </ul>
                    </li>

                    <li>
                        <a href="#leaveSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-x"></i> Leave
                        </a>
                        <ul class="collapse list-unstyled" id="leaveSubmenu">
                            <li>
                                <a href="leave_accept.py"><i class="bi bi-envelope"></i> Requests</a>
                            </li>
                            <li>
                                <a href="leave_old.py"><i class="bi bi-clock-history"></i> History</a>
                            </li>
                        </ul>
                    </li>

                    <li class="active">
                        <a href="rehab_add.py">
                            <i class="bi bi-building"></i> Rehabilation Center
                        </a>
                    </li>
                </ul>
            </div>

            <!-- Logout Button at the bottom of the sidebar -->
            <div class="sidebar-footer mb-3">
                <a href="javascript:logout()" class="logout-btn d-block">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            </div>
        </div>

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i> Toggle Menu
                </button>
            <center><h1>Add Rehabilation Center</h1>
                <div class="form-container" >
                <form  method="post" style="width:400px;">
                <div class="form-group mt-5">
                    <input type="text" class="form-control" id="centerName" name="CNAME" required placeholder="Enter Center Name">
                </div>
                <div class="form-group mt-3">
                    <input type="text" class="form-control" id="centerLocation" name="DOOR" required placeholder="Door no">
                </div>
                <div class="form-group mt-3">
                    <input type="text" class="form-control" id="centerLocation" name="ADD1" required placeholder="Address line 1">
                </div>
                <div class="form-group mt-3">
                    <input type="text" class="form-control" id="centerLocation" name="ADD2" required placeholder="Address line 2">
                </div>
                <div class="form-group mt-3">
                    <input type="text" class="form-control" id="centerLocation" name="CITY" required placeholder="city">
                </div> 
                <div class="form-group mt-3">
                    <input type="text" class="form-control" id="centerLocation" name="STATE" required placeholder="state">
                </div>
                <div class="form-group mt-3">
                    <input type="submit" class="form-control btn w-50 btn-primary" name="SUB" required>
                </div>
                </form>
                </center>
                </div>
</body>
</div>
</div>
</div>""")
sub=form.getvalue("SUB")
cname=form.getvalue("CNAME")
door=form.getvalue("DOOR")
Add1=form.getvalue("ADD1")
Add2=form.getvalue("ADD2")
city=form.getvalue("CITY")
state=form.getvalue("STATE")


if sub!= None:
    b="""insert rehab (Cname,Cloc,Address1,Doorno,State,City)values('%s','%s','%s','%s','%s','%s')"""%(cname,Add1,Add2,door,state,city)
    cur.execute(b)
    con.commit()
    print("""
    <script>
    alert("Rehabilation center added");
    </script>
    """)
print("""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")
