package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	as := make(map[int]int)
	bs := make(map[int]int)
	for {
		l, _, err := reader.ReadLine()
		if err != nil {
			break
		}
		nums := strings.Split(string(l), "   ")

		a, _ := strconv.Atoi(nums[0])
		b, _ := strconv.Atoi(nums[1])
		as[a] += 1
		bs[b] += 1
	}
	count := 0
	for k, v := range as {
		count += k * v * bs[k]
	}
	fmt.Println(count)
}
