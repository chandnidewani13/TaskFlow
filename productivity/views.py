from django.shortcuts import render
from .models import Project, Task
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project, Task, Team, Meeting, Upload
from django.shortcuts import redirect
from .models import Upload
from .models import Team
from datetime import date

# ==========================================
# AUTHENTICATION
# ==========================================
def login_page(request):

    return render(
        request,
        'auth/login.html'
    )
def register_page(request):

    return render(
        request,
        'auth/register.html'
    )


def forgot_password(request):

    return render(
        request,
        'auth/forgot_password.html'
    )
def verify_email(request):

    return render(
        request,
        'auth/verify_email.html'
    )
# ==========================================
# ADMIN PANEL
# ==========================================
def admin_dashboard(request):

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    total_teams = Team.objects.count()

    total_users = Team.objects.count()

    return render(
        request,
        'admin/dashboard.html',
        {
            'total_projects': total_projects,
            'total_tasks': total_tasks,
            'total_teams': total_teams,
            'total_users': total_users
        }
    )
def manage_users(request):

    users = Team.objects.all()

    return render(
        request,
        'admin/manage_users.html',
        {
            'users': users
        }
    )
def manage_teams(request):

    teams = Team.objects.all()

    total_teams = Team.objects.count()

    active_leaders = Team.objects.filter(
        role__icontains='Leader'
    ).count()

    employees = Team.objects.filter(
        role__icontains='Employee'
    ).count()

    return render(
        request,
        'admin/manage_teams.html',
        {
            'teams': teams,
            'total_teams': total_teams,
            'active_leaders': active_leaders,
            'employees': employees
        }
    )
def analytics_page(request):

    total_users = Team.objects.count()

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status='Completed'
    ).count()

    pending_tasks = Task.objects.filter(
        status='Pending'
    ).count()

    return render(
        request,
        'admin/analytics.html',
        {
            'total_users': total_users,
            'total_projects': total_projects,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks
        }
    )
def reports(request):

    reports_data = [

        {
            'name': f'Total Projects ({Project.objects.count()})',
            'generated_by': 'Admin',
            'date': date.today(),
            'status': 'Completed'
        },

        {
            'name': f'Total Tasks ({Task.objects.count()})',
            'generated_by': 'Admin',
            'date': date.today(),
            'status': 'Completed'
        },

        {
            'name': f'Total Team Members ({Team.objects.count()})',
            'generated_by': 'Admin',
            'date': date.today(),
            'status': 'Completed'
        }

    ]
    return render(
        request,
        'admin/reports.html',
        {
            'reports_data': reports_data
        }
    )
def uploaded_files(request):

    uploads = Upload.objects.all().order_by('-id')

    return render(
        request,
        'admin/uploaded_files.html',
        {
            'uploads': uploads
        }
    )

def notifications_page(request):

    notifications = [

        f"{Project.objects.count()} Projects Created",

        f"{Task.objects.count()} Tasks Available",

        f"{Team.objects.count()} Teams Registered",

        f"{Meeting.objects.count()} Meetings Scheduled",

        f"{Upload.objects.count()} Files Uploaded"

    ]

    return render(
        request,
        'admin/notifications.html',
        {
            'notifications': notifications
        }
    )

def approvals_page(request):

    pending_tasks = Task.objects.filter(
        status='Pending'
    )

    return render(
        request,
        'admin/approvals.html',
        {
            'pending_tasks': pending_tasks
        }
    )

def logout_page(request):

    return redirect('/')
# ==========================================
# BUSINESS PANEL
# ==========================================

# ==========================================
# BUSINESS PANEL
# ==========================================

from .models import (
    Project,
    Task,
    Team,
    Meeting
)

