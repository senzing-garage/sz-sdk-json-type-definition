/*
For more information, visit https://jsontypedef.com/docs/go-codegen/
*/
package main

import (
	"encoding/json"
	"fmt"

	"github.com/senzing-garage/g2-sdk-json-type-definition/go/typedef"
)

func main() {
	jsonString := `{"DATA_SOURCES":[{"DSRC_ID":1,"DSRC_CODE":"TEST"},{"DSRC_ID":2,"DSRC_CODE":"SEARCH"}]}`
	jsonStruct := typedef.G2configListDataSourcesResponse{}
	err := json.Unmarshal([]byte(jsonString), &jsonStruct)
	if err != nil {
		panic(err)
	}

	for _, datasource := range jsonStruct.DataSources {
		fmt.Printf("ID: %d  Code: %s\n", datasource.DsrcID, datasource.DsrcCode)
	}

	reconstructedString, err := json.Marshal(jsonStruct)
	if err != nil {
		panic(err)
	}

	fmt.Printf("     Original JSON: %s\n", jsonString)
	fmt.Printf("Reconstructed JSON: %s - notice JSON keys have been sorted.\n", string(reconstructedString))
}
