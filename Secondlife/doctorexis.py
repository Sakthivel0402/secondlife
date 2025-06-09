#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb
import string,random,smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()

def generate_random_string(length):
    characters = string.ascii_letters
    numbers = string.digits
    random_chars = random.choices(characters + numbers, k=length)
    return ''.join(random_chars)


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
            width:1220px !important;
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
            padding:10px 20px;
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
                    <li >
                        <a href="patientexis.py" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-people-fill"></i> Patient List
                        </a>
                    </li>

                    <li class="active">
                        <a href="#doctorSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-person-badge-fill"></i> Doctor
                        </a>
                        <ul class="collapse list-unstyled show" id="doctorSubmenu">
                            <li >
                                <a href="doctoradd.py" style="text-decoration: underline #2d5b83 2px;">
                                    <i class="bi bi-person-plus"></i> Add Doctor
                                </a>
                            </li>
                            <li class="active">
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
            <div class="sidebar-footer  mb-3">
                <a href="javascript:logout()" class="logout-btn d-block">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            </div>
        </div>

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i>
                </button>
      <h1 style="color: var(--primary-color); text-align: center;">Doctor List</h1>
                <div class="table-container">
              
                    <table class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th>SINO</th>
                                <th>Join Date</th>
                                <th>Doctor name</th>
                                <th>Profile</th>
                                <th>Doctorid</th>
                                <th>Gender</th>
                                <th>Email</th>
                                <th>Contact</th>
                                <th>Position</th>
                                <th>City</th>
                                <th>More</th>
                                <th>Password</th>
                            </tr>
                        </thead>
                        <tbody>
""")

w = """select * from doctor"""
cur.execute(w)
rec = cur.fetchall()
si = 1
for i in rec:
    print(f"""
    <tr>
        <td>{si}</td>
        <td>{i[1]}</td>
        <td>{i[8]}</td>
        <td><img src="./doctor_pics/{i[12]}" width="100px" class="img-thumbnail"></td>
        <td>{i[3]}</td>
        <td>{i[6]}</td>
        <td>{i[2]}</td>
        <td>{i[7]}</td>
        <td>{i[13]}</td>
        <td>{i[20]}</td>
        <td>
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#{'myModal' if i[13] == 'aware' else 'myModall'}{i[0]}">
                Readmore
            </button>
        </td>
        <td>
            <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#myModalpass{i[0]}">
                Generate
            </button>
        </td>
    </tr>

    <!-- Modal for Doctor Details -->
    <div class="modal fade" id="{'myModal' if i[13] == 'aware' else 'myModall'}{i[0]}" tabindex="-1" aria-labelledby="doctorModalLabel{i[0]}" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="doctorModalLabel{i[0]}">Doctor Details</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="text-center mb-4">
                        <img src="./doctor_pics/{i[12]}" width="150px" class="img-thumbnail rounded-circle">
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <p><strong>Full Name:</strong> {i[1]}</p>
                            <p><strong>Email:</strong> {i[2]}</p>
                            <p><strong>Date of Birth:</strong> {i[5]}</p>
                            <p><strong>Gender:</strong> {i[6]}</p>
                            <p><strong>Contact:</strong> {i[7]}</p>
                            <p><strong>Join date:</strong> {i[8]}</p>
                        </div>
                        <div class="col-md-6">
                            <p><strong>Degree:</strong> {i[9]}</p>
                            <p><strong>Licence:</strong> {i[10]}</p>
                            <p><strong>Graduation year:</strong> {i[11]}</p>
                            <p><strong>Role:</strong> {i[13]}</p>
                            {f'<p><strong>Specialization:</strong> {i[15]}</p>' if i[13] != "aware" else ''}
                            <p><strong>Year of Experience:</strong> {i[14] if i[13] == "aware" else i[16]}</p>
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-6">
                            <h5>Address Details</h5>
                            <p><strong>Door no:</strong> {i[17]}</p>
                            <p><strong>Address line1:</strong> {i[18]}</p>
                            <p><strong>Address line2:</strong> {i[19]}</p>
                        </div>
                        <div class="col-md-6">
                            <h5>Location</h5>
                            <p><strong>City:</strong> {i[20]}</p>
                            <p><strong>State:</strong> {i[21]}</p>
                            <p><strong>Country:</strong> {i[22]}</p>
                        </div>
                    </div>
                    <div class="mt-3">
                        <p><strong>Docid:</strong> {i[3]}</p>
                        <p><strong>Password:</strong> *****</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal for Password Generation -->
    <div class="modal fade" id="myModalpass{i[0]}" tabindex="-1" aria-labelledby="passwordModalLabel{i[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <form method="post">
                    <div class="modal-header">
                        <h5 class="modal-title" id="passwordModalLabel{i[0]}">Generate Password</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label class="form-label">Doctor ID</label>
                            <input type="text" value="{i[3]}" name="DID" class="form-control"> 
                        </div>
                        <input type="hidden" value="{i[0]}" name="ID" class="form-control">
                        <input type="hidden" value="{i[1]}" name="NAME" class="form-control"> 
                        <input type="hidden" value="{i[2]}" name="EMAIL" class="form-control"> 
                        <input type="hidden" value="{i[5]}" name="DOB" class="form-control"> 
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <input type="Submit" value="Generate" name="SUB" class="btn btn-primary"> 
                    </div>
                </form>
            </div>
        </div>
    </div>
    """)
    si += 1

print("""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

did=form.getvalue("DID")
gid=form.getvalue("ID")
gname=form.getvalue("NAME")
gemail=form.getvalue("EMAIL")
gdob=form.getvalue("DOB")
gsub=form.getvalue("SUB")

if gsub!=None:
    gpassword = gemail[:3] + gdob[1:4] + generate_random_string(2)
    b="""update doctor SET DoctorID='%s',Password='%s' WHERE id='%s'"""%(did,gpassword,gid)
    cur.execute(b)
    con.commit()
    fromadd = 'badrinathcvb@gmail.com'
    passworD = 'mgpe dzpq ueup rwvt'
    toadd = gemail
    subject = """This is Your Doctorid And Password"""
    body = "welcome {} \n Doctorid:{} \n password:{}".format(gname, did,gpassword)
    msg = """ Subject:{} \n\n {}""".format(subject, body)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromadd, passworD)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""
    <script>
    alert("Password generated");

    </script>
    """)
print("""
  </center>

</div>
</div>
</div>

</body>
</html>
""")
