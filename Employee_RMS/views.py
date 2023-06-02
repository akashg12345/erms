
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from .forms import EmployeeForm
from django.contrib import messages
from .models import EmployeeCreate, EmployeeEducation1, StudentResult, StudyMaterial, TestResults
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import csv

# Create your views here.


def Home(request):
    return render(request, "home.html")


def registration(request):

    if request.method == "POST":

        if request.POST["pwd"] != request.POST["cpwd"]:
            messages.success(
                request, "please confirm that password and confirm password should be same  !!!")
            return redirect("registration")
        else:
            N = request.POST["Fname"]
            L = request.POST["Lname"]
            P = request.POST["pwd"]
            EC = request.POST["Ecode"]
            EM = request.POST["Email"]

            cv = request.FILES["cover1"]

            error = ""

            U = User.objects.create_user(
                username=EM, password=P, first_name=N, last_name=L)
            U.save()

            try:
                object = EmployeeCreate.objects.create(
                    FirstName=N, LastName=L, Ecode=EC, Email=EM, user=U, cover=cv)
                object.save()
                exp = StudentResult.objects.create(user=U)
                exp.save()
                edu = EmployeeEducation1.objects.create(user=U)
                edu.save()
                error = "no"

            except:
                error = "yes"

    return render(request, "registration.html", locals())


def employee_login(request):
    error = ""
    if request.method == "POST":
        U = request.POST["Email"]
        P = request.POST["pwd"]
        user_auth = authenticate(username=U, password=P)
        if user_auth:
            login(request, user_auth)
            error = "no"
        else:
            error = "yes"

    return render(request, "employee_login.html", locals())


def employee_home(request):
    print(request.user.is_authenticated)

    if not request.user.is_authenticated:
        return redirect("employee_login")

    return render(request, "employee_home.html")


def employee_profile(request):
    if not request.user.is_authenticated:
        return redirect("employee_login")
    error = ""
    user = request.user
    employee = EmployeeCreate.objects.get(user=user)
    if request.method == "POST":
        N = request.POST["Fname"]
        L = request.POST["Lname"]

        EC = request.POST["Ecode"]

        Edesig = request.POST["Edesig"]
        ED = request.POST["ED"]
        ECONT = request.POST["contact"]
        JDate = request.POST["Jdate"]
        G = request.POST["gender"]

        if JDate:
            employee.date_created = JDate

        employee.user.first_name = N
        employee.user.last_name = L
        employee.Ecode = EC
        employee.Edesignation = Edesig
        employee.Econtact = ECONT
        employee.Edepartment = ED
        employee.FirstName = N
        employee.gender = G
        employee.LastName = L

        # employee.save()

        # employee.user.save()
        try:

            employee.save()

            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "profile.html", locals())


def Logout(request):
    if not request.user.is_authenticated:
        return redirect("employee_login")
    logout(request)
    return redirect("home")


def admin_login(request):
    error = ""
    if request.method == "POST":
        U = request.POST["username"]
        P = request.POST["password"]

        user = authenticate(username=U, password=P)

        if user:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        else:
            error = "yes"
    return render(request, "login_Admin.html", locals())


def employee_experience(request):

    if not request.user.is_authenticated:
        return redirect("employee_login")

    user = request.user
    print(request.user, "USER CURRENT")
    experience = StudentResult.objects.get(user=user)

    return render(request, "myexperience.html", locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect("employee_login")
    error = ""
    user = request.user
    experience = StudentResult.objects.get(user=user)
    if request.method == "POST":
        c1n = request.POST["c1name"]
        c1desig = request.POST["c1desig"]
        c1d = request.POST["c1d"]
        c1s = request.POST["c1s"]

        c2n = request.POST["c2name"]
        c2desig = request.POST["c2desig"]
        c2d = request.POST["c2d"]
        c2s = request.POST["c2s"]

        c3n = request.POST["c3name"]
        c3desig = request.POST["c3desig"]
        c3d = request.POST["c3d"]
        c3s = request.POST["c3s"]

        experience.Company1Name = c1n
        experience.Company1Desig = c1desig
        experience.Company1Duration = c1d
        experience.Company1salary = c1s

        experience.Company2Name = c2n
        experience.Company2Desig = c2desig
        experience.Company2Duration = c2d
        experience.Company2salary = c2s

        experience.Company3Name = c3n
        experience.Company3Desig = c3desig
        experience.Company3Duration = c3d
        experience.Company3salary = c3s

        try:

            experience.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "edit_experience.html", locals())


def employee_education(request):

    if not request.user.is_authenticated:
        return redirect("employee_login")

    user = request.user
    education = EmployeeEducation1.objects.get(user=user)

    return render(request, "my_education.html", locals())


