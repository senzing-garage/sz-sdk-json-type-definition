// # For more information, visit https://jsontypedef.com/docs/java-codegen/

import com.senzing.schema.ConfigListDataSourcesResponse;
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper;

class Main {
    public static void main(String[] args) {
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonString = "{\"DATA_SOURCES\":[{\"DSRC_ID\":1,\"DSRC_CODE\":\"TEST\"},{\"DSRC_ID\":2,\"DSRC_CODE\":\"SEARCH\"}]}";
        ConfigListDataSourcesResponse jsonStruct = objectMapper.readValue(jsonString,
                ConfigListDataSourcesResponse.class);

        // TODO: Loop through jsonStruct to print "ID: {0} Code: {1}"

        jsonStruct.ConfigListDataSourcesResponse

        String reconstructedString = objectMapper.writeValueAsString(jsonString);
        System.out.printf("     Original JSON: %s%n", jsonString);
        System.out.printf("Reconstructed JSON: %s%n", reconstructedString);
    }
}