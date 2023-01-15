package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"os"
	"os/exec"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "9988"
	SERVER_TYPE = "tcp"
)

// '/'//'/'//'//'/'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'
// '/'//'/'//'//'/'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'
// '/'//'/'//'//'/'//'//'//'//'---------------'//'//'//'//'//'//'//'//'//'//'
// '/'//'/'//'//'/'//'//'//'//| YİĞİT GÜMÜŞ  |//'//'//'//'//'//'//'//'//'//'//'
// '/'//'/'//'//'/'//'//'//'//---------------/'//'//'//'//'//'//'//'//'//'//'
// '/'//'/'//'//'/'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'
// '/'//'/'//'//'/'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'//'
var data string

func saveData(data []byte) int {
	content, err := ioutil.ReadFile("../../config.json")
	if err != nil {
		log.Fatal("Error when opening file:", err)
	}

	var payload map[string]interface{}
	err = json.Unmarshal(content, &payload)
	if err != nil {
		log.Fatal("Error during Unmarshal: ", err)
	}

	println(payload["fileToEncrypt"])
	return 0
}

func runProgram() string {
	out, err := exec.Command("python3", "../../cli.py", "-cd").Output()
	if err != nil {
		log.Fatal(err)
	}
	return string(out)
}

func main() {

	fmt.Println("Server Running...")
	server, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		fmt.Println("Error listening:", err.Error())
		os.Exit(1)
	}
	defer server.Close()
	fmt.Println("Listening on " + SERVER_HOST + ":" + SERVER_PORT)
	fmt.Println("Waiting for client...")
	for {
		connection, err := server.Accept()
		if err != nil {
			fmt.Println("Error accepting: ", err.Error())
			os.Exit(1)
		}
		fmt.Println("A client connected")
		go processClient(connection)
	}
}
func processClient(connection net.Conn) {
	defer connection.Close()
	buffer := make([]byte, 1024)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("Error reading:", err.Error())
	}
	fmt.Println("Received: ", string(buffer[:mLen]))
	// declared in global scope look at it! line: 22
	data = string(buffer[:mLen])
	// - - - - - - - - - - - - - - - - - -
}
