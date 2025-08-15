// See https://aka.ms/new-console-template for more information

using Senzing.Schema;
using System.Text.Json;


namespace Bob

{

    // ------------------------------------------------------------------------
    // Demonstrate creating input parameter and parsing output result.
    // ------------------------------------------------------------------------

    public class Account
    {
        public string? Name { get; set; }
        public string? Email { get; set; }
        public DateTime DOB { get; set; }
    }
    internal class Program
    {
        static void Main(string[] args)
        {

            IList<RecordKey> recordKeyList = new List<RecordKey>();

            RecordKey recordKey1 = new RecordKey
            {
                DataSource = "DATA_SOURCE_1",
                RecordId = "RECORD_ID_1"
            };
            recordKeyList.Add(recordKey1);

            RecordKey recordKey2 = new RecordKey
            {
                DataSource = "DATA_SOURCE_2",
                RecordId = "RECORD_ID_2"
            };
            recordKeyList.Add(recordKey2);

            RecordKeys recordKeys = new RecordKeys
            {
                Records = recordKeyList
            };

            SzEngineGetVirtualEntityByRecordIdRecordKeys recordKeyStruct = new SzEngineGetVirtualEntityByRecordIdRecordKeys
            {
                Value = recordKeys
            };



            Account account = new Account
            {
                Name = "John Doe",
                Email = "john@nuget.org",
                DOB = new DateTime(1980, 2, 20, 0, 0, 0, DateTimeKind.Utc),
            };

            // string json = JsonConvert.SerializeObject(account, Formatting.Indented);
            string json2 = JsonSerializer.Serialize(recordKeyStruct);
            Console.WriteLine(json2);
        }
    }
}
