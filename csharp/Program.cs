// See https://aka.ms/new-console-template for more information

using Senzing.Schema;
using System.Net;
using System.Security.Cryptography.X509Certificates;
using System.Text.Json;


namespace Bob

{
    internal class Program
    {
        static void Main(string[] args)
        {

            Program myProgram = new Program();

            // ----------------------------------------------------------------
            // Demonstrate creating input parameter and parsing output result.
            // ----------------------------------------------------------------

            Console.WriteLine("--- Demonstrate creating input parameter and parsing output result ------------\n\n");

            // Example of creating a JSON input parameter.
            // The advantage is that this is checked at compilation time.

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

            string recordKeysJson = JsonSerializer.Serialize(recordKeyStruct);


            SzEngineGetVirtualEntityByRecordIdRecordKeys? xyz = JsonSerializer.Deserialize<SzEngineGetVirtualEntityByRecordIdRecordKeys>(recordKeysJson);

            Console.WriteLine(">>>>> {0:G}", xyz);

            // Simulate calling Senzing SDK.

            string response = myProgram.mockSzEngineGetVirtualEntityByRecordID(recordKeysJson, 1);

            // Parse response.  FIXME;

            SzEngineGetVirtualEntityByRecordIdResponse? virtualEntity = JsonSerializer.Deserialize<SzEngineGetVirtualEntityByRecordIdResponse>(response);

            if (virtualEntity != null)
            {

                // string x = virtualEntity.Value.ResolvedEntity.Features["ADDRESS"][0].FEAT_DESC;
                string x = virtualEntity.Value.ResolvedEntity.Features["ADDRESS"][0].FeatDesc;

                Console.WriteLine("RESOLVED_ENTITY.FEATURES['ADDRESS'][0].FEAT_DESC: {0:G}\n", x);
            }
        }

        public string mockSzEngineGetVirtualEntityByRecordID(string recordKeys, int flags)
        {
            if (flags > 0)
            {
                Console.WriteLine("recordKeys Parameter: {0:G}\n", recordKeys);
            }

            string currentPath = Directory.GetCurrentDirectory();
            string filePath = currentPath + "/testdata/SzEngineGetVirtualEntityByRecordIdResponse-test-001.json";

            string result = "";
            StreamReader file = new StreamReader(filePath);

            try
            {
                string? line = file.ReadLine();
                while (line != null)
                {
                    result += line;
                    line = file.ReadLine();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }
            finally
            {
                file.Close();
            }

            return result;
        }

    }
}
