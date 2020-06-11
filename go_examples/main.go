// A trivial web server written in go, for benchmarking purposes.

package main

import (
	"fmt"
	"html"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// APIRoot trivial api root page
func APIRoot(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "{ }")
}

// Index trivial api index page
func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
}

func main() {

	fmt.Println("Welcome to trivial web server written in go.")

	router := mux.NewRouter().StrictSlash(true)

	// router.HandleFunc("/", APIRoot)
	router.HandleFunc("/", Index)

	log.Fatal(http.ListenAndServe("localhost:7081", router))

	fmt.Println("web server returned, exiting.")
}
