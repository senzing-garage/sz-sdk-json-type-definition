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

func outputln(message ...any) {
	fmt.Println(message...) //nolint
}

func outputf(format string, message ...any) {
	fmt.Printf(format, message...) //nolint
}

func pathToTestdata(filename string) string {
	return "./testdata/" + filename
}

func mockSzEngineGetVirtualEntityByRecordID() string {
	filePath := pathToTestdata("SzEngineGetVirtualEntityByRecordIdResponse-test-001.json")

	result, err := os.ReadFile(filePath)
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

	outputf(
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

		outputln(" ADDRESS FEAT_DESC:", addressStruct.FeatDesc)
	}

	// Show reconstructed (Unmarshall/Marshall) JSON.

	jsonString := `{"DATA_SOURCES":[{"DSRC_ID":1,"DSRC_CODE":"TEST"},{"DSRC_ID":2,"DSRC_CODE":"SEARCH"}]}`
	jsonStruct := typedef.SzConfigGetDataSourceRegistryResponse{}

	if err = json.Unmarshal([]byte(jsonString), &jsonStruct); err != nil {
		panic(err)
	}

	for _, datasource := range jsonStruct.DataSources {
		outputf("                ID: %d  Code: %s\n", datasource.DsrcID, datasource.DsrcCode)
	}

	reconstructedString, err := json.Marshal(jsonStruct)
	if err != nil {
		panic(err)
	}

	outputf("     Original JSON: %s\n", jsonString)
	outputf("Reconstructed JSON: %s - notice JSON keys have been sorted.\n",
		string(reconstructedString))
}
