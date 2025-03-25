/*
Module sz-sdk-jackson-type-definition has input/output types for Senzing API SDKs.
*/
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/senzing-garage/sz-sdk-json-type-definition/go/typedef"
)

func pathToTestdata(filename string) string {
	return "./testdata/" + filename
}

func mockSzEngineGetVirtualEntityByRecordID() string {
	result, err := os.ReadFile(pathToTestdata("SzEngineGetVirtualEntityByRecordIdResponse-test-001.json"))
	if err != nil {
		panic(err)
	}

	return string(result)
}

func main() {
	var err error

	// Simulate response from Senzing SDK API.

	response := mockSzEngineGetVirtualEntityByRecordID()
	virtualEntity := typedef.SzEngineGetVirtualEntityByRecordIDResponse{}

	if err := json.Unmarshal([]byte(response), &virtualEntity); err != nil {
		panic(err)
	}

	fmt.Printf(
		"RESOLVED_ENTITY.FEATURES['ADDRESS'][0].FEAT_DESC: %s\n",
		virtualEntity.ResolvedEntity.Features["ADDRESS"][0].FeatDesc,
	)

	// Looping through list.

	addresses := virtualEntity.ResolvedEntity.Features["ADDRESS"]
	for _, address := range addresses {
		addressBytes, err := json.Marshal(address)
		if err != nil {
			panic(err)
		}

		addressStruct := typedef.FeatureForAttribute{}

		if err = json.Unmarshal(addressBytes, &addressStruct); err != nil {
			panic(err)
		}

		fmt.Println(" ADDRESS FEAT_DESC:", addressStruct.FeatDesc)
	}

	// Show reconstructed (Unmarshall/Marshall) JSON.

	jsonString := `{"DATA_SOURCES":[{"DSRC_ID":1,"DSRC_CODE":"TEST"},{"DSRC_ID":2,"DSRC_CODE":"SEARCH"}]}`
	jsonStruct := typedef.SzConfigGetDataSourcesResponse{}

	if err = json.Unmarshal([]byte(jsonString), &jsonStruct); err != nil {
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