def edit_education(request):
    if not request.user.is_authenticated:
        return redirect("employee_login")
    error = ""
    user = request.user
    education = EmployeeEducation1.objects.get(user=user)
    if request.method == "POST":
        PG = request.POST["PostGraduation"]
        COLL = request.POST["CollegePG"]
        YOP1 = request.POST["YearOfPassing1"]
        PGP = request.POST["PGPercentage"]

        G = request.POST["Graduation"]
        GC = request.POST["CollegeGraduation"]
        YOP2 = request.POST["YearOfPassing2"]
        GP = request.POST["GraduationPercentage"]

        HSC = request.POST["CourseHSC"]
        HC = request.POST["CollegeHSC"]
        YOP3 = request.POST["YearOfPassing3"]
        HP = request.POST["HSCPercentage"]

        SSC = request.POST["CourseSSC"]
        SC = request.POST["CollegeSSC"]
        YOP4 = request.POST["YearOfPassing4"]
        SP = request.POST["SSCPercentage"]

        education.PostGraduation = PG
        education.CollegePG = COLL
        education.YearOfPassing1 = YOP1
        education.PGPercentage = PGP

        education.Graduation = G
        education.CollegeGraduation = GC
        education.YearOfPassing2 = YOP2
        education.GraduationPercentage = GP

        education.CourseHSC = HSC
        education.CollegeHSC = HC
        education.YearOfPassing3 = YOP3
        education.HSCPercentage = HP

        education.CourseSSC = SSC
        education.CollegeSSC = SC
        education.YearOfPassing4 = YOP4
        education.SSCPercentage = SP

        try:

            education.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "edit_my_education.html", locals())


