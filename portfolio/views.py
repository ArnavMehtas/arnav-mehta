from django.shortcuts import render
from .models import *
# Create your views here.
# portfolio/views.py
from django.shortcuts import render, get_object_or_404
# ...

def index(request):
    selected_skill = request.GET.get("skill")          # <-- NEW
    projects = (Project.objects.filter(skills__id=selected_skill).order_by('-date')
            if selected_skill else Project.objects.all().order_by('-date'))

    experience_links={
        "Data Analyst at Wildnet Technologies":"https://drive.google.com/file/d/1p1DBtZkCEz5YFx1HrPEN6L2HcMRIMCaz/view?usp=sharing"
    }

    achievement_links = {
        "Letter of Recommendation from Wildnet":"https://drive.google.com/file/d/1OZCWlx-GGMrC5DQxlsK3BHHevBhlBki3/view?usp=sharing",
        "Cyber Security A.P.":"https://www.linkedin.com/posts/arnav-mehta-1b5b93226_learning-hacking-cybersecurity-activity-7015959581289779200-L2vn?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADjFklkB5EctP2DgK_ePgTXUJZHAJlhUtYQ",
        "Career Essentials in Data Analysis by Microsoft":"https://www.linkedin.com/posts/arnav-mehta-1b5b93226_certificate-of-completion-activity-7199088385863426050-Kb9V?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADjFklkB5EctP2DgK_ePgTXUJZHAJlhUtYQ",
        "JKSD 30 hour Training":"https://www.linkedin.com/posts/arnav-mehta-1b5b93226_hello-connections-i-am-thrilled-to-announce-activity-7200819136262725632-8_mF?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADjFklkB5EctP2DgK_ePgTXUJZHAJlhUtYQ",
        "Deep Learning Specialization":"https://coursera.org/share/77f5d34c727a165c17509ceb0e6b9073",
    }
    context = {
        "profile": Profile.objects.first(),
        "skills_by_category": _build_skill_dict(),     # pulled-out helper, see below
        "projects": projects,
        "experience": Experience.objects.all().order_by("-start_date"),
        "education": Education.objects.all().order_by("-year_completed"),
        "achievements": Achievement.objects.all(),
        "selected_skill": selected_skill,  
        "experience_links": experience_links,
        "achievement_links": achievement_links
        }
    return render(request, "portfolio/index.html", context)


def _build_skill_dict():
    skills_by_category = {}
    for s in Skill.objects.all():
        skills_by_category.setdefault(s.category, []).append(s)
    return skills_by_category

def achievement_detail(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    
    return render(request, "portfolio/achievement_detail.html",
                  {"achievement": achievement,
                   "profile": Profile.objects.first()})
