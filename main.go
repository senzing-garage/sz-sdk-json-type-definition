/*
For more information, visit https://jsontypedef.com/docs/go-codegen/
*/
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/senzing-garage/sz-sdk-json-type-definition/go/typedef"
)

func pathToTestdata(filename string) string {
	return fmt.Sprintf("./testdata/%s", filename)
}

func mockSzEngineGetVirtualEntityByRecordId() string {
	result, err := os.ReadFile(pathToTestdata("SzEngineGetVirtualEntityByRecordIdResponse-test-001.json"))
	if err != nil {
		panic(err)
	}
	return string(result)
}

func main() {

	// Simulate response from Senzing SDK API.

	response := mockSzEngineGetVirtualEntityByRecordId()
	virtualEntity := typedef.SzEngineGetVirtualEntityByRecordIDResponse{}
	err := json.Unmarshal([]byte(response), &virtualEntity)
	if err != nil {
		panic(err)
	}
	fmt.Printf("RESOLVED_ENTITY.FEATURES['ADDRESS'][0].FEAT_DESC: %s\n", virtualEntity.ResolvedEntity.Features["ADDRESS"][0].FeatDesc)

	// Looping through list.

	addresses := virtualEntity.ResolvedEntity.Features["ADDRESS"]
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
	jsonStruct := typedef.SzConfigGetDataSourcesResponse{}
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
