/*
For more information, visit https://jsontypedef.com/docs/go-codegen/
*/
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"reflect"

	"github.com/senzing-garage/g2-sdk-json-type-definition/go/typedef"
)

func pathToTestdata(filename string) string {
	return fmt.Sprintf("./testdata/%s", filename)

}

func mockG2engineGetVirtualEntityByRecordId() string {
	x, err := os.ReadFile(pathToTestdata("G2EngineGetVirtualEntityByRecordIdResponse-test-001.json"))
	if err != nil {
		panic(err)
	}
	return string(x)
}

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

	response := mockG2engineGetVirtualEntityByRecordId()
	jsonStruct2 := typedef.G2engineGetVirtualEntityByRecordIDResponse{}
	err = json.Unmarshal([]byte(response), &jsonStruct2)
	if err != nil {
		panic(err)
	}

	featureList := jsonStruct2.ResolvedEntity.Features.(map[string]any)

	fmt.Println("featureList:", reflect.TypeOf(featureList))
	fmt.Println(featureList["ADDRESS"])

	address := featureList["ADDRESS"].([]any)
	fmt.Println("address:", reflect.TypeOf(address))
	fmt.Println(address)

	address2 := address[0]
	fmt.Println("address2:", reflect.TypeOf(address2))
	fmt.Println(address2)

	myBytes, err := json.Marshal(address2)
	if err != nil {
		panic(err)
	}

	jsonStruct3 := typedef.FeatureForAttribute{}
	err = json.Unmarshal(myBytes, &jsonStruct3)
	if err != nil {
		panic(err)
	}

	fmt.Println("Final:", jsonStruct3.FeatDesc)

}
