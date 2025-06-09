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
pid = form.getvalue("id")
dname2= form.getvalue("id2")
cur.execute(f"""select Name from doctor where id='{dname2}' """)
dname=cur.fetchone()



# Fetch patient data
q = """select * from patient where id='%s'""" % (pid)
cur.execute(q)
res = cur.fetchall()
pname = res[0][1]
pgender = res[0][4]
pcity = res[0][13]

# Update chat status
zero = "0"
d = """update chat set d='%s' where patient='%s' and doctor='%s'""" % (zero, pname, dname[0])
cur.execute(d)
con.commit()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Chat</title>

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
            --doctor-message-color: #d1e7dd;
            --patient-message-color: #f8f9fa;
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

        .chat-container {
            max-width: 1200px;
            margin: 0 auto;
            height: calc(100vh - 50px);
            display: flex;
            flex-direction: column;
        }

        .chat-header {
            background-color: var(--primary-color);
            color: white;
            padding: 15px 20px;
            border-radius: 8px 8px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chat-body {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background-color: white;
            border-left: 1px solid #dee2e6;
            border-right: 1px solid #dee2e6;
        }

        .chat-footer {
            background-color: white;
            padding: 15px 20px;
            border-radius: 0 0 8px 8px;
            border: 1px solid #dee2e6;
        }

        .message {
            margin-bottom: 15px;
            display: flex;
            flex-direction: column;
        }

        .message-doctor {
            align-items: flex-start;
        }

        .message-patient {
            align-items: flex-end;
        }

        .message-bubble {
            max-width: 70%;
            padding: 12px 15px;
            border-radius: 18px;
            position: relative;
            word-wrap: break-word;
        }

        .message-doctor .message-bubble {
            background-color: var(--doctor-message-color);
            border: 1px solid #d1e7dd;
            border-radius: 0 18px 18px 18px;
        }

        .message-patient .message-bubble {
            background-color: var(--patient-message-color);
            border: 1px solid #dee2e6;
            border-radius: 18px 0 18px 18px;
        }

        .message-time {
            font-size: 0.75rem;
            color: #6c757d;
            margin-top: 5px;
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

            .message-bubble {
                max-width: 85%;
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

        // Function to scroll the chat container to the bottom
        function scrollToBottom() {
            var chatContainer = document.querySelector('.chat-body');
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        // Call scrollToBottom after the page loads to initially scroll to the bottom
        window.onload = function() {
            scrollToBottom();
        };

        // Auto-refresh functionality
        const IDLE_TIME_THRESHOLD = 3000; // 3 seconds
        let idleTimer;

        function resetIdleTimer() {
            clearTimeout(idleTimer);
            idleTimer = setTimeout(reloadPage, IDLE_TIME_THRESHOLD);
        }

        function reloadPage() {
            location.reload();
        }

        function handleUserActivity() {
            resetIdleTimer();
        }

        // Attach event listeners for user activity
        document.addEventListener('mousemove', handleUserActivity);
        document.addEventListener('keydown', handleUserActivity);

        // Initial setup
        resetIdleTimer();
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
                        <a href="patientindex.py?id={pid}">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li>
                                <a href="patientreq.py?id={pid}"><i class="bi bi-file-earmark-plus"></i> Request</a>
                            </li>
                            <li class="active">
                                <a href="patientstatus.py?id={pid}"><i class="bi bi-list-check"></i> Status</a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>

            <!-- Logout Button at the bottom of the sidebar -->
            <div class="sidebar-footer mb-3">
                <a href="javascript:logout()" class="logout-btn d-block ">
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

                <div class="chat-container">
                    <div class="chat-header">
                        <h4 class="mb-0"><i class="bi bi-person-fill"></i> Chat with Dr. {dname[0]}</h4>
                        <a href="patient_com.py?id={pid}" class="btn btn-sm btn-danger">
                            <i class="bi bi-arrow-left"></i> Back
                        </a>
                    </div>

                    <div class="chat-body">
""")

# Fetch chat messages
recie = """select * from chat where patient='%s' and doctor='%s'""" % (pname, dname[0])
cur.execute(recie)
recie2 = cur.fetchall()

for j in recie2:
    if j[4] == "Doctor":
        print(f"""
                        <div class="message message-doctor">
                            <div class="message-bubble">
                                {j[3]}
                                <div class="message-time">{j[8]}</div>
                            </div>
                        </div>""")
    elif j[4] == "Patient":
        print(f"""
                        <div class="message message-patient">
                            <div class="message-bubble">
                                {j[3]}
                                <div class="message-time">{j[8]}</div>
                            </div>
                        </div>""")

print(f"""
                    </div>

                    <div class="chat-footer">
                        <form method="post" class="d-flex">
                            <input type="hidden" name="PATIENT" value="{pname}">
                            <input type="hidden" name="DOCTOR" value="{dname[0]}">
                            <input type="text" class="form-control me-2" placeholder="Type your message..." name="MESSAGE" required>
                            <input type="submit" class="btn btn-primary" name="SEND"
                                value="Send">
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

# Handle message sending
send = form.getvalue("SEND")
doctor = form.getvalue("DOCTOR")
patient = form.getvalue("PATIENT")
message = form.getvalue("MESSAGE")

if send is not None and message:
    # Insert new message
    b = """insert into chat(patient, doctor, message, sender, p) values('%s', '%s', '%s', 'Patient', 'yes')""" % (
    patient, doctor, message)
    cur.execute(b)
    con.commit()

    # Update message count and timestamp
    bd = """select * from chat where patient='%s' and doctor='%s'""" % (patient, doctor)
    cur.execute(bd)
    um = cur.fetchall()
    im = int(um[0][5])
    uum = im + 1
    uuum = str(uum)

    max_id_query = "SELECT MAX(id) FROM chat"
    cur.execute(max_id_query)
    max_id = cur.fetchone()[0]

    q = "SELECT regtime FROM chat WHERE id ='%s'" % (max_id)
    cur.execute(q)
    timestamp_string = str(cur.fetchone()[0])
    datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S.%f")
    formatted_date = datetime_object.strftime("%H:%M | %d-%m-%Y")

    hv = """update chat set mtime='%s' where id='%s'""" % (formatted_date, max_id)
    cur.execute(hv)
    con.commit()

    d = """update chat set p='%s' where patient='%s' and doctor='%s'""" % (uuum, patient, doctor)
    cur.execute(d)
    con.commit()

    print(f"""
    <script>
        window.location.replace("patient_chat.py?id={pid}&id2={dname2}");
    </script>
    """)