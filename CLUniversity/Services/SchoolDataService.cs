using CLUniversity.Models;
using Newtonsoft.Json;

namespace CLUniversity.Services;

public class SchoolDataService
{
    private readonly string _dataFile = "Data/school_data.json";
    private SchoolData _data;

    public SchoolDataService()
    {
        _data = LoadData();
    }

    private SchoolData LoadData()
    {
        if (File.Exists(_dataFile))
        {
            var json = File.ReadAllText(_dataFile);
            return JsonConvert.DeserializeObject<SchoolData>(json) ?? new SchoolData();
        }
        return new SchoolData();
    }

    private void SaveData()
    {
        Directory.CreateDirectory("Data");
        File.WriteAllText(_dataFile, JsonConvert.SerializeObject(_data, Formatting.Indented));
    }

    // Students
    public List<Student> GetStudents() => _data.Students;
    public Student? GetStudent(string id) => _data.Students.FirstOrDefault(s => s.Id == id);
    public void AddStudent(Student student)
    {
        student.StudentId = $"STU{DateTime.Now:yyyy}{_data.Students.Count + 1:D4}";
        _data.Students.Add(student);
        SaveData();
    }
    public void DeleteStudent(string id)
    {
        _data.Students.RemoveAll(s => s.Id == id);
        SaveData();
    }

    // Lecturers
    public List<Lecturer> GetLecturers() => _data.Lecturers;
    public void AddLecturer(Lecturer lecturer)
    {
        lecturer.LecturerId = $"LEC{DateTime.Now:yyyy}{_data.Lecturers.Count + 1:D4}";
        _data.Lecturers.Add(lecturer);
        SaveData();
    }
    public void DeleteLecturer(string id)
    {
        _data.Lecturers.RemoveAll(l => l.Id == id);
        SaveData();
    }

    // Staff
    public List<Staff> GetStaff() => _data.Staff;
    public void AddStaff(Staff staff)
    {
        staff.StaffId = $"STF{DateTime.Now:yyyy}{_data.Staff.Count + 1:D4}";
        _data.Staff.Add(staff);
        SaveData();
    }
    public void DeleteStaff(string id)
    {
        _data.Staff.RemoveAll(s => s.Id == id);
        SaveData();
    }

    // Departments
    public List<Department> GetDepartments() => _data.Departments;
    public Department? GetDepartment(string id) => _data.Departments.FirstOrDefault(d => d.Id == id);
    public void AddDepartment(Department dept)
    {
        _data.Departments.Add(dept);
        SaveData();
    }

    // Courses
    public List<Course> GetCourses() => _data.Courses;
    public void AddCourse(Course course)
    {
        _data.Courses.Add(course);
        SaveData();
    }

    // Payments
    public List<Payment> GetPayments() => _data.Payments;
    public void AddPayment(Payment payment)
    {
        _data.Payments.Add(payment);
        SaveData();
    }
    public void UpdatePaymentStatus(string md5, string status)
    {
        var payment = _data.Payments.FirstOrDefault(p => p.Md5 == md5);
        if (payment != null)
        {
            payment.Status = status;
            payment.PaidAt = DateTime.Now;
            SaveData();
        }
    }
    public Payment? GetPaymentByMd5(string md5) => _data.Payments.FirstOrDefault(p => p.Md5 == md5);

    // Salaries
    public List<Salary> GetSalaries() => _data.Salaries;
    public void AddSalary(Salary salary)
    {
        _data.Salaries.Add(salary);
        SaveData();
    }
    public void PaySalary(string id)
    {
        var salary = _data.Salaries.FirstOrDefault(s => s.Id == id);
        if (salary != null)
        {
            salary.Status = "paid";
            salary.PaidAt = DateTime.Now;
            SaveData();
        }
    }

    // Stats
    public DashboardStats GetStats() => new()
    {
        TotalStudents = _data.Students.Count(s => s.Status == "active"),
        TotalLecturers = _data.Lecturers.Count(l => l.Status == "active"),
        TotalStaff = _data.Staff.Count(s => s.Status == "active"),
        TotalCourses = _data.Courses.Count,
        TotalDepartments = _data.Departments.Count,
        TotalPayments = _data.Payments.Where(p => p.Status == "paid").Sum(p => p.Amount),
        PendingPayments = _data.Payments.Where(p => p.Status == "pending").Sum(p => p.Amount),
        TotalSalariesPaid = _data.Salaries.Where(s => s.Status == "paid").Sum(s => s.Amount),
        PendingSalaries = _data.Salaries.Where(s => s.Status == "pending").Sum(s => s.Amount)
    };
}

public class SchoolData
{
    public List<Student> Students { get; set; } = new();
    public List<Lecturer> Lecturers { get; set; } = new();
    public List<Staff> Staff { get; set; } = new();
    public List<Department> Departments { get; set; } = new();
    public List<Course> Courses { get; set; } = new();
    public List<Payment> Payments { get; set; } = new();
    public List<Salary> Salaries { get; set; } = new();
}

public class DashboardStats
{
    public int TotalStudents { get; set; }
    public int TotalLecturers { get; set; }
    public int TotalStaff { get; set; }
    public int TotalCourses { get; set; }
    public int TotalDepartments { get; set; }
    public decimal TotalPayments { get; set; }
    public decimal PendingPayments { get; set; }
    public decimal TotalSalariesPaid { get; set; }
    public decimal PendingSalaries { get; set; }
}
