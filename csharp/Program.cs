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

            Console.WriteLine("--- Demonstrate creating input parameter and parsing output result ------------\n");

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

            // Simulate calling Senzing SDK.

            string response = myProgram.mockSzEngineGetVirtualEntityByRecordID(recordKeysJson, 1);

            // Parse response.

            SzEngineGetVirtualEntityByRecordIdResponse? virtualEntity = JsonSerializer.Deserialize<SzEngineGetVirtualEntityByRecordIdResponse>(response);
            if (virtualEntity != null)
            {
                Console.WriteLine("RESOLVED_ENTITY.FEATURES['ADDRESS'][0].FEAT_DESC: {0:G}\n",
                    virtualEntity.Value.ResolvedEntity.Features["ADDRESS"][0].FeatDesc);

                // Looping through list.

                IList<FeatureForAttribute> addresses = virtualEntity.Value.ResolvedEntity.Features["ADDRESS"];
                foreach (FeatureForAttribute address in addresses)
                {
                    Console.WriteLine("   ADDRESS FEAT_DESC: {0:G}", address.FeatDesc);
                }
            }

            // ----------------------------------------------------------------
            // Demonstrate reconstructed JSON.
            // ----------------------------------------------------------------

            Console.WriteLine("\n--- Demonstrate reconstructed JSON --------------------------------------------\n");
            string jsonString = "{\"DATA_SOURCES\":[{\"DSRC_ID\":1,\"DSRC_CODE\":\"TEST\"},{\"DSRC_ID\":2,\"DSRC_CODE\":\"SEARCH\"}]}";

            // Unmarshall JSON string into a structure.

            SzConfigGetDataSourceRegistryResponse? dataSourceRegistry = JsonSerializer.Deserialize<SzConfigGetDataSourceRegistryResponse>(jsonString);

            // Show individual (ID, Code) pairs.

            if (dataSourceRegistry != null)
            {
                foreach (DataSource datasource in dataSourceRegistry.Value.DataSources)
                {
                    Console.WriteLine("                ID: {0:G}  Code: {1:G}", datasource.DsrcId, datasource.DsrcCode);
                }
            }

            // Reconstruct JSON.

            string reconstructedString = JsonSerializer.Serialize(dataSourceRegistry);

            // Compare original and reconstructed JSON.

            Console.WriteLine("     Original JSON: {0:G}", jsonString);
            Console.WriteLine("Reconstructed JSON: {0:G} - notice JSON keys have been sorted.\n", reconstructedString);

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