def change_password(request):
    error = ""
    user = request.user
    if request.method == "POST":
        currentpass = request.POST["currentpass"]
        NewPass = request.POST["newpass"]
        ConfirmNew = request.POST["confnewpass"]
        if NewPass != ConfirmNew:
            messages.success(
                request, " New password and Confirm Password Should Be Same  !!!")
            return redirect("change_password")
        else:
            if user.check_password(currentpass):
                user.set_password(NewPass)
                user.save()
                error = "no"
            else:
                error = "yes"

    return render(request, "change_password.html", locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    return render(request, "admin_home.html")


def admin_change_password(request):
    error = ""
    user = request.user
    if request.method == "POST":
        currentpass = request.POST["currentpass"]
        NewPass = request.POST["newpass"]
        ConfirmNew = request.POST["confnewpass"]
        if NewPass != ConfirmNew:
            messages.success(
                request, " New password and Confirm Password Should Be Same  !!!")
            return redirect("change_password")
        else:
            if user.check_password(currentpass):
                user.set_password(NewPass)
                user.save()
                error = "no"
            else:
                error = "yes"

    return render(request, "admin_change_pass.html", locals())


def admin_Logout(request):
    if not request.user.is_authenticated:
        return redirect("employee_login")
    logout(request)
    return redirect("admin_login")


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    employee = EmployeeCreate.objects.all()
    return render(request, "all_employee.html", locals())


def delete_employee(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user = User.objects.get(id=pid)
    user.delete()
    return redirect("all_employee")


def edit_employee(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error = ""

    employee = EmployeeCreate.objects.get(id=pid)
    if request.method == "POST":
        N = request.POST["Fname"]
        L = request.POST["Lname"]

        EC = request.POST["Ecode"]

        Edesig = request.POST["Edesig"]
        ED = request.POST["ED"]
        ECONT = request.POST["contact"]
        JDate = request.POST["Jdate"]
        G = request.POST["gender"]

        if JDate:
            employee.date_created = JDate

        employee.user.first_name = N
        employee.user.last_name = L
        employee.Ecode = EC
        employee.Edesignation = Edesig
        employee.Econtact = ECONT
        employee.Edepartment = ED
        employee.FirstName = N
        employee.gender = G
        employee.LastName = L

        # employee.save()

        # employee.user.save()
        try:

            employee.save()

            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "edit_employee.html", locals())


def edit_education_admin(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation1.objects.get(user=user)
    if request.method == "POST":
        PG = request.POST["PostGraduation"]
        COLL = request.POST["CollegePG"]
        YOP1 = request.POST["YearOfPassing1"]
        PGP = request.POST["PGPercentage"]

        G = request.POST["Graduation"]
        GC = request.POST["CollegeGraduation"]
        YOP2 = request.POST["YearOfPassing2"]
        GP = request.POST["GraduationPercentage"]

        HSC = request.POST["CourseHSC"]
        HC = request.POST["CollegeHSC"]
        YOP3 = request.POST["YearOfPassing3"]
        HP = request.POST["HSCPercentage"]

        SSC = request.POST["CourseSSC"]
        SC = request.POST["CollegeSSC"]
        YOP4 = request.POST["YearOfPassing4"]
        SP = request.POST["SSCPercentage"]

        education.PostGraduation = PG
        education.CollegePG = COLL
        education.YearOfPassing1 = YOP1
        education.PGPercentage = PGP

        education.Graduation = G
        education.CollegeGraduation = GC
        education.YearOfPassing2 = YOP2
        education.GraduationPercentage = GP

        education.CourseHSC = HSC
        education.CollegeHSC = HC
        education.YearOfPassing3 = YOP3
        education.HSCPercentage = HP

        education.CourseSSC = SSC
        education.CollegeSSC = SC
        education.YearOfPassing4 = YOP4
        education.SSCPercentage = SP

        try:

            education.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "edit_education_admin.html", locals())


def edit_experience_admin(request, pid):
    if not request.user.is_authenticated:
        return redirect("employee_login")
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        c1n = request.POST["c1name"]
        c1desig = request.POST["c1desig"]
        c1d = request.POST["c1d"]
        c1s = request.POST["c1s"]

        c2n = request.POST["c2name"]
        c2desig = request.POST["c2desig"]
        c2d = request.POST["c2d"]
        c2s = request.POST["c2s"]

        c3n = request.POST["c3name"]
        c3desig = request.POST["c3desig"]
        c3d = request.POST["c3d"]
        c3s = request.POST["c3s"]

        experience.Company1Name = c1n
        experience.Company1Desig = c1desig
        experience.Company1Duration = c1d
        experience.Company1salary = c1s

        experience.Company2Name = c2n
        experience.Company2Desig = c2desig
        experience.Company2Duration = c2d
        experience.Company2salary = c2s

        experience.Company3Name = c3n
        experience.Company3Desig = c3desig
        experience.Company3Duration = c3d
        experience.Company3salary = c3s

        try:

            experience.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "edit_experience_admin.html", locals())


def CsV_File_Expo(request):

    studs_details = EmployeeCreate.objects.values_list(
        "FirstName", "LastName", "Ecode", "Econtact", "Email", "date_created", "cover")
    response = HttpResponse(content_type="text/csv")

    csv_writer = csv.writer(response)
    fields = ["FirstName", "LastName", "Ecode",
              "Econtact", "Email", "date_created", "cover"]
    csv_writer.writerow(fields)

    for i in studs_details:
        csv_writer.writerow(i)

    response['Content-Disposition'] = " attachments ; filename = export_csv.csv "
    return response

def downloadresult(request,pid):

    test_details = TestResults.objects.get(id=pid)
    response = HttpResponse(content_type="text/csv")
    print(test_details)
    csv_writer = csv.writer(response)
    fields = [ "TestName", "TestTopics", "Material",]
    csv_writer.writerow(fields)

    csv_writer.writerow((test_details.TestName, test_details.TestTopics, test_details.Material,))

    response['Content-Disposition'] = " attachments ; filename = export_csv.csv "
    return response



def results(request):
    result = TestResults.objects.all()
    return render(request, "testresult.html", context= {"result":result})

def uploadresult(request):
    if request.method == "POST":
        

        name = request.POST["NAME"]
        topics = request.POST["TOPICS"]
        file = request.FILES["FILE"]
        print(name,topics)
        obj = TestResults.objects.create(
            TestName=name, TestTopics=topics, Material=file)
        obj.save()
        return redirect("results")
    else:
        return render(request, "uploadresult.html", locals())
def uploadmaterial(request):
    if request.method == "POST":
        
        name = request.POST["NAME"]
        topcis = request.POST["TOPICS"]
        file = request.FILES["FILE"]
        obj = StudyMaterial.objects.create(
            SubjectName=name, SubjectTopics=topcis, Material=file)
        obj.save()
        return render(request, "studymaterial.html", locals())
    else:
        return render(request, "uploadmaterial.html", locals())

def deletematerial(request,id):
    material = StudyMaterial.objects.get(id = id)
    print("hhhhhhhhhhhhhhh",material,"hhhhhhhhhhhhhhhhhhhhhhhh")

    material.delete()
    return redirect("material")
def deleteresult(request,id):
    material = TestResults.objects.get(id = id)
    print("hhhhhhhhhhhhhhh",material,"hhhhhhhhhhhhhhhhhhhhhhhh")
    material.delete()
    return redirect("results")
def material(request):
    
    material = StudyMaterial.objects.all()
    print(material)
    return render(request,"studymaterial.html", locals())