def business_dashboard(request):

    total_projects = Project.objects.count()

    pending_tasks = Task.objects.filter(
        status='Pending'
    ).count()

    total_meetings = Meeting.objects.count()

    completed_projects = 0

    for project in Project.objects.all():

        total_tasks = Task.objects.filter(
            project=project
        ).count()

        completed_tasks = Task.objects.filter(
            project=project,
            status='Completed'
        ).count()

        if total_tasks > 0 and total_tasks == completed_tasks:

            completed_projects += 1

    context = {

        'total_projects': total_projects,

        'pending_tasks': pending_tasks,

        'total_meetings': total_meetings,

        'completed_projects': completed_projects
    }
    return render(
        request,
        'business/dashboard.html',
        context
    )
def create_project(request):

    if request.method == "POST":

        Project.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            deadline=request.POST['deadline'],
            priority=request.POST['priority']
        )

        messages.success(
            request,
            "Project created successfully!"
        )
    return render(
        request,
        'business/create_project.html'
    )
def project_status(request):

    projects = Project.objects.all()

    high_priority_count = Project.objects.filter(
        priority="High"
    ).count()

    normal_priority_count = Project.objects.exclude(
        priority="High"
    ).count()

    project_data = []

    for project in projects:

        total_tasks = Task.objects.filter(
            project=project
        ).count()

        completed_tasks = Task.objects.filter(
            project=project,
            status="Completed"
        ).count()

        if total_tasks > 0:

            completion_percentage = int(
                (completed_tasks / total_tasks) * 100
            )

        else:

            completion_percentage = 0

        project_data.append({

            'project': project,

            'total_tasks': total_tasks,

            'completed_tasks': completed_tasks,

            'completion_percentage': completion_percentage
        })

    return render(
        request,
        'business/project_status.html',
        {
            'project_data': project_data,
            'high_priority_count': high_priority_count,
            'normal_priority_count': normal_priority_count,
            'projects': projects
        }
    )

def hire_team(request):

    if request.method == "POST":

        Team.objects.create(

            name=request.POST['name'],

            leader=request.POST['leader'],

            email=request.POST['email'],

            skill=request.POST['skill'],

            role=request.POST['role']
        )

        messages.success(
            request,
            "Team member hired successfully!"
        )

    teams = Team.objects.all()

    return render(
        request,
        'business/hire_team.html',
        {
            'teams': teams
        }
    )

def meetings_page(request):

    if request.method == "POST":

        Meeting.objects.create(

            title=request.POST['title'],

            date=request.POST['date'],

            time=request.POST['time'],

            description=request.POST['description']
        )

        messages.success(
            request,
            "Meeting scheduled successfully!"
        )

    meetings = Meeting.objects.all().order_by('-date')

    return render(
        request,
        'business/meetings.html',
        {
            'meetings': meetings
        }
    )

def business_reports(request):

    total_projects = Project.objects.count()

    total_teams = Team.objects.count()

    total_tasks = Task.objects.count()

    return render(
        request,
        'business/reports.html',
        {
            'total_projects': total_projects,
            'total_teams': total_teams,
            'total_tasks': total_tasks
        }
    )
# ==========================================
# TEAM LEADER PANEL
# ==========================================

# ==========================================
# TEAM LEADER PANEL
# ==========================================

def leader_dashboard(request):

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status='Completed'
    ).count()

    pending_tasks = Task.objects.filter(
        status='Pending'
    ).count()

    total_members = Team.objects.count()

    total_meetings = Meeting.objects.count()

    return render(
        request,
        'leader/dashboard.html',
        {
            'total_projects': total_projects,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'total_members': total_members,
            'total_meetings': total_meetings,
        }
    )

def task_management(request):

    if request.method == "POST":

        project = Project.objects.get(
            id=request.POST['project']
        )

        Task.objects.create(

            project=project,

            title=request.POST['title'],

            priority=request.POST['priority'],

            status=request.POST['status'],

            assigned_to=request.POST['assigned_to'],

            deadline=request.POST['deadline']
        )

        messages.success(
            request,
            "Task created successfully!"
        )

    tasks = Task.objects.all().order_by('-id')

    projects = Project.objects.all()

    return render(
        request,
        'leader/task_management.html',
        {
            'tasks': tasks,
            'projects': projects
        }
    )

