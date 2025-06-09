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

        .welcome-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            margin-top: 30px;
            border: none;
        }

        .table-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            margin-top: 30px;
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
                    <li class="active">
                        <a href="patientexis.py" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-people-fill"></i> Patient List
                        </a>
                    </li>

                    <li>
                        <a href="#doctorSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-person-badge-fill"></i> Doctor
                        </a>
                        <ul class="collapse list-unstyled" id="doctorSubmenu">
                            <li>
                                <a href="doctoradd.py"><i class="bi bi-person-plus"></i> Add Doctor</a>
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

                    <li>
                        <a href="#awareSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-megaphone"></i> Aware Program
                        </a>
                        <ul class="collapse list-unstyled" id="awareSubmenu">
                            <li>
                                <a href="awarepro.py"><i class="bi bi-plus-circle"></i> Add</a>
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

                    <li>
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
                    <button class="btn btn-primary d-lg-none" onclick="toggleSidebar()">
                        <i class="bi bi-list"></i>
                    </button>

                </div>

                    <h1 style="color: #2d5b83; text-align: center;">Patient List</h1>

            <div class="container-fluid">
                <div class="table-container">
                    <table class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th>SINO</th>
                                <th>Patient name</th>
                                <th>Gender</th>
                                <th>Reg On</th>
                                <th>City</th>
                                <th>Patientid</th>
                                <th>Password</th>
                                <th>Edit</th>
                            </tr>
                        </thead>
                        <tbody>
""")

w = """select * from patient"""
cur.execute(w)
rec = cur.fetchall()
si = 1
for i in rec:
    timestamp_string = str(i[18])
    datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S")
    formatted_date = datetime_object.strftime("%d-%m-%Y")
    print(f"""
                            <tr>
                                <td>{si}</td>
                                <td>{i[1]}</td>
                                <td>{i[4]}</td>
                                <td>{formatted_date}</td>
                                <td>{i[13]}</td>
                                <td>{i[16]}</td>
                                <td>****</td>

<td><button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal{i[0]}">Edit</button></td>

<div class="modal fade" id="myModal{i[0]}" tabindex="-1" aria-labelledby="modalLabel{i[0]}" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <form method="post" >
        <div class="modal-header">
          <h5 class="modal-title" id="modalLabel{i[0]}">Edit Patient Details</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <input type="hidden" name="id" value="{i[0]}">

          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label">Name</label>
              <input type="text" class="form-control" name="Name" value="{i[1]}">
            </div>
            <div class="col-md-6">
              <label class="form-label">Email</label>
              <input type="email" class="form-control" name="Email" value="{i[2]}">
            </div>

            <div class="col-md-4">
              <label class="form-label">DOB</label>
              <input type="date" class="form-control" name="Dob" value="{i[3]}">
            </div>
            <div class="col-md-4">
              <label class="form-label">Gender</label>
              <select class="form-select" name="Gender">
                <option value="Male" {'selected' if i[4] == 'Male' else ''}>Male</option>
                <option value="Female" {'selected' if i[4] == 'Female' else ''}>Female</option>
                <option value="Other" {'selected' if i[4] == 'Other' else ''}>Other</option>
              </select>
            </div>
            <div class="col-md-4">
              <label class="form-label">Phone</label>
              <input type="text" class="form-control" name="Phone" value="{i[5]}">
            </div>

            <div class="col-md-6">
              <label class="form-label">Aware or Addicted</label>
              <input type="text" class="form-control" name="AwareOrAddicted" value="{i[6]}">
            </div>
            <div class="col-md-6">
              <label class="form-label">Aware For</label>
              <input type="text" class="form-control" name="AwareFor" value="{i[7]}">
            </div>

            <div class="col-md-6">
              <label class="form-label">Addiction Type</label>
              <input type="text" class="form-control" name="AddictionType" value="{i[8]}">
            </div>
            <div class="col-md-6">
              <label class="form-label">Years in Addiction</label>
              <input type="text" class="form-control" name="YearsInAddiction" value="{i[9]}">
            </div>

            <div class="col-md-4">
              <label class="form-label">Door No</label>
              <input type="text" class="form-control" name="DoorNo" value="{i[10]}">
            </div>
            <div class="col-md-8">
              <label class="form-label">Address Line 1</label>
              <input type="text" class="form-control" name="Address1" value="{i[11]}">
            </div>

            <div class="col-md-12">
              <label class="form-label">Address Line 2</label>
              <input type="text" class="form-control" name="Address2" value="{i[12]}">
            </div>

            <div class="col-md-4">
              <label class="form-label">City</label>
              <input type="text" class="form-control" name="City" value="{i[13]}">
            </div>
            <div class="col-md-4">
              <label class="form-label">State</label>
              <input type="text" class="form-control" name="State" value="{i[14]}">
            </div>
            <div class="col-md-4">
              <label class="form-label">Country</label>
              <input type="text" class="form-control" name="Country" value="{i[15]}">
            </div>

            <div class="col-md-6">
              <label class="form-label">Username</label>
              <input type="text" class="form-control" name="Username" value="{i[16]}">
            </div>
            <div class="col-md-6">
              <label class="form-label">Password</label>
              <input type="password" class="form-control" name="Password" value="{i[17]}">
            </div>

            <div class="col-md-6">
              <label class="form-label">Registration Date</label>
              <input type="date" class="form-control" name="regdate" value="{i[18].date()}">
            </div>
          </div>
        </div>

        <div class="modal-footer">
          <input type="submit" class="btn btn-success" name="submit" value="Save">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </form>
    </div>
  </div>
</div>



                            </tr>
    """)
    si += 1


print(f"""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

submit = form.getvalue("submit")
if submit is not None:
    try:
        cur.execute("""
            UPDATE patient
            SET 
                Name = %s,
                Email = %s,
                Dob = %s,
                Gender = %s,
                Phone = %s,
                AwareOrAddicted = %s,
                AwareFor = %s,
                AddictionType = %s,
                YearsInAddiction = %s,
                DoorNo = %s,
                Address1 = %s,
                Address2 = %s,
                City = %s,
                State = %s,
                Country = %s,
                Username = %s,
                Password = %s,
                regdate = %s
            WHERE id = %s
        """, (
            form.getvalue('Name'), form.getvalue('Email'), form.getvalue('Dob'),
            form.getvalue('Gender'), form.getvalue('Phone'), form.getvalue('AwareOrAddicted'),
            form.getvalue('AwareFor'), form.getvalue('AddictionType'), form.getvalue('YearsInAddiction'),
            form.getvalue('DoorNo'), form.getvalue('Address1'), form.getvalue('Address2'),
            form.getvalue('City'), form.getvalue('State'), form.getvalue('Country'),
            form.getvalue('Username'), form.getvalue('Password'), form.getvalue('regdate'),
            form.getvalue('id')
        ))
        con.commit()
        print("""
        <script>
            alert("Patient details updated successfully!");
            window.location.href = "patientexis.py";
        </script>
        """)
    except Exception as e:
        print(f"<script>alert('Update failed: {str(e)}');</script>")


