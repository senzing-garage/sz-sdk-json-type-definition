/*
Module sz-sdk-jackson-type-definition has input/output types for Senzing API SDKs.
*/
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/senzing-garage/sz-sdk-json-type-definition/go/typedef"
)

func main() {
	var err error
	ctx := context.Background()

	// ------------------------------------------------------------------------
	// Demonstrate creating input parameter and parsing output result.
	// ------------------------------------------------------------------------

	outputf("--- Demonstrate creating input parameter and parsing output result ------------\n\n")

	// Example of creating a JSON input parameter.
	// The advantage is that this is checked at compilation time.

	recordKeysStruct := typedef.SzEngineGetVirtualEntityByRecordIDRecordKeys{
		Records: []typedef.RecordKey{
			{
				DataSource: "DATA_SOURCE_1",
				RecordID:   "RECORD_ID_1",
			},
			{
				DataSource: "DATA_SOURCE_2",
				RecordID:   "RECORD_ID_2",
			},
		},
	}

	recordKeysBytes, err := json.Marshal(recordKeysStruct)
	if err != nil {
		panic(err)
	}

	// Simulate calling Senzing SDK.

	response, err := mockSzEngineGetVirtualEntityByRecordID(ctx, string(recordKeysBytes), 0)

	// Parse response.

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

		outputln("   ADDRESS FEAT_DESC:", addressStruct.FeatDesc)
	}

	// ------------------------------------------------------------------------
	// Demonstrate reconstructed JSON.
	// ------------------------------------------------------------------------

	outputf("\n--- Demonstrate reconstructed JSON --------------------------------------------\n\n")
	jsonString := `{"DATA_SOURCES":[{"DSRC_ID":1,"DSRC_CODE":"TEST"},{"DSRC_ID":2,"DSRC_CODE":"SEARCH"}]}`

	// Unmarshall JSON string into a structure.

	jsonStruct := typedef.SzConfigGetDataSourceRegistryResponse{}
	if err = json.Unmarshal([]byte(jsonString), &jsonStruct); err != nil {
		panic(err)
	}

	// Show individual (ID, Code) pairs.

	for _, datasource := range jsonStruct.DataSources {
		outputf("                ID: %d  Code: %s\n", datasource.DsrcID, datasource.DsrcCode)
	}

	// Reconstruct JSON.

	reconstructedString, err := json.Marshal(jsonStruct)
	if err != nil {
		panic(err)
	}

	// Compare original and reconstructed JSON.

	outputf("     Original JSON: %s\n", jsonString)
	outputf("Reconstructed JSON: %s - notice JSON keys have been sorted.\n",
		string(reconstructedString))
}

func outputln(message ...any) {
	fmt.Println(message...) //nolint
}

func outputf(format string, message ...any) {
	fmt.Printf(format, message...) //nolint
}

func pathToTestdata(filename string) string {
	return "./testdata/" + filename
}

func mockSzEngineGetVirtualEntityByRecordID(ctx context.Context, recordKeys string, flags int64) (string, error) {
	_ = ctx
	_ = flags

	outputf("recordKeys Parameter: %s\n", recordKeys)

	filePath := pathToTestdata("SzEngineGetVirtualEntityByRecordIdResponse-test-001.json")
	result, err := os.ReadFile(filePath)

	return string(result), err
}
