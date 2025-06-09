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

# Fetch doctor data
q = """select * from doctor where id='%s'""" % (did)
cur.execute(q)
res = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Leave Request</title>

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
            max-width: 600px;
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
    </style>

    <script>
        function logout() {
            location.href = "index.py";
        }

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('active');
            document.getElementById('content').classList.toggle('active');
        }

        // Date validation
        document.addEventListener('DOMContentLoaded', function() {
            const fromDate = document.getElementById('leaveFrom');
            const toDate = document.getElementById('leaveTo');

            fromDate.addEventListener('change', function() {
                toDate.min = this.value;
            });
        });
    </script>
</head>
""")

print("""
<body>
    <div class="" id="wrapper">
        <!-- Sidebar -->
        <div class="" id="sidebar">
            <div class="sidebar-header">
                <h3 class="text-center">Doctor Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="doctorindex.py?id=%s">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li>
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled" id="appointmentSubmenu">
                            <li>
                                <a href="doctorapp_new.py?id=%s"><i class="bi bi-file-earmark-plus"></i> New</a>
                            </li>
                            <li>
                                <a href="doctorapp_old.py?id=%s"><i class="bi bi-check-circle"></i> Accepted</a>
                            </li>
                        </ul>
                    </li>
                    <li class="active">
                        <a href="#leaveSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-calendar-x"></i> Leave
                        </a>
                        <ul class="collapse list-unstyled show" id="leaveSubmenu">
                            <li class="active">
                                <a href="doctor_leave.py?id=%s"><i class="bi bi-envelope"></i> New Request</a>
                            </li>
                            <li>
                                <a href="leave_status.py?id=%s"><i class="bi bi-clock-history"></i> Status</a>
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
        </div>

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i> Toggle Menu
                </button>

                

                <div class="form-container">
                    <h2 class="form-title">Leave Request Form</h2>
                    <form method="post">
                        <div class="mb-3">
                            <label for="leaveReason" class="form-label">Reason for Leave</label>
                            <select class="form-select" id="leaveReason" required name="REASON">
                                <option value="" selected disabled>Select a reason</option>
                                <option value="Vacation">Vacation</option>
                                <option value="Medical">Medical</option>
                                <option value="Personal">Personal</option>
                                <option value="Conference">Conference</option>
                                <option value="Training">Training</option>
                                <option value="Family Emergency">Family Emergency</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-4">
                                <label for="leaveDays" class="form-label">Number of Days</label>
                                <input type="number" class="form-control" id="leaveDays" required name="NO" min="1" placeholder="Days">
                            </div>
                            <div class="col-md-4">
                                <label for="leaveFrom" class="form-label">Leave From</label>
                                <input type="date" class="form-control" id="leaveFrom" required name="FROM">
                            </div>
                            <div class="col-md-4">
                                <label for="leaveTo" class="form-label">Leave To</label>
                                <input type="date" class="form-control" id="leaveTo" required name="TO">
                            </div>
                        </div>

                        <div class="d-grid gap-2">
                            <input type="submit" class="btn btn-primary" value="Submit Request" name="SUB">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""" % (did, did, did, did, did))

# Process form submission
reason = form.getvalue("REASON")
name = res[0][1]
fdate = form.getvalue("FROM")
tdate = form.getvalue("TO")
no = form.getvalue("NO")
sub = form.getvalue("SUB")

if sub != None:
    try:
        timestamp_string = str(fdate)
        datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d")
        formatted_date = datetime_object.strftime("%d-%m-%Y")

        timestamp_string2 = str(tdate)
        datetime_object2 = datetime.strptime(timestamp_string2, "%Y-%m-%d")
        formatted_date2 = datetime_object2.strftime("%d-%m-%Y")

        b = """insert into leaves(Name, Reason, Fromd, Tod, No, Status) 
               values('%s', '%s', '%s', '%s', '%s', 'Requested')""" % (
            name, reason, formatted_date, formatted_date2, no)
        cur.execute(b)
        con.commit()

        print("""
        <script>
        alert("Leave request submitted successfully");
        location.href = "leave_status.py?id=%s";
        </script>
        """ % did)
    except Exception as e:
        print(f"""
        <script>
        alert("Error submitting leave request: {str(e)}");
        </script>
        """)