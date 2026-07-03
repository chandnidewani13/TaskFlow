from django.urls import path

from . import views


urlpatterns = [

    # ==========================================
    # AUTHENTICATION
    # ==========================================

    path(
        '',
        views.login_page,
        name='login'
    ),

    path(
        'register/',
        views.register_page,
        name='register'
    ),

    path(
        'forgot-password/',
        views.forgot_password,
        name='forgot_password'
    ),

    path(
        'verify-email/',
        views.verify_email,
        name='verify_email'
    ),


    # ==========================================
    # ADMIN PANEL
    # ==========================================

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'manage-users/',
        views.manage_users,
        name='manage_users'
    ),

    path(
        'manage-teams/',
        views.manage_teams,
        name='manage_teams'
    ),

    path(
        'analytics/',
        views.analytics_page,
        name='analytics'
    ),

    path(
        'reports/',
        views.reports,
        name='reports'
    ),

    path(
        'notifications/',
        views.notifications_page,
        name='notifications'
    ),
    path(
    'uploaded-files/',
    views.uploaded_files,
    name='uploaded_files'
    ),

    path(
        'approvals/',
        views.approvals_page,
        name='approvals'
    ),
    path(
    'logout/',
    views.logout_page,
    name='logout'
),
# ==========================================
# BUSINESS PANEL
# ==========================================

path(
    'business-dashboard/',
    views.business_dashboard,
    name='business_dashboard'
),

path(
    'create-project/',
    views.create_project,
    name='create_project'
),

path(
    'hire-team/',
    views.hire_team,
    name='hire_team'
),

path(
    'meetings/',
    views.meetings_page,
    name='meetings'
),

path(
    'business-reports/',
    views.business_reports,
    name='business_reports'
),

path(
    'project-status/',
    views.project_status,
    name='project_status'
),

    # ==========================================
    # TEAM LEADER PANEL
    # ==========================================

    # ==========================================
# TEAM LEADER PANEL
# ==========================================

path(
    'leader/dashboard/',
    views.leader_dashboard,
    name='leader_dashboard'
),


path(
    'task-management/',
    views.task_management,
    name='task_management'
),

path(
    'kanban/',
    views.kanban_board,
    name='kanban'
),

path(
    'team-members/',
    views.team_members,
    name='team_members'
),

path(
    'team-chat/',
    views.team_chat,
    name='team_chat'
),

path(
    'calendar/',
    views.calendar_page,
    name='calendar'
),

path(
    'leader-analytics/',
    views.leader_analytics,
    name='leader_analytics'
),

    # ==========================================
    # EMPLOYEE PANEL
    # ==========================================

    # ==========================================
# EMPLOYEE PANEL
# ==========================================

path(
    'employee-dashboard/',
    views.employee_dashboard,
    name='employee_dashboard'
),

path(
    'my-tasks/',
    views.my_tasks,
    name='my_tasks'
),

path(
    'employee-kanban/',
    views.employee_kanban,
    name='employee_kanban'
),

path(
    'employee-meetings/',
    views.employee_meetings,
    name='employee_meetings'
),

path(
    'employee-chat/',
    views.employee_chat,
    name='employee_chat'
),

path(
    'uploads/',
    views.uploads_page,
    name='uploads'
),

path(
    'profile/',
    views.employee_profile,
    name='profile'
),
]