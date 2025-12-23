namespace CLUniversity.Models;

public class Student
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string StudentId { get; set; } = "";
    public string FirstName { get; set; } = "";
    public string LastName { get; set; } = "";
    public string Email { get; set; } = "";
    public string Phone { get; set; } = "";
    public string Gender { get; set; } = "";
    public string DepartmentId { get; set; } = "";
    public string Status { get; set; } = "active";
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public string FullName => $"{FirstName} {LastName}";
}

public class Lecturer
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string LecturerId { get; set; } = "";
    public string FirstName { get; set; } = "";
    public string LastName { get; set; } = "";
    public string Email { get; set; } = "";
    public string Phone { get; set; } = "";
    public string Qualification { get; set; } = "";
    public string DepartmentId { get; set; } = "";
    public decimal Salary { get; set; }
    public string Status { get; set; } = "active";
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public string FullName => $"{FirstName} {LastName}";
}

public class Staff
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string StaffId { get; set; } = "";
    public string FirstName { get; set; } = "";
    public string LastName { get; set; } = "";
    public string Email { get; set; } = "";
    public string Phone { get; set; } = "";
    public string Position { get; set; } = "";
    public string DepartmentId { get; set; } = "";
    public decimal Salary { get; set; }
    public string Status { get; set; } = "active";
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public string FullName => $"{FirstName} {LastName}";
}

public class Department
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Code { get; set; } = "";
    public string Name { get; set; } = "";
    public string Description { get; set; } = "";
    public DateTime CreatedAt { get; set; } = DateTime.Now;
}

public class Course
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Code { get; set; } = "";
    public string Name { get; set; } = "";
    public int Credits { get; set; } = 3;
    public string DepartmentId { get; set; } = "";
    public decimal FeePerCredit { get; set; } = 50;
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public decimal TotalFee => Credits * FeePerCredit;
}

public class Payment
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string BillNumber { get; set; } = "";
    public string StudentId { get; set; } = "";
    public decimal Amount { get; set; }
    public string Currency { get; set; } = "USD";
    public string PaymentType { get; set; } = "tuition";
    public string Md5 { get; set; } = "";
    public string Status { get; set; } = "pending";
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public DateTime? PaidAt { get; set; }
}

public class Salary
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string EmployeeId { get; set; } = "";
    public string EmployeeType { get; set; } = "";
    public string EmployeeName { get; set; } = "";
    public decimal Amount { get; set; }
    public int Month { get; set; }
    public int Year { get; set; }
    public string Status { get; set; } = "pending";
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public DateTime? PaidAt { get; set; }
}

public class QRCodeResult
{
    public bool Success { get; set; }
    public string QrImage { get; set; } = "";
    public string QrData { get; set; } = "";
    public string Md5 { get; set; } = "";
    public string BillNumber { get; set; } = "";
    public string Error { get; set; } = "";
}

public class Receipt
{
    public string BillNumber { get; set; } = "";
    public string StudentName { get; set; } = "";
    public string StudentId { get; set; } = "";
    public string PaymentType { get; set; } = "";
    public decimal Amount { get; set; }
    public string Currency { get; set; } = "";
    public DateTime PaidAt { get; set; }
    public string TransactionId { get; set; } = "";
}
