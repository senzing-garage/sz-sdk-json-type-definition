/*
For more information, visit https://jsontypedef.com/docs/go-codegen/
*/
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/senzing-garage/g2-sdk-json-type-definition/go/typedef"
)

func pathToTestdata(filename string) string {
	return fmt.Sprintf("./testdata/%s", filename)
}

func mockG2engineGetVirtualEntityByRecordId() string {
	result, err := os.ReadFile(pathToTestdata("G2EngineGetVirtualEntityByRecordIdResponse-test-001.json"))
	if err != nil {
		panic(err)
	}
	return string(result)
}

func main() {

	// Simulate response from Senzing SDK API.

	response := mockG2engineGetVirtualEntityByRecordId()
	responseStruct := typedef.G2engineGetVirtualEntityByRecordIDResponse{}
	err := json.Unmarshal([]byte(response), &responseStruct)
	if err != nil {
		panic(err)
	}

	featureList := responseStruct.ResolvedEntity.Features.(map[string]any)
	addresses := featureList["ADDRESS"].([]any)
	for _, address := range addresses {

		addressBytes, err := json.Marshal(address)
		if err != nil {
			panic(err)
		}

		addressStruct := typedef.FeatureForAttribute{}
		err = json.Unmarshal(addressBytes, &addressStruct)
		if err != nil {
			panic(err)
		}

		fmt.Println(" ADDRESS FEAT_DESC:", addressStruct.FeatDesc)
	}

	// Show reconstructed (Unmarshall/Marshall) JSON.

	jsonString := `{"DATA_SOURCES":[{"DSRC_ID":1,"DSRC_CODE":"TEST"},{"DSRC_ID":2,"DSRC_CODE":"SEARCH"}]}`
	jsonStruct := typedef.G2configListDataSourcesResponse{}
	err = json.Unmarshal([]byte(jsonString), &jsonStruct)
	if err != nil {
		panic(err)
	}

	for _, datasource := range jsonStruct.DataSources {
		fmt.Printf("                ID: %d  Code: %s\n", datasource.DsrcID, datasource.DsrcCode)
	}

	reconstructedString, err := json.Marshal(jsonStruct)
	if err != nil {
		panic(err)
	}

	fmt.Printf("     Original JSON: %s\n", jsonString)
	fmt.Printf("Reconstructed JSON: %s - notice JSON keys have been sorted.\n", string(reconstructedString))
}