def kanban_board(request):

    pending_tasks = Task.objects.filter(
        status='Pending'
    )

    progress_tasks = Task.objects.filter(
        status='In Progress'
    )

    completed_tasks = Task.objects.filter(
        status='Completed'
    )

    return render(

        request,

        'leader/kanban_board.html',

        {

            'pending_tasks': pending_tasks,

            'progress_tasks': progress_tasks,

            'completed_tasks': completed_tasks
        }
    )


def team_members(request):

    members = Team.objects.all()

    return render(
        request,
        'leader/team_members.html',
        {
            'members': members
        }
    )
def team_chat(request):

    return render(
        request,
        'leader/team_chat.html'
    )


def calendar_page(request):

    return render(
        request,
        'leader/calendar.html'
    )

def leader_analytics(request):

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status='Completed'
    ).count()

    pending_tasks = Task.objects.filter(
        status='Pending'
    ).count()

    total_members = Team.objects.count()

    total_meetings = Meeting.objects.count()

    context = {

        'total_projects': total_projects,

        'total_tasks': total_tasks,

        'completed_tasks': completed_tasks,

        'pending_tasks': pending_tasks,

        'total_members': total_members,

        'total_meetings': total_meetings

    }

    return render(
        request,
        'leader/analytics.html',
        context
    )

# ==========================================
# EMPLOYEE PANEL
# ==========================================

# ==========================================
# EMPLOYEE PANEL
# ==========================================

def employee_dashboard(request):

    employee_name = "Rahul"

    assigned_tasks = Task.objects.filter(
        assigned_to=employee_name
    ).count()

    completed_tasks = Task.objects.filter(
        assigned_to=employee_name,
        status='Completed'
    ).count()

    pending_tasks = Task.objects.filter(
        assigned_to=employee_name,
        status='Pending'
    ).count()

    return render(
        request,
        'employee/dashboard.html',
        {
            'assigned_tasks': assigned_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks
        }
    )

def my_tasks(request):

    employee_name = "Rahul"

    tasks = Task.objects.filter(
        assigned_to=employee_name
    ).order_by('-id')

    return render(
        request,
        'employee/my_tasks.html',
        {
            'tasks': tasks
        }
    )

def employee_kanban(request):

    employee_name = "Rahul"

    pending_tasks = Task.objects.filter(
        assigned_to=employee_name,
        status='Pending'
    )

    progress_tasks = Task.objects.filter(
        assigned_to=employee_name,
        status='In Progress'
    )

    completed_tasks = Task.objects.filter(
        assigned_to=employee_name,
        status='Completed'
    )

    return render(
        request,
        'employee/kanban.html',
        {
            'pending_tasks': pending_tasks,
            'progress_tasks': progress_tasks,
            'completed_tasks': completed_tasks
        }
    )

    progress_tasks = Task.objects.filter(

        assigned_to=employee_name,

        status='In Progress'
    )

    completed_tasks = Task.objects.filter(

        assigned_to=employee_name,

        status='Completed'
    )

    return render(

        request,

        'employee/kanban.html',

        {

            'pending_tasks': pending_tasks,

            'progress_tasks': progress_tasks,

            'completed_tasks': completed_tasks
        }
    )


def employee_meetings(request):

    meetings = Meeting.objects.all().order_by('-date')

    return render(
        request,
        'employee/meetings.html',
        {
            'meetings': meetings
        }
    )


def employee_chat(request):

    return render(
        request,
        'employee/chat.html'
    )


def uploads_page(request):

    if request.method == "POST":

        Upload.objects.create(

            title=request.FILES['file'].name,

            file=request.FILES['file']
        )

        messages.success(
            request,
            "File uploaded successfully!"
        )

    uploads = Upload.objects.all().order_by('-id')

    return render(
        request,
        'employee/uploads.html',
        {
            'uploads': uploads
        }
    )
def employee_profile(request):

    employee = Team.objects.filter(
        name="Rahul Sharma"
    ).first()

    return render(
        request,
        'employee/profile.html',
        {
            'employee': employee
        }
    )