// See https://aka.ms/new-console-template for more information

using Newtonsoft.Json;

var obj = new
{
    EmpID = "Larry",
    Name = "Larry The Man",
    Shift = new[] {
        new { StartTime = "1 AM" },
        new { StartTime = "2 PM" }
    }
};

string json = JsonConvert.SerializeObject(obj);

Console.WriteLine("Hello, World!");
