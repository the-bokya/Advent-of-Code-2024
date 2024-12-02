package main

import (
	"day2/part1"
	"day2/part2"
	"flag"
	"fmt"
)

func main() {
	part := flag.Int("part", 0, "Specify the part")
	flag.Parse()
	switch *part {
	case 1:
		fmt.Println(part1.Result())
	case 2:
		fmt.Println(part2.Result())
	}
}
