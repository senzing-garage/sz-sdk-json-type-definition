// # For more information, visit https://jsontypedef.com/docs/java-codegen/

import com.senzing.schema.SzConfigGetDataSourceRegistryResponse;
import com.senzing.schema.GetDataSourceRegistry;
import com.senzing.schema.DataSource;

import java.util.Map;
import java.util.List;
import com.fasterxml.jackson.databind.ObjectMapper;

class Main {
    public static void main(String[] args) {

        // --------------------------------------------------------------------
        // Demonstrate reconstructed JSON.
        // --------------------------------------------------------------------

        System.out.printf("\n--- Demonstrate reconstructed JSON --------------------------------------------\n");

        try {
        String jsonString = "{\"DATA_SOURCES\":[{\"DSRC_ID\":1,\"DSRC_CODE\":\"TEST\"},{\"DSRC_ID\":2,\"DSRC_CODE\":\"SEARCH\"}]}";

        // Unmarshall JSON string into a object.

        ObjectMapper objectMapper = new ObjectMapper();
        SzConfigGetDataSourceRegistryResponse jsonStruct = objectMapper.readValue(jsonString,
                SzConfigGetDataSourceRegistryResponse.class);

        // Show individual (ID, Code) pairs.

        GetDataSourceRegistry dataSourceRegistry = jsonStruct.getValue();


        for (DataSource dataSource : dataSourceRegistry.getDataSources()) {
            System.out.printf("                ID: %s  Code: %s\n", dataSource.getDsrcId(), dataSource.getDsrcCode());
        }

        // Reconstruct JSON.

        String reconstructedString = objectMapper.writeValueAsString(jsonStruct);

        // Compare original and reconstructed JSON.

        System.out.printf("     Original JSON: %s\n", jsonString);
        System.out.printf("Reconstructed JSON: %s - notice JSON keys have been sorted.\n", reconstructedString);
        } catch (Exception e) {

        }
    }
}