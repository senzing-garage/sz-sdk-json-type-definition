// # For more information, visit https://jsontypedef.com/docs/java-codegen/

import com.senzing.schema.SzConfigGetDataSourceRegistryResponse;
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper;

class Main {
    public static void main(String[] args) {

        // --------------------------------------------------------------------
        // Demonstrate reconstructed JSON.
        // --------------------------------------------------------------------

        try {
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonString = "{\"DATA_SOURCES\":[{\"DSRC_ID\":1,\"DSRC_CODE\":\"TEST\"},{\"DSRC_ID\":2,\"DSRC_CODE\":\"SEARCH\"}]}";
        SzConfigGetDataSourceRegistryResponse jsonStruct = objectMapper.readValue(jsonString,
                SzConfigGetDataSourceRegistryResponse.class);


        bob = jsonStruct.DATA_SOURCES

        // TODO: Loop through jsonStruct to print "ID: {0} Code: {1}"


        String reconstructedString = objectMapper.writeValueAsString(jsonString);
        System.out.printf("     Original JSON: %s%n", jsonString);
        System.out.printf("Reconstructed JSON: %s%n", reconstructedString);
        } catch (Exception e) {

        }
    }
